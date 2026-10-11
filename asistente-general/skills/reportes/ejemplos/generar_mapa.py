import json, math, shapefile
from shapely.geometry import shape, Polygon, MultiPolygon, Point
from shapely.ops import unary_union, transform
from shapely.affinity import translate
CCAA = {"Andalucía": ("ES-AN", "Andalucia"), "Aragón": ("ES-AR", "Aragon"), "Asturias": ("ES-AS", "Asturias"), "Canary Is.": ("ES-CN", "Canarias"),
  "Cantabria": ("ES-CB", "Cantabria"), "Castilla y León": ("ES-CL", "Castilla y Leon"), "Castilla-La Mancha": ("ES-CM", "Castilla-La Mancha"),
  "Cataluña": ("ES-CT", "Cataluna"), "Extremadura": ("ES-EX", "Extremadura"), "Galicia": ("ES-GA", "Galicia"), "Islas Baleares": ("ES-IB", "Illes Balears"),
  "La Rioja": ("ES-RI", "La Rioja"), "Madrid": ("ES-MD", "Comunidad de Madrid"), "Murcia": ("ES-MC", "Region de Murcia"), "Foral de Navarra": ("ES-NC", "Navarra"),
  "País Vasco": ("ES-PV", "Pais Vasco"), "Valenciana": ("ES-VC", "Comunitat Valenciana"), "Ceuta": ("ES-CE", "Ceuta"), "Melilla": ("ES-ML", "Melilla")}
PROV_NOMBRE = {"La Coruña": "A Coruna", "Orense": "Ourense", "Lérida": "Lleida", "Gerona": "Girona", "Baleares": "Illes Balears", "Álava": "Araba/Alava",
  "Castellón": "Castellon", "Alicante": "Alicante", "Valencia": "Valencia"}
import unicodedata
def ascii(s): return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
r = shapefile.Reader("ne_10m_admin_1_states_provinces")
provs = []
for sr in r.shapeRecords():
    rec = sr.record
    if rec["adm0_a3"] != "ESP": continue
    provs.append((rec["name"], rec["region"], rec["iso_3166_2"], shape(sr.shape.__geo_interface__)))
K, LAT0, LON0, CS = 46.0, 43.9, -9.5, math.cos(math.radians(40))
def proy(lon, lat): return ((lon - LON0) * CS * K, (LAT0 - lat) * K)
def proyectar(g, canarias):
    g2 = transform(lambda x, y, z=None: proy(x, y), g)
    if canarias:  # recuadro abajo a la derecha, bajo Baleares y Murcia
        b = g2.bounds
        g2 = translate(g2, xoff=478 - b[2], yoff=398 - b[3])
    return g2
def limpiar(g, minimo):
    polys = [g] if isinstance(g, Polygon) else list(g.geoms)
    polys = [p for p in polys if p.area >= minimo]
    return MultiPolygon(polys) if len(polys) > 1 else polys[0]
def ruta(g, tol):
    g = g.simplify(tol, preserve_topology=True)
    polys = [g] if isinstance(g, Polygon) else list(g.geoms)
    partes = []
    for p in polys:
        pts = [(round(x), round(y)) for x, y in p.exterior.coords[:-1]]
        dedup = [pts[0]] + [q for a, q in zip(pts, pts[1:]) if q != a]
        if len(dedup) < 3: continue
        s = "M%d %d" % dedup[0]
        prev = dedup[0]
        rel = []
        for q in dedup[1:]:
            rel.append("%d %d" % (q[0] - prev[0], q[1] - prev[1])); prev = q
        partes.append(s + "l" + " ".join(rel).replace(" -", "-") + "z")
    return "".join(partes)
def construir(nivel, tol, minimo):
    salida, puntos = {}, {}
    if nivel == "ccaa":
        grupos = {}
        for nombre, region, iso, g in provs: grupos.setdefault(region, []).append(g)
        items = [(CCAA[reg][0], CCAA[reg][1], unary_union(gs), reg == "Canary Is.") for reg, gs in grupos.items()]
    else:
        items = [(iso, ascii(PROV_NOMBRE.get(nombre, nombre)), g, region == "Canary Is.") for nombre, region, iso, g in provs]
    for cod, nombre, g, can in items:
        gp = proyectar(g, can)
        if cod in ("ES-CE", "ES-ML"):
            c = gp.centroid; puntos[cod] = [nombre, round(c.x), round(c.y)]; continue
        gp = limpiar(gp, minimo)
        salida[cod] = [nombre, ruta(gp, tol)]
    return salida, puntos
for nivel, tol in (("ccaa", 0.9), ("provincias", 0.9)):
    zonas, puntos = construir(nivel, tol, 2.0)
    from shapely.geometry import box
    can = [proyectar(unary_union([g for n, r, i, g in provs if r == "Canary Is."]), True).bounds]
    c = can[0]
    marco = [round(c[0]) - 8, round(c[1]) - 8, round(c[2] - c[0]) + 16, round(c[3] - c[1]) + 16]
    js = json.dumps({"zonas": zonas, "puntos": puntos, "recuadro": marco, "lienzo": [500, 420]}, ensure_ascii=True, separators=(",", ":"))
    open("mapa_%s.json" % nivel, "w").write(js)
    print(nivel, len(zonas), "zonas", len(js), "bytes")
