print("--- Calculadora Prime ---")
print("Jonathan - Juan Carlos - Bryan")

probar = True
lpDerecho = []
posDerecho = []
lpIzquierdo = []
posIzquierdo = []
# Esto suma los dos numeros del usuario
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multi(x, y):
    return x * y



def construir(argumento):
    a = 0
    for s in range(len(argumento)):
        if argumento[s] == " ":
            a +=1
    if a % 2 == 0:
        v1 = argumento.find(" ")
        v2 = argumento.find(" ", v1 + 1)
        valor1 = argumento[:v1]
        valor2 = argumento[v1+1:v2]
        valor3 = argumento[v2+1:]

        valor1 = int(valor1)
        valor2 = int(valor2)

        if valor3 == "+":
            resultado = suma(valor1, valor2)
        elif valor3 == "-":
            resultado = resta(valor1, valor2)
        elif valor3 == "*":
            resultado = multi(valor1, valor2)
        elif valor3 == "/":
            resultado = resta(valor1, valor2)
        elif valor3 == "DIV":
            resultado = resta(valor1, valor2)
        elif valor3 == "%":
            resultado = resta(valor1, valor2)
        elif valor3 == "sqr":
            resultado = resta(valor1, valor2)

        argumento = resultado
        return argumento
    


    else: 
        print("Error 3")


def verificar(calculo):
    marca = 1
    marca2 = 1
    n = 0

    for x in range(len(calculo)):

        if calculo[x] == "(":
            lpIzquierdo.append(calculo[x] + str(marca))
            marca +=1
            posIzquierdo.append(x)

        if calculo[x] == ")":
            lpDerecho.append(calculo[x] + str(marca2))
            marca2 +=1
            posDerecho.append(x)

    if len(lpIzquierdo) == len(lpDerecho):
        for x in range(len(lpIzquierdo)):
            for k in posDerecho:
                if posIzquierdo[x] > k:
                    probar = False
                    print("Error 2")
                    break
        
            
        if probar:
            
            while "(" in calculo:

                inicio = calculo.rfind("(")
                fin = calculo.find(")", inicio)

                arg = calculo[inicio+1:fin]
                print(arg)

                valor = str(construir(arg))
                calculo = calculo[:inicio] + valor + calculo[fin+1:]
                print(calculo)

                n +=1
    else:
        print("Error 1")
        probar = False


    return probar
    

def inicio():
    while True:
        calculo = str(input("Ingrese calculo a operar: "))
        if verificar(calculo):
            print("Aqui aparecera el calculo")


            




