Olvera De la Huerta Santiago

# Tiro Parabólico

Este es un programa en Python que resuelve problemas de tiro parabólico y grafica la trayectoria de un proyectil en movimiento parabólico.

## Descripción del Problema

El programa resuelve dos tipos de problemas de tiro parabólico:

### Problema 1
Un jugador de Fútbol Americano patea el balón con una velocidad de 30 m/s, y éste mismo lleva un ángulo de elevación de 48° respecto a la horizontal. Se deben calcular los siguientes valores:
- Altura máxima alcanzada por el proyectil.
- Alcance horizontal.
- Tiempo de vuelo.

### Problema 2
En este caso, se le pide al usuario que elija una opción para resolver un problema específico relacionado con el tiro parabólico. Las opciones son:
1. Calcular altura máxima.
2. Calcular alcance horizontal.
3. Calcular tiempo de vuelo.
4. Calcular posición en un tiempo dado.

El usuario debe proporcionar los datos necesarios según la opción elegida y el programa calculará y mostrará el resultado correspondiente, además de graficar la trayectoria del proyectil.

## Solución

El programa utiliza las fórmulas y ecuaciones del movimiento en tiro parabólico para realizar los cálculos necesarios. Se han implementado las siguientes funciones para cada uno de los cálculos:

- `calcular_altura(v0, theta)`: Calcula la altura máxima alcanzada por el proyectil.
- `calcular_alcance(v0, theta)`: Calcula el alcance horizontal del proyectil.
- `calcular_tiempo_vuelo(v0, theta)`: Calcula el tiempo de vuelo del proyectil.
- `calcular_velocidad_inicial_horizontal(v0, theta)`: Calcula la componente horizontal de la velocidad inicial.
- `calcular_velocidad_inicial_vertical(v0, theta)`: Calcula la componente vertical de la velocidad inicial.
- `calcular_velocidad_horizontal(v0, theta, t)`: Calcula la componente horizontal de la velocidad en un tiempo dado.
- `calcular_velocidad_vertical(v0, theta, t)`: Calcula la componente vertical de la velocidad en un tiempo dado.
- `calcular_posicion_horizontal(x0, v0, theta, t)`: Calcula la posición horizontal en un tiempo dado.
- `calcular_posicion_vertical(y0, v0, theta, t)`: Calcula la posición vertical en un tiempo dado.

El programa también incluye las funciones `resolver_problema_1()` y `resolver_problema_2()` que implementan la lógica para resolver los problemas mencionados y mostrar los resultados correspondientes.

Para ejecutar el programa, simplemente sigue las instrucciones que se mostrarán en la consola.

## Requisitos del Sistema

- Python 3.x
- Bibliotecas: matplotlib, math

## Ejecución

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala las bibliotecas necesarias ejecutando el siguiente comando en tu terminal:
pip install matplotlib
3. Descarga los archivos del programa en tu sistema.
4. Abre una terminal y navega hasta la ubicación donde se encuentran los archivos descargados.
5. Ejecuta el programa utilizando el siguiente
python tiro_parabolico.py
6. Sigue las instrucciones que se mostrarán en la consola para resolver el problema deseado.
