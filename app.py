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


def maximo_comun_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def minimo_comun_multiplo(a, b):
    return (a * b) // maximo_comun_divisor(a, b)

def contar_palabras(texto):
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

def get_int():
    try:
        return int(input("Ingrese un número entero: "))
    except ValueError:
        print("Error: No es un número válido.")
        return get_int()

# Ejemplo de uso
if __name__ == "__main__":
    a = get_int()
    b = get_int()

    print("Máximo común divisor:", maximo_comun_divisor(a, b))
    print("Mínimo común múltiplo:", minimo_comun_multiplo(a, b))

    cadena = input("Ingrese una cadena de caracteres: ")
    frecuencia_palabras = contar_palabras(cadena)
    print("Frecuencia de palabras:", frecuencia_palabras)
    
    palabra, frecuencia = palabra_mas_repetida(frecuencia_palabras)
    print("Palabra más repetida:", palabra)
    print("Frecuencia:", frecuencia)

    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    dni = input("Ingrese el DNI: ")
    persona = Persona(nombre, edad, dni)
    persona.mostrar()
    if persona.es_mayor_de_edad():
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")
    
    cantidad = float(input("Ingrese la cantidad inicial de la cuenta: "))
    cuenta = Cuenta(persona, cantidad)
    cuenta.mostrar()
    cantidad_ingresar = float(input("Ingrese la cantidad a ingresar: "))
    cuenta.ingresar(cantidad_ingresar)
    cuenta.mostrar()
    cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
    cuenta.retirar(cantidad_retirar)
    cuenta.mostrar()
    
    bonificacion = float(input("Ingrese la bonificación de la cuenta joven: "))
    cuenta_joven = CuentaJoven(persona, cantidad, bonificacion)
    cuenta_joven.mostrar()
