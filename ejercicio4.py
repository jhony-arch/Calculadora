import sys

archivo = sys.argv[1]
numero = int(sys.argv[2])

with open(archivo, "r") as f:
    for n in f:
        if int(n) > numero:
            print(n.strip())