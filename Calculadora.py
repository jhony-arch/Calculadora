print("--- Calculadora Prime ---")  
print("Jonathan - Juan Carlos - Bryan")



# Esto suma los dos numeros del usuario
def suma(x, y):
    return x + y

def resta(x, y):         
    return x - y           #devuelve la resta de x - y

def multi(x, y):
    return x * y           #devuelve la multiplicacion

def divi(x, y):
    return x / y           #devuelve la division normal

def DIVI(x, y):
    return x // y          #devuelve la division entera (sin decimales)

def resi(x, y):
    return x % y           #devuelve el residuo (lo que sobra)




def construir(argumento):
    a = 0
    for s in range(len(argumento)):
        if argumento[s] == " ":          #cuenta cuantos espacios hay en la operación
            a +=1
    if a % 2 == 0:
        v1 = argumento.find(" ")
        v2 = argumento.find(" ", v1 + 1)       #encuentra posiciones de los espacios 
        valor1 = argumento[:v1]
        valor2 = argumento[v1+1:v2]            #separa los valores
        valor3 = argumento[v2+1:]

        valor1 = float(valor1)
        valor2 = float(valor2)            #convierte los numeros a enteros 

        try:
            if valor3 == "+":
                resultado = suma(valor1, valor2)
            elif valor3 == "-":
                resultado = resta(valor1, valor2)
            elif valor3 == "*":
                resultado = multi(valor1, valor2)
            elif valor3 == "/":
                resultado = divi(valor1, valor2)         #dependiendo del operador hace la operacion
            elif valor3 == "DIV":
                resultado = DIVI(valor1, valor2)
            elif valor3 == "%":
                resultado = resi(valor1, valor2)

            argumento = resultado      #guarda el resultado 
            
            return argumento       #devuelve el resultado
        
        except:
            print("Error 4")
            return False     # Si ocurre cualquier error (ej: división por 0)
    


    else: 
        print("Error 3") 
        return False       # Si el formato está mal escrito


def verificar(calculo):
    marca = 1
    marca2 = 1
    n = 0
    probar = True
    lpDerecho = []
    posDerecho = []
    lpIzquierdo = []
    posIzquierdo = []

    for x in range(len(calculo)):    #recorre todo el calculo 

        if calculo[x] == "(":                           # Guarda paréntesis izquierdos "("
            lpIzquierdo.append(calculo[x] + str(marca))
            marca +=1
            posIzquierdo.append(x)

        if calculo[x] == ")":                    # Guarda paréntesis derechos ")"
            lpDerecho.append(calculo[x] + str(marca2))
            marca2 +=1
            posDerecho.append(x)

    if len(lpIzquierdo) == len(lpDerecho):            # Verifica que haya la misma cantidad de paréntesis
        for x in range(len(lpIzquierdo)):          # Verifica que estén bien ordenados
            for k in posDerecho:
                if posIzquierdo[x] > k:
                    probar = False
                    print("Error 2")
                    break
        
            
        if probar:
            valor = calculo
            while "(" in calculo:             # Mientras haya paréntesis

                inicio = calculo.rfind("(")       # Busca el último "("
                fin = calculo.find(")", inicio)      # Busca el ")" correspondiente

                arg = calculo[inicio+1:fin]       # Extrae lo que está dentro del paréntesis

                valor = str(construir(arg))       # Resuelve esa parte
                calculo = calculo[:inicio] + valor + calculo[fin+1:]   # Reemplaza el paréntesis con el resultado
                n +=1
            print(valor)          # Muestra resultado final
    else:
        print("Error 1")    # Paréntesis desiguales
        probar = False


    return probar
    

def inicio():
    while True:
        calculo = str(input("Ingrese calculo a operar: "))  # Pide al usuario una operación
        if verificar(calculo):              # Verifica y ejecuta
            print("Aqui aparecera el calculo")


inicio()
