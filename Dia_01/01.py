def leer_entrada():
    with open("entrada.txt", "r") as entrada_f:
        return entrada_f.read()

def main():
    entrada = leer_entrada()

    calorias_elfos = []
    for calorias in entrada.split("\n\n"):
        calorias_elfo = 0
        for calorias_item in calorias.split("\n"):
            calorias_elfo += int(calorias_item)

        calorias_elfos.append(calorias_elfo)
    
    # mayor = calorias_elfos[0]
    # for calorias in calorias_elfos:
    #     if calorias > mayor:
    #         mayor = calorias

    calorias_elfos.sort()

    print(f"Respuesta 1: {calorias_elfos[-1]}")
    print(f"Respuesta 2: {calorias_elfos[-1] + calorias_elfos[-2] + calorias_elfos[-3]}")

if __name__ == "__main__":
    main()