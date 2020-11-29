
print("===CALCULADORA===")
def ingreso ():
    global a,b
    a = float(input("Ingrese el primer numero: \n"))
    b = float(input("Ingrese el segundo numero: \n"))
    
def suma ():
    print(f"El resultado es:{a + b}")
    input()

def resta ():
    print(f"El resultado es:{a - b} ")
    input()

def multiplicacion ():
    print(f"El resultado es:{a * b} ")
    input()

def division ():
    if (b == 0):
        print ("No se puede dividir en 0")
        input()
    else:
        print(f"El resultado es:{a / b} ")
        input() 
    

while (True):
    print ("1 Suma")
    print ("2 Resta")
    print ("3 Multiplicacion")
    print ("4 Division")
    opcion =int(input("Ingrese opcion:\n"))
    if (opcion==1):
        ingreso ()
        suma ()
        

    elif (opcion ==2):
        ingreso()
        resta()


    elif(opcion ==3):
        ingreso() 
        multiplicacion()

    elif (opcion ==4):
        ingreso() 
        division()
