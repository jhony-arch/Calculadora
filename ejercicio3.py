def estudiantes():
    n_e = int(input("Ingrese numero de estudiantes: "))
    lista_e = []
    for x in range(n_e):
        estu = str(input("Ingrese estudiante: "))
        lista_e.append(estu)
    return lista_e

def notas(lista):
    lista_n = []
    for x in lista:
        nota = float(input("Ingrese la nota: "))
        lista_n.append(nota)
    return lista_n

def archivo(listaE, listaN):
    with open("resultados.txt", "w") as f:
        for x in range(len(listaE)):
            save = listaE[x] + " - " + str(listaN[x])
            f.write(save + "\n")

def main():
    estu = estudiantes()
    n = notas(estu)
    archivo(estu, n)

main()