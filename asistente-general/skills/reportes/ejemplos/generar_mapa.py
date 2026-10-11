"""Contornos simplificados de Espana para los modulos mapa_ccaa y mapa_provincias.

Fuente: Natural Earth, ne_10m_admin_1_states_provinces (dominio publico), descargado en esta
carpeta. Agrupa las provincias en comunidades, proyecta, simplifica, coloca Canarias en un
recuadro (un solo desplazamiento para todas sus islas) y deja Ceuta y Melilla como puntos.
Uso: python3 generar_mapa.py   (necesita pyshp y shapely)
"""
import json, math, unicodedata
import shapefile
from shapely.geometry import shape, Polygon, MultiPolygon
from shapely.ops import unary_union, transform
from shapely.affinity import translate

CCAA = {"Andalucía": ("ES-AN", "Andalucia"), "Aragón": ("ES-AR", "Aragon"), "Asturias": ("ES-AS", "Asturias"), "Canary Is.": ("ES-CN", "Canarias"),
  "Cantabria": ("ES-CB", "Cantabria"), "Castilla y León": ("ES-CL", "Castilla y Leon"), "Castilla-La Mancha": ("ES-CM", "Castilla-La Mancha"),
  "Cataluña": ("ES-CT", "Cataluna"), "Extremadura": ("ES-EX", "Extremadura"), "Galicia": ("ES-GA", "Galicia"), "Islas Baleares": ("ES-IB", "Illes Balears"),
  "La Rioja": ("ES-RI", "La Rioja"), "Madrid": ("ES-MD", "Comunidad de Madrid"), "Murcia": ("ES-MC", "Region de Murcia"), "Foral de Navarra": ("ES-NC", "Navarra"),
  "País Vasco": ("ES-PV", "Pais Vasco"), "Valenciana": ("ES-VC", "Comunitat Valenciana"), "Ceuta": ("ES-CE", "Ceuta"), "Melilla": ("ES-ML", "Melilla")}
PROV_NOMBRE = {"La Coruña": "A Coruna", "Orense": "Ourense", "Lérida": "Lleida", "Gerona": "Girona", "Baleares": "Illes Balears", "Álava": "Araba/Alava"}
K, LAT0, LON0, CS, TOL, AREA_MIN = 46.0, 43.9, -9.5, math.cos(math.radians(40)), 0.9, 2.0

def ascii(s): return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
def proy(g): return transform(lambda x, y, z=None: ((x - LON0) * CS * K, (LAT0 - y) * K), g)

r = shapefile.Reader("ne_10m_admin_1_states_provinces")
provs = [(sr.record["name"], sr.record["region"], sr.record["iso_3166_2"], proy(shape(sr.shape.__geo_interface__)))
         for sr in r.shapeRecords() if sr.record["adm0_a3"] == "ESP"]
# Canarias: un unico desplazamiento para todas sus islas, abajo a la derecha (bajo Baleares y Murcia).
canarias = unary_union([g for n, reg, i, g in provs if reg == "Canary Is."]).bounds
DX, DY = 478 - canarias[2], 398 - canarias[3]
RECUADRO = [round(canarias[0] + DX) - 8, round(canarias[1] + DY) - 8, round(canarias[2] - canarias[0]) + 16, round(canarias[3] - canarias[1]) + 16]
def colocar(g, region): return translate(g, xoff=DX, yoff=DY) if region == "Canary Is." else g

def ruta(g):
    """Ruta SVG relativa y entera; h/v para los pasos horizontales o verticales."""
    g = g.simplify(TOL, preserve_topology=True)
    partes = []
    for p in ([g] if isinstance(g, Polygon) else list(g.geoms)):
        if p.area < AREA_MIN: continue
        pts = [(round(x), round(y)) for x, y in p.exterior.coords[:-1]]
        pts = [pts[0]] + [q for a, q in zip(pts, pts[1:]) if q != a]
        if len(pts) < 3: continue
        s, prev, modo = "M%d %d" % pts[0], pts[0], ""
        for q in pts[1:]:
            dx, dy = q[0] - prev[0], q[1] - prev[1]
            if dy == 0: s += "h%d" % dx; modo = ""
            elif dx == 0: s += "v%d" % dy; modo = ""
            else:
                s += ("l" if modo != "l" else (" " if dx >= 0 else "")) + ("%d %d" % (dx, dy)).replace(" -", "-"); modo = "l"
            prev = q
        partes.append(s + "z")
    return "".join(partes)

def zonas(nivel):
    if nivel == "ccaa":
        grupos = {}
        for n, reg, i, g in provs: grupos.setdefault(reg, []).append(colocar(g, reg))
        items = [(CCAA[reg][0], CCAA[reg][1], unary_union(gs)) for reg, gs in grupos.items()]
    else:
        items = [(iso, ascii(PROV_NOMBRE.get(n, n)), colocar(g, reg)) for n, reg, iso, g in provs]
    return {cod: [nombre, ruta(g)] for cod, nombre, g in items if cod not in ("ES-CE", "ES-ML")}

puntos = {}
for n, reg, iso, g in provs:
    if iso in ("ES-CE", "ES-ML"): c = g.centroid; puntos[iso] = [n, round(c.x), round(c.y)]
print("constantes:", json.dumps({"puntos": puntos, "recuadro": RECUADRO}))
for nivel in ("ccaa", "provincias"):
    js = json.dumps(zonas(nivel), ensure_ascii=True, separators=(",", ":"))
    open("zonas_%s.json" % nivel, "w").write(js)
    print(nivel, len(js), "bytes")
