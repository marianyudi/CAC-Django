#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
#• Un constructor, donde los datos pueden estar vacíos.
#• Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#• mostrar(): Muestra los datos de la persona.
#• es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:

    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str):
            self.nombre = nuevo_nombre
        else:
            raise TypeError("El nombre debe ser un str") 

    def get_nombre(self):
        return self.nombre

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int):
            self.edad = nueva_edad
        else:
            raise TypeError("La edad debe ser un int") 

    def get_edad(self):
        return self.edad

    def set_dni(self, nuevo_dni):
        if isinstance(nuevo_dni, int):
            self.dni = nuevo_dni
        else:
            raise TypeError("El DNI debe ser un int") 

    def get_dni(self):
        return self.get_dni

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)

    def es_mayor_de_edad(self):
        return self.edad >= 18
    
#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: • Un constructor, donde los datos pueden estar vacíos. • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. • mostrar(): Muestra los datos de la cuenta. • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:

    def __init__(self,titular:Persona = None,cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular:Persona):
        self.titular = titular
        
    def get_titular(self):
        return self.titular

    def ingresar(self, dinero):
        if dinero >0:
            self.cantidad += dinero

    def retirar(self, dinero):
        self.cantidad -= dinero

    def mostrar(self):
        print("Titular: ", self.titular.get_nombre)
        print("Cantidad: ", self.cantidad)

# Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase: • Un constructor. • Los setters y getters para el nuevo atributo. • En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. • Además, la retirada de dinero sólo se podrá hacer si el titular es válido. • El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
 
        