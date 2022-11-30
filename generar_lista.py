def main():
    with open('lista.txt', "w+") as lista_f:
        for i in range(1, 26):
            lista_f.write("Dia_%02d\n" % i)

if __name__ == "__main__":
    main()