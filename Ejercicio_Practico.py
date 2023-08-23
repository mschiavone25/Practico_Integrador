#Ejercicio 6

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
    
    def get_edad(self):
        return self.edad
    
    def set_dni(self, dni):
        self.dni = dni
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejercicio 7

class Cuenta:
    def __init__(self, titular=None, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad
    
    def set_titular(self, titular):
        self.titular = titular
    
    def get_titular(self):
        return self.titular
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar(self):
        print("Titular:", self.titular.get_nombre())
        print("Cantidad:", self.cantidad)
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

#Ejercicio 8

class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificación:", self.bonificacion)


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

def contador(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def palabra_mas_repetida(frecuencia):
    max_palabra = None
    max_frecuencia = 0
    for palabra, freq in frecuencia.items():
        if freq > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = freq
    return (max_palabra, max_frecuencia)

#Ejercicio 4

#Igual al 3

#Ejercicio 5

def get_int():
    try:
        return int(input("Ingrese un número entero para verificar: "))
    except ValueError:
        print("Error: No es un número válido.")
        return get_int()
    





# Ejercicio 1
 
if __name__ == "__main__":
    a = int (input("Ingrese el primer numero entero_MCD:"))
    b = int (input("Ingrese el segundo numero entero_MCD:"))

    print("Máximo común divisor es:", MCD(a, b))

# Ejercicio 2

    c = int (input("Ingrese el primer numero entero_MCM:"))
    d = int (input("Ingrese el segundo numero entero_MCM:"))

    print("Mínimo común múltiplo entre es:", MCM(c, d))

#Ejercicio 3

cadena = input("Ingrese una cadena de caracteres: ")
frecuencia_palabras = contador(cadena)
print("Frecuencia de palabras:", frecuencia_palabras)
    
palabra, frecuencia = palabra_mas_repetida(frecuencia_palabras)
print("Palabra más repetida:", palabra)
print("Frecuencia:", frecuencia)

#Ejercicio 6

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
dni = input("Ingrese el DNI: ")
persona = Persona(nombre, edad, dni)
persona.mostrar()
if persona.es_mayor_de_edad():
        print("Es mayor de edad.")
else:
        print("No es mayor de edad.")

#Ejercicio 7

cantidad = float(input("Ingrese la cantidad inicial de la cuenta: "))
cuenta = Cuenta(persona, cantidad)
cuenta.mostrar()
cantidad_ingresar = float(input("Ingrese la cantidad a ingresar: "))
cuenta.ingresar(cantidad_ingresar)
cuenta.mostrar()
cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
cuenta.retirar(cantidad_retirar)
cuenta.mostrar()

#Ejercicio 8

bonificacion = float(input("Ingrese la bonificación de la cuenta joven: "))
cuenta_joven = CuentaJoven(persona, cantidad, bonificacion)
cuenta_joven.mostrar()
