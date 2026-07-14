# Operaciones aéreas de Chile

Proyecto del examen transversal de **Programación para la Ciencia de Datos**. Integra datos oficiales de operaciones aeroportuarias, una API REST de feriados de Chile y un catálogo abierto de aeropuertos.

## Objetivo

Analizar la evolución de las operaciones aéreas de Chile, clasificar la actividad mensual por aeropuerto y tipo de operación, y descubrir perfiles de aeropuertos mediante aprendizaje no supervisado.

## Contenido técnico

- Validación, limpieza y transformación con Pandas.
- Pipeline ETL con tres fuentes.
- API REST de Nager.Date.
- Regresión logística y árbol de decisión.
- Accuracy, precision, recall, F1 y matriz de confusión.
- Evaluación temporal: entrenamiento 2022-2025 y prueba enero-junio de 2026.
- K-Means, silhouette y PCA.
- Visualizaciones interactivas con Plotly.
- Pruebas automáticas con Pytest y GitHub Actions.
- Entorno reproducible mediante Docker.

## Estructura

```text
.
├── .github/workflows/ci.yml
├── data/operaciones-aeropuertos.csv
├── notebooks/Proyecto_Operaciones_Aereas_Chile_COLAB.ipynb
├── tests/test_project.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Ejecución en Google Colab

1. Abrir el notebook de la carpeta `notebooks/` en Google Colab.
2. Ejecutar todas las celdas.
3. Subir `data/operaciones-aeropuertos.csv` cuando Colab lo solicite.
4. Las fuentes de feriados y aeropuertos se descargan automáticamente.

## Pruebas locales

```bash
python -m pip install -r requirements-dev.txt
pytest -q
```

Las pruebas comprueban que:

- El CSV tiene el esquema esperado.
- No existen nulos, duplicados ni operaciones negativas.
- Los meses y tipos de operación son válidos.
- El notebook conserva todas sus celdas ejecutadas y sin errores.
- Todas las celdas de Python tienen sintaxis válida.

## Docker

Construir la imagen:

```bash
docker build -t operaciones-aereas-chile .
```

Ejecutar las pruebas dentro del contenedor:

```bash
docker run --rm operaciones-aereas-chile
```

## Integración continua

El workflow `.github/workflows/ci.yml` se ejecuta automáticamente en cada `push` y `pull request`. Instala las dependencias y ejecuta las pruebas. Una marca verde en la pestaña **Actions** constituye la evidencia de CI/CD.

## Fuentes

- Junta de Aeronáutica Civil / Datos.gob.cl: https://datos.gob.cl/dataset/operaciones-aeronaves
- Nager.Date API: https://date.nager.at/Api
- OurAirports: https://ourairports.com/data/

## Limitaciones

- Los datos de 2026 llegan hasta junio y no representan un año completo.
- La API de feriados utilizada en el modelo cubre 2022-2026.
- Las asociaciones observadas no demuestran causalidad.
- Los clusters representan perfiles estadísticos, no categorías oficiales.

