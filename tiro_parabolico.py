import math
import matplotlib.pyplot as plt

g = 9.81  # Aceleración de la gravedad en m/s^2

def calcular_altura(v0, theta):
    return (v0 * math.sin(math.radians(theta)))**2 / (2 * g)

def calcular_alcance_horizontal(v0, theta):
    return (v0**2 * math.sin(2 * math.radians(theta))) / g

def calcular_tiempo_vuelo(v0, theta):
    return (2 * v0 * math.sin(math.radians(theta))) / g

def calcular_posicion(x0, y0, v0, theta, t):
    x = x0 + (v0 * math.cos(math.radians(theta))) * t
    y = y0 + (v0 * math.sin(math.radians(theta))) * t - (0.5 * g * t**2)
    return x, y

def calcular_velocidad_inicial(v0, theta):
    v0x = v0 * math.cos(math.radians(theta))
    v0y = v0 * math.sin(math.radians(theta))
    return v0x, v0y

def calcular_velocidad(v0, theta, t):
    vx = v0 * math.cos(math.radians(theta))
    vy = v0 * math.sin(math.radians(theta)) - g * t
    return vx, vy

def resolver_problema():
    print("Resolver problema de tiro parabólico:")
    print("1. Calcular altura")
    print("2. Calcular alcance horizontal")
    print("3. Calcular tiempo de vuelo")
    print("4. Calcular posición en un tiempo dado")
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        v0 = float(input("Ingrese la velocidad inicial (m/s): "))
        theta = float(input("Ingrese el ángulo de elevación (grados): "))
        altura = calcular_altura(v0, theta)
        print(f"La altura máxima alcanzada es: {altura} metros")

    elif opcion == 2:
        v0 = float(input("Ingrese la velocidad inicial (m/s): "))
        theta = float(input("Ingrese el ángulo de elevación (grados): "))
        alcance = calcular_alcance_horizontal(v0, theta)
        print(f"El alcance horizontal es: {alcance} metros")

    elif opcion == 3:
        v0 = float(input("Ingrese la velocidad inicial (m/s): "))
        theta = float(input("Ingrese el ángulo de elevación (grados): "))
        tiempo_vuelo = calcular_tiempo_vuelo(v0, theta)
        print(f"El tiempo de vuelo es: {tiempo_vuelo} segundos")

    elif opcion == 4:
        x0 = float(input("Ingrese la posición inicial en x (m): "))
        y0 = float(input("Ingrese la posición inicial en y (m): "))
        v0 = float(input("Ingrese la velocidad inicial (m/s): "))
        theta = float(input("Ingrese el ángulo de elevación (grados): "))
        t = float(input("Ingrese el tiempo (s): "))
        posicion = calcular_posicion(x0, y0, v0, theta, t)
        print(f"La posición en el tiempo {t} es: ({posicion[0]}, {posicion[1]}) metros")

        # Graficar el tiro parabólico
        t_values = [i / 100 for i in range(int(tiempo_vuelo * 100) + 1)]
        x_values = [calcular_posicion(x0, y0, v0, theta, t)[0] for t in t_values]
        y_values = [calcular_posicion(x0, y0, v0, theta, t)[1] for t in t_values]

        plt.plot(x_values, y_values)
        plt.xlabel('Distancia (m)')
        plt.ylabel('Altura (m)')
        plt.title('Tiro Parabólico')
        plt.show()

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

resolver_problema()
