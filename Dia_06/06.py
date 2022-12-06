def leer_entrada():
    with open("entrada.txt", "r") as entrada_f:
        return entrada_f.read()

def buscar_n_distintos(n, chars):
    ultimos_chars = []
    posicion_marcador = 0
    for i in range(len(chars)):
        if len(ultimos_chars) != n:
            ultimos_chars.append(chars[i])
            continue

        if len(set(ultimos_chars)) == len(ultimos_chars):
            posicion_marcador = i
            break
        else:
            for j in range(len(ultimos_chars) - 1):
                ultimos_chars[j] = ultimos_chars[j + 1]
            ultimos_chars[-1] = chars[i]
    
    return posicion_marcador

def main():
    entrada = leer_entrada()
    
    print(f"Respuesta 1: {buscar_n_distintos(4, entrada)}")
    print(f"Respuesta 2: {buscar_n_distintos(14, entrada)}") 

if __name__ == "__main__":
    main()