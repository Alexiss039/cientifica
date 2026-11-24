# Taller de grafos · Problema 4.7 «El tubo que no conviene»

**Entregables:** [`index.html`](index.html) (un solo archivo, doble clic, sin internet) y un video de 4 a 6 minutos explicándolo.

## El problema

La vereda inventada **Alto Verde** recibe agua de un tanque en la loma. La red tiene 10 puntos y 15 tubos, cada uno con su longitud en metros.

> **Pregunta:** ¿cuál es la menor longitud de tubería desde el Tanque El Alto hasta la Escuela?

**Algoritmo:** Dijkstra (pesos positivos, la pregunta es una suma de metros, no un conteo de tubos).

## El grafo (propio)

10 vértices: Tanque El Alto, Válvula Alta, Válvula Quebrada, Válvula Camino, Finca Los Pinos, Capilla, Lavadero, Tienda, Cancha y Escuela.

| Tubo | Metros | Tubo | Metros |
| --- | --- | --- | --- |
| Tanque – Válvula Alta | 120 | Válvula Alta – Capilla | 200 |
| Tanque – Válvula Quebrada | 210 | Finca – Válvula Camino | 170 |
| Tanque – Finca | **460** | Válvula Quebrada – Lavadero | 190 |
| Válvula Alta – Finca | 180 | Capilla – Tienda | 160 |
| Válvula Quebrada – Finca | 150 | Capilla – Válvula Camino | 140 |
| Válvula Camino – Cancha | **600** | Válvula Camino – Escuela | 400 |
| Tienda – Escuela | 300 | Cancha – Escuela | 150 |
| Lavadero – Cancha | 210 | | |

La diapositiva 3 del HTML muestra la lista de adyacencia, generada con los mismos datos que el dibujo.

## Respuesta

**760 m** en 4 tubos: Tanque El Alto → Válvula Quebrada → Lavadero → Cancha → Escuela (210 + 190 + 210 + 150).

## Los dos tubos que no convienen

| Tubo directo | Metros | Rodeo | Metros del rodeo |
| --- | --- | --- | --- |
| Tanque – Finca Los Pinos | 460 | Tanque → Válvula Alta → Finca | 300 |
| Válvula Camino – Cancha | 600 | Válvula Camino → Escuela → Cancha | 550 |

En el laboratorio, el botón **«Ver el tubo descartado»** salta al paso en que Válvula Camino (460 m) prueba el tubo hacia Cancha: 460 + 600 = 1060 m no mejora los 610 m que Cancha ya tenía por Lavadero.

Además, Válvula Alta se confirma a 120 m, antes que la Escuela, y no queda en la ruta final.

## Contraste con BFS (diapositiva de cierre)

Contar tubos llevaría por Tanque → Finca → Válvula Camino → Escuela: 3 tubos pero 1030 m. La ruta de Dijkstra usa 4 tubos y solo 760 m.

## Cómo está hecho

Se partió de la plantilla de la clase (`grafos/index.html`): se reutilizó el reproductor de pasos y los controles. Se cambiaron el grafo, los pesos, los textos de cada paso, la respuesta y las diapositivas, para que cuenten un solo problema. El HTML no tiene dependencias externas.

Controles: flechas ← → cambian de diapositiva; en el laboratorio, `N` y `P` mueven el algoritmo y la barra espaciadora lo reproduce.

## Revisión contra las reglas del taller

| Regla | Dónde se cumple |
| --- | --- |
| Un solo problema, de la lista | 4.7 |
| Grafo propio, de 6 a 14 vértices | 10 vértices, 15 tubos, distinto del ejemplo de clase |
| Pesos positivos escritos sobre la arista | cada tubo muestra sus metros en el dibujo |
| El largo del trazo no es el peso | aviso sobre el dibujo y en la diapositiva 2 |
| Lista de adyacencia con pesos | diapositiva 3 |
| Un paso donde el tubo directo se descarta | laboratorio, paso 20 de 32 |
| Cierre con ruta y total en metros | diapositiva 6 |
| Todo en español, sin nombres de personas reales | sí |
| Un solo HTML, doble clic, sin internet | `index.html` |
