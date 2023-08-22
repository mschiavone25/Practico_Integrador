# Ejercicio 1
def MCD (a,b):
    x=0
    while b!=0:
        x = b
        b = a % b
        a = x
        print(a)
        print(b)
    return a


# Ejercicio 2

def MCM (c,d):
    if c > d:
        mayor = c
    else:
        mayor = d
    while (mayor % c != 0) or (mayor % d !=0):
        mayor += 1
    return mayor

# Ejercicio 3



if __name__ == "__main__":
    a = int (input("Ingrese el primer numero entero_MCD:"))
    b = int (input("Ingrese el segundo numero entero_MCD:"))

    print("Máximo común divisor:", MCD(a, b))

    c = int (input("Ingrese el primer numero entero_MCM:"))
    d = int (input("Ingrese el segundo numero entero_MCM:"))

    print("Mínimo común múltiplo:", MCM(c, d))






    
