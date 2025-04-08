#Se piden el valor de las variables
nume1 = int(input("1: "))
nume2 = int(input("2: "))

#se definen las operaciones
def suma(num1,num2):
    sumat = num1 + num2
    print(f"la suma es {sumat}")

def resta(num1,num2):
    resta = num1 - num2
    print(f"la resta es {resta}")

def multiplicacion(num1,num2):
    mult = num1 * num2
    print(f"la multiplicacion es {mult}")

def division(num1,num2):
    divi = num1 / num2
    print(f"la division es {divi}")

#se realiza la operacion y muestra el resultado
if __name__ == "__main__":
    suma(nume1, nume2)
    resta(nume1, nume2)
    multiplicacion(nume1, nume2)
    division(nume1, nume2)
