def pedir():
    n = int(input("Ingrese numero de notas: "))
    list = []
    for x in range(n):
        nota = float(input("Ingrese la nota: "))
        list.append(nota)
    return list

def prom(lista):
    sum = 0
    for x in lista:
        sum += x
    xProm = sum/len(lista)
    return xProm

def categoria(Yprom):
    if Yprom > 90:
        return "A"
    elif Yprom >= 80:
        return "B"
    elif Yprom >= 70:
        return "C"
    elif Yprom >= 61:
        return "D"
    else :
        return "F"
    
def main():
    notas = pedir()
    promedio = prom(notas)
    grado = categoria(promedio)
    print("Lista de notas: ", notas)
    print("Promedio: ", promedio)
    print("Grado: ", grado)
    
main()