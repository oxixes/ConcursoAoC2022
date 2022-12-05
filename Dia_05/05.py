import re

def leer_entrada():
    with open("entrada.txt", "r") as entrada_f:
        return entrada_f.read()

def main():
    entrada = leer_entrada().split("\n\n")
    num_stacks = int(entrada[0].split("\n")[-1].split(" ")[-2])
    stacks = []
    for _ in range(num_stacks):
        stacks.append([])

    for linea_items in reversed(entrada[0].split("\n")[0:-1]):
        temp = list(linea_items)
        del temp[3::4]
        lista_items_sin_espacios = ''.join(temp)
        items_en_lista = re.findall("...?", lista_items_sin_espacios)
        i = 0
        for item in items_en_lista:
            if item[1] != " ":
                stacks[i].append(item[1])
            i += 1

    stacks_parte2 = []
    for stack in stacks:
        stacks_parte2.append(stack.copy())

    for linea in entrada[1].split("\n"):
        partes = linea.split("move ")[1].split(" from ")
        cantidad_movimientos = int(partes[0])
        desde = int(partes[1].split(" to ")[0])
        a_donde = int(partes[1].split(" to ")[1])

        for i in range(cantidad_movimientos):
            item = stacks[desde - 1][-1]
            del stacks[desde - 1][-1]
            stacks[a_donde - 1].append(item)

        items = stacks_parte2[desde - 1][len(stacks_parte2[desde - 1]) - cantidad_movimientos:]
        del stacks_parte2[desde - 1][len(stacks_parte2[desde - 1]) - cantidad_movimientos:]
        stacks_parte2[a_donde - 1] += items
    
    respuesta1 = ""
    for stack in stacks:
        respuesta1 += f"{stack[-1]}"

    respuesta2 = ""
    for stack in stacks_parte2:
        respuesta2 += f"{stack[-1]}"

    print(f"Respuesta 1: {respuesta1}")
    print(f"Respuesta 2: {respuesta2}")
            

if __name__ == "__main__":
    main()