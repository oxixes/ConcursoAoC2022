def leer_entrada():
    with open("entrada.txt", "r") as entrada_f:
        return entrada_f.read()

def main():
    entrada = leer_entrada().split("\n")

    veces_contenido = 0
    veces_superpuesto = 0
    for linea in entrada:
        partes = []
        for parte in linea.split(","):
            partes.append(parte.split("-"))
        if (int(partes[0][0]) <= int(partes[1][0]) and \
           int(partes[0][1]) >= int(partes[1][1])) or \
           (int(partes[1][0]) <= int(partes[0][0]) and \
           int(partes[1][1]) >= int(partes[0][1])):
            veces_contenido += 1

        if ((int(partes[0][0]) >= int(partes[1][0]) and \
           int(partes[0][0]) <= int(partes[1][1])) or \
           (int(partes[0][1]) >= int(partes[1][0]) and \
           int(partes[0][1]) <= int(partes[1][1]))) or \
           ((int(partes[1][0]) >= int(partes[0][0]) and \
           int(partes[1][0]) <= int(partes[0][1])) or \
           (int(partes[1][1]) >= int(partes[0][0]) and \
           int(partes[1][1]) <= int(partes[0][1]))):
            veces_superpuesto += 1
    
    print(f"Respuesta 1: {veces_contenido}")
    print(f"Respuesta 2: {veces_superpuesto}")

if __name__ == "__main__":
    main()