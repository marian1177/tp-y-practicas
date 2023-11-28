class Persona:
    # se declaran los datos basicos de la persona
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni

    @property
    # como es dato sensible para evitar modificarlo se protege el dni
    def obtener_dni(self):
        return self._dni

    def datos_basicos(self):
        # metodo para mostrar los datos basicos de la persona
        return f"los datos basicos del empleado son: {self.nombre}, {self.edad}, {self._dni}"


# en categoria mas baja se crea la clase Empleado
class Empleado(Persona):

    # atributo de clase con rangos a utilizar segun el tipo de empleado
    salario = [300000, 600000, 900000]

    def __init__(self, nombre, edad, dni, cargo):
        # se heredan los datos basicos de la persona con el agregado del cargo
        super().__init__(nombre, edad, dni)

        self.cargo = cargo

    def calcular_salario(self):
        if self.cargo == "A":
            return self.salario[2]
        elif self.cargo == "B":
            return self.salario[1]
        elif self.cargo == "C":
            return self.salario[0]
        else:
            return "error en categoria"


class Departamento:  # clase para agregar en una lista los empleados que se carguen
    def __init__(self, ingreso):
        self.ingreso = ingreso
        self._empleados = []

    @property               # se protege la lista a modificaciones
    def listar_empleados(self):

        if self._empleados == []:
            return []  # si no hay empleados devuelve la lista vacia
        else:
            return self._empleados

    def agregar_empleado(self, ingreso):
        # metodos para ingresar el tipo de empleado
        self._empleados.append(ingreso)

    def eliminar_empleado(self, ingreso):
        self._empleados.remove(ingreso)


class Gerente(Empleado):  # la clase gerente heredando los datos basicos y sueldos

    # atributo de clase especifico siempre que se instancie un gerente
    departamento = Departamento("Gerente")

    def __init__(self, nombre, edad, dni, cargo, cant_subordinados):
        super().__init__(nombre, edad, dni, cargo)
        # se agrega un atributo extra de cantidudad de subordinados
        self.cant_subordinados = cant_subordinados


# instancia de pruebas
mariano = Gerente("mariano", 35, 34094027, "B", 2)
print(mariano.datos_basicos())
print(mariano.calcular_salario())
departamento_mariano = mariano.departamento
departamento_mariano.agregar_empleado(mariano)
empleados = mariano.departamento.listar_empleados
for empleado in empleados:  # se recorren los datos a visualizar
    print(
        f"Nombre: {empleado.nombre}, Cargo: {empleado.cargo}, Subordinados: {empleado.cant_subordinados}")
departamento_mariano.eliminar_empleado(mariano)
empleados = mariano.departamento.listar_empleados
