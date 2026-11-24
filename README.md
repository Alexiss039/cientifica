# Introducción a la programación científica

Trabajos del curso, en el orden en que se hicieron. Cada carpeta tiene su propio README con el detalle.

## 1. Taller de modelos de predicción

Clasificar si un hurto a persona en Medellín fue **atraco o cosquilleo**, con baseline, split temporal, regresión logística y bosque aleatorio.

| Qué | Dónde |
| --- | --- |
| Notebook del taller | [notebooks/modelo prediccion modalidad.ipynb](notebooks/modelo%20prediccion%20modalidad.ipynb) |
| Datos de entrada | [data/processed/hurtos_medellin_hechos.csv](data/processed/hurtos_medellin_hechos.csv) |
| Análisis descriptivo del curso (referencia) | [notebooks/analisis de hurtos medellin.ipynb](notebooks/analisis%20de%20hurtos%20medellin.ipynb) |

## 2. Tarea 1: algoritmos greedy en LeetCode

Dos ejercicios resueltos en Python y aceptados en LeetCode: *Lemonade Change* y *Assign Cookies*.

| Qué | Dónde |
| --- | --- |
| README con criterio greedy y complejidad | [tarea1/README.md](tarea1/README.md) |
| Código | [tarea1/lemonade-change/](tarea1/lemonade-change/solution.py) y [tarea1/assign-cookies/](tarea1/assign-cookies/solution.py) |
| Capturas de *Accepted* | [tarea1/evidencias/](tarea1/evidencias/) |

## 3. Tarea 2: primer análisis en Google Colab

Análisis de los nacimientos del Hospital General de Medellín (datos.gov.co): limpieza, gráficos y un modelo para predecir **cesárea**.

| Qué | Dónde |
| --- | --- |
| README con dataset, limpieza y resultados | [tarea2/README.md](tarea2/README.md) |
| Notebook | [tarea2/analisis-nacimientos/tarea2-analisis.ipynb](tarea2/analisis-nacimientos/tarea2-analisis.ipynb) |
| Enlace de Colab | <https://colab.research.google.com/drive/1cfI8UMxTzCaQhO6lhiJ0zZa06pUXgIvj?usp=sharing> |
| Gráficos exportados | [tarea2/evidencias/](tarea2/evidencias/) |

## 4. Taller de grafos: problema 4.7 «El tubo que no conviene»

Dijkstra sobre la red de un acueducto veredal inventado: menor longitud de tubería del tanque a la escuela (**760 m**).

| Qué | Dónde |
| --- | --- |
| Entregable, un solo HTML (abrir con doble clic) | [taller-grafos/index.html](taller-grafos/index.html) |
| README con el grafo y la respuesta | [taller-grafos/README.md](taller-grafos/README.md) |

## Estructura

```text
.
├── README.md
├── data/processed/          datos de hurtos (taller de modelos)
├── notebooks/               notebooks del taller de modelos
├── tarea1/                  greedy en LeetCode
├── tarea2/                  análisis en Colab
└── taller-grafos/           problema 4.7 con Dijkstra
```
