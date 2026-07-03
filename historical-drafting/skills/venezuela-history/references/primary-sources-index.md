# primary-sources-index

> Material de referencia para la skill `venezuela-history`. Indice de archivos, repositorios y bibliotecas digitales de fuentes primarias para la historia de Venezuela. Lo lee Claude al aplicar el procedimiento para localizar fuentes trazables. NO se incluye en el output al usuario.

## Proposito

Este indice sirve como punto de partida cuando Claude necesita verificar o complementar hechos y no tiene fuentes aportadas por el usuario. Su funcion es reducir el numero de busquedas web necesarias y mejorar la calidad de la trazabilidad.

## Como usar este archivo

1. Para cada hecho factual a triangular, identificar si alguno de los repositorios listados contiene material relevante.
2. Si la fuente esta digitalizada y accesible, citarla como fuente primaria con localizador (URL, numero de documento, etc.).
3. Si la fuente solo esta disponible en archives fisicos, marcar `[verificar: fuente fisica]` y recomendar al usuario consulta presencial o reproduccion digital via repositorio cooperativo.
4. Si ningun repositorio del indice es util, pasar a busqueda web con `io.gravitonai.tools.web_search`.

## Archivos y repositorios

### 1. Archivo General de la Nacion (AGN)

- **Sede**: Caracas, Venezuela.
- **Cobertura**: periodo colonial en adelante; documentos oficiales, correspondencia, registros administrativos.
- **Acceso digital**: parcial via portal del AGN; resto bajo consulta presencial o solicitud de reproduccion.
- **URL de referencia**: https://agn.gob.ve/ (verificar disponibilidad al momento de uso).
- **Riesgo**: URLs y politicas de acceso cambian. Verificar antes de citar.

### 2. Biblioteca Nacional de Venezuela

- **Sede**: Caracas, Venezuela.
- **Cobertura**: publicaciones oficiales, periodicos historicos, materiales editoriales.
- **Acceso digital**: catalogo en linea; digitalizaciones parciales.
- **URL de referencia**: http://www.bnv.gob.ve/ (verificar al uso).
- **Utilidad**: localizar ediciones originales de la Gaceta Oficial y periodicos de epoca.

### 3. Gaceta Oficial de Venezuela (historica)

- **Cobertura**: desde 1811 (primer numero de la Republica) hasta la actualidad.
- **Acceso digital**: algunos anios digitalizados en repositorios universitarios y en la Biblioteca Nacional; coleccion incompleta en linea.
- **Utilidad**: fuente primaria para leyes, decretos, resoluciones oficiales y actos administrativos.
- **Citacion**: incluir numero, fecha y, si aplica, URL del repositorio digitalizador.

### 4. Biblioteca Virtual Miguel de Cervantes

- **Sede**: Universidad de Alicante, Espana.
- **Cobertura**: literatura y documentos hispanoamericanos, con seccion dedicada a Venezuela.
- **Acceso digital**: abierto.
- **URL de referencia**: https://www.cervantesvirtual.com/
- **Utilidad**: localizar ediciones digitales de periodicos de epoca, cartas y documentos publicos.

### 5. Hemeroteca Digital de la Biblioteca Nacional de Espana (BNE)

- **Cobertura**: prensa hispanica, siglos XVIII-XXI, incluye publicaciones venezolanas y relativas a Venezuela.
- **Acceso digital**: abierto.
- **URL de referencia**: https://www.bne.es/es/Catalogos/HemerotecaDigital
- **Utilidad**: localizar periodicos contemporaneos a eventos historicos venezolanos, especialmente durante el periodo colonial y los primeros decenios republicanos.

### 6. Internet Archive (archive.org)

- **Cobertura**: materiales digitalizados, periodicos historicos, libros en dominio publico.
- **Acceso digital**: abierto, con descarga selectiva.
- **URL de referencia**: https://archive.org/
- **Utilidad**: localizar ediciones originales de textos historicos en dominio publico y periodicos digitalizados por terceros.
- **Nota**: la calidad de la digitalizacion varia; verificar transcripcion cuando se cite.

### 7. HathiTrust Digital Library

- **Cobertura**: libros y periodicos academicamente curados.
- **Acceso digital**: dominio publico abierto; resto bajo autenticacion institucional.
- **URL de referencia**: https://www.hathitrust.org/
- **Utilidad**: localizar ediciones criticas y compilaciones documentales.

### 8. Repositorios universitarios venezolanos

- **Ejemplos** (verificar URLs al uso):
  - Saber ULA (Universidad de Los Andes).
  - Revistas y tesis de la UCV (Universidad Central de Venezuela).
  - Deposito institucional de la USB (Universidad Simon Bolivar).
- **Utilidad**: localizar articulos academicos con revision por pares y tesis de grado/postgrado que pueden contener fuentes primarias editadas.

### 9. Catastro de fuentes oficiales internacionales

- **Ejemplos**:
  - Biblioteca del Congreso de EE.UU. (Country Studies; Law Library).
  - Biblioteca del Congreso de Chile y otras bibliotecas nacionales latinoamericanas (con secciones de historia venezolana).
- **Utilidad**: localizar estudios de pais y traducciones de documentos oficiales.

### 10. Colecciones especiales de periodicos y archivos sonoros

- **Ejemplos**:
  - Periódicos del s. XIX venezolano digitalizados por la Biblioteca Nacional o proyectos academicos especificos.
  - Fondos de la Biblioteca de la Academia Nacional de la Historia (Caracas).
  - Archivo de la palabra (testimonios orales) de la UCV.
- **Utilidad**: testimonios contemporaneos al evento, en formato hemerografico o sonoro.

## Cheat sheet rapido

| Tipo de fuente | Repositorio primario | Como citar |
|---|---|---|
| Documento oficial colonial | AGN; BNE; Internet Archive | AGN, Caja X, Folio Y, fecha Z |
| Ley / decreto / gaceta | Gaceta Oficial historica; BNV | Gaceta Oficial, numero N, fecha |
| Periodico de epoca | BNE Hemeroteca; Internet Archive | Periodico, fecha, pagina o URL |
| Carta / documento privado | AGN; Cerventes Virtual | AGN, Fondo X, anio, descripcion |
| Edicion academica critica | HathiTrust; Internet Archive | Autor, Titulo, Editor, anio, URL |
| Articulo academico con revision por pares | Repositorio universitario | Autor, Titulo, Revista, vol., num., anio, DOI/URL |

## Notas finales

Este indice es un esqueleto de trabajo. El equipo de investigacion debe expandirlo con repositorios especificos del area de interes (ej: archivos sindicales para el periodo 1936-1948; archivos eclesiasticos para el periodo colonial; fondos petroleros para 1908-1975). Las URLs y disponibilidades deben verificarse en el momento de uso.