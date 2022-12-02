def leer_entrada():
    with open("entrada.txt", "r") as entrada_f:
        return entrada_f.read()

def calcular_puntuacion(partes):
    puntuacion = 0
    for parte in partes:
        if parte[1] == "X":
            puntuacion += 1
        elif parte[1] == "Y":
            puntuacion += 2
        elif parte[1] == "Z":
            puntuacion += 3
        
        if (parte[0] == "A" and parte[1] == "X") or \
           (parte[0] == "B" and parte[1] == "Y") or \
           (parte[0] == "C" and parte[1] == "Z"):
           puntuacion += 3
        elif (parte[0] == "A" and parte[1] == "Y") or \
             (parte[0] == "B" and parte[1] == "Z") or \
             (parte[0] == "C" and parte[1] == "X"):
             puntuacion += 6
    return puntuacion

def main():
    entrada = leer_entrada().split("\n")
    partes = []
    for linea in entrada:
        partes.append(linea.split(" "))

    puntuacion1 = calcular_puntuacion(partes)

    for i in range(len(partes)):
        if partes[i][1] == "Y":
            if partes[i][0] == "A":
                partes[i][1] = "X"
            elif partes[i][0] == "B":
                partes[i][1] = "Y"
            elif partes[i][0] == "C":
                partes[i][1] = "Z"
        elif partes[i][1] == "X":
            if partes[i][0] == "A":
                partes[i][1] = "Z"
            elif partes[i][0] == "B":
                partes[i][1] = "X"
            elif partes[i][0] == "C":
                partes[i][1] = "Y"
        elif partes[i][1] == "Z":
            if partes[i][0] == "A":
                partes[i][1] = "Y"
            elif partes[i][0] == "B":
                partes[i][1] = "Z"
            elif partes[i][0] == "C":
                partes[i][1] = "X"

    puntuacion2 = calcular_puntuacion(partes)

    print(f"Respuesta 1: {puntuacion1}")
    print(f"Respuesta 2: {puntuacion2}")


if __name__ == "__main__":
    main()