def leer_entrada():
    with open("entrada.txt", "r") as entrada_f:
        return entrada_f.read()

def calcular_prioridad_de_char(char):
    # A a la Z (mayúscula)
    if ord(char) >= 65 and ord(char) <= 90:
        return ord(char) - 38
    # a a la z (minúscula)
    elif ord(char) >= 97 and ord(char) <= 122:
        return ord(char) - 96

def main():
    entrada = leer_entrada().split("\n")

    suma_prioridades1 = 0
    for linea in entrada:
        char = ""
        for i in range(int(len(linea) / 2)):
            char_actual = linea[i]
            if char_actual in linea[-int(len(linea) / 2):]:
                char = char_actual
                break
        
        suma_prioridades1 += calcular_prioridad_de_char(char)

    suma_prioridades2 = 0
    for i in range(int(len(entrada) / 3)):
        for char in entrada[i * 3]:
            if char in entrada[i * 3 + 1] and char in entrada[i * 3 + 2]:
                suma_prioridades2 += calcular_prioridad_de_char(char)
                break

    print(f"Respuesta 1: {suma_prioridades1}")
    print(f"Respuesta 2: {suma_prioridades2}")

if __name__ == "__main__":
    main()