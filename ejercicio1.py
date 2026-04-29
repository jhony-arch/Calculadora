import sys

archivo = sys.argv[1]
numero = int(sys.argv[2])

with open(archivo, "r") as file:
    for linea in file:
        cont = 1

        for sep in linea:
            if sep == " ":
                cont += 1
        if cont >= numero:
            print (linea)

