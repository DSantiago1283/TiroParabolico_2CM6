import matplotlib.pyplot as plt
import math

g = 9.81  # Aceleración de la gravedad en m/s^2

def calcular_altura(v0, theta):
    theta_rad = math.radians(theta)
    v0y = v0 * math.sin(theta_rad)
    altura = (v0y ** 2) / (2 * g)
    return altura

def calcular_alcance(v0, theta):
    theta_rad = math.radians(theta)
    alcance = (v0 ** 2) * math.sin(2 * theta_rad) / g
    return alcance

def calcular_tiempo_vuelo(v0, theta):
    theta_rad = math.radians(theta)
    tiempo_vuelo = (2 * v0 * math.sin(theta_rad)) / g
    return tiempo_vuelo

def calcular_velocidad_inicial_horizontal(v0, theta):
    theta_rad = math.radians(theta)
    v0x = v0 * math.cos(theta_rad)
    return v0x

def calcular_velocidad_inicial_vertical(v0, theta):
    theta_rad = math.radians(theta)
    v0y = v0 * math.sin(theta_rad)
    return v0y

def calcular_velocidad_horizontal(v0, theta, t):
    theta_rad = math.radians(theta)
    vx = v0 * math.cos(theta_rad)
    return vx

def calcular_velocidad_vertical(v0, theta, t):
    vy = calcular_velocidad_inicial_vertical(v0, theta) - g * t
    return vy

def calcular_posicion_horizontal(x0, v0, theta, t):
    theta_rad = math.radians(theta)
    x = x0 + (v0 * math.cos(theta_rad)) * t
    return x

def calcular_posicion_vertical(y0, v0, theta, t):
    theta_rad = math.radians(theta)
    y = y0 + (v0 * math.sin(theta_rad)) * t - 0.5 * g * (t ** 2)
    return y

def calcular_posicion(x0, y0, v0, theta, t):
    theta_rad = math.radians(theta)
    x = x0 + (v0 * math.cos(theta_rad)) * t
    y = y0 + (v0 * math.sin(theta_rad)) * t - 0.5 * g * (t ** 2)
    return x, y

def resolver_problema_1():
    v0 = 30
    theta = 48

    altura = calcular_altura(v0, theta)
    alcance = calcular_alcance(v0, theta)
    tiempo_vuelo = calcular_tiempo_vuelo(v0, theta)

    print("Problema:")
    print("Un jugador de Fútbol Americano patea el balón con una velocidad de 30 m/s,")
    print("y éste mismo lleva un ángulo de elevación de 48° respecto a la horizontal.")
    print("Calcule:")
    print("a) Altura")
    print("b) Alcance")
    print("c) Tiempo que permanece en el aire")

    print(f"\nAltura: {altura} m")
    print(f"Alcance: {alcance} m")
    print(f"Tiempo de vuelo: {tiempo_vuelo} s")

    # Generar gráfica
    t_values = [0]
    dt = tiempo_vuelo / 100  # Dividimos el tiempo de vuelo en 100 intervalos
    while t_values[-1] < tiempo_vuelo:
        t_values.append(t_values[-1] + dt)

    x_values = [calcular_posicion_horizontal(0, v0, theta, t) for t in t_values]
    y_values = [calcular_posicion_vertical(0, v0, theta, t) for t in t_values]

    plt.plot(x_values, y_values)
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.title("Tiro Parabólico")
    plt.show()

def resolver_problema_2():
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
        alcance = calcular_alcance(v0, theta)
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

# Main
print("Bienvenido al solucionador de problemas de tiro parabólico")

resolver = input("¿Desea resolver el Problema 1 o el Problema 2? (1/2): ")

if resolver == "1":
    resolver_problema_1()
elif resolver == "2":
    resolver_problema_2()
else:
    print("Opción inválida")

1