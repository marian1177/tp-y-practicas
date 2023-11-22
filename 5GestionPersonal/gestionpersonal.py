class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni

    @property
    def obtener_dni(self):
        return self._dni

    def datos_basicos(self):
        return f"los datos basicos del empleado son: {self.nombre}, {self.edad}, {self._dni}"


class Empleado(Persona):

    salario = [300000, 600000, 900000]

    def __init__(self, nombre, edad, dni, cargo):
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


class Departamento:
    def __init__(self, ingreso):
        self.ingreso = ingreso
        self._empleados = []

    @property
    def listar_empleados(self):

        if self._empleados == []:
            return []
        else:
            return self._empleados

    def agregar_empleado(self, ingreso):
        self._empleados.append(ingreso)

    def eliminar_empleado(self, ingreso):
        self._empleados.remove(ingreso)


class Gerente(Empleado):

    departamento = Departamento("Gerente")

    def __init__(self, nombre, edad, dni, cargo, cant_subordinados):
        super().__init__(nombre, edad, dni, cargo)
        self.cant_subordinados = cant_subordinados


mariano = Gerente("mariano", 35, 34094027, "B", 2)
print(mariano.datos_basicos())
print(mariano.calcular_salario())
departamento_mariano = mariano.departamento
departamento_mariano.agregar_empleado(mariano)
empleados = mariano.departamento.listar_empleados
for empleado in empleados:
    print(
        f"Nombre: {empleado.nombre}, Cargo: {empleado.cargo}, Subordinados: {empleado.cant_subordinados}")
departamento_mariano.eliminar_empleado(mariano)
empleados = mariano.departamento.listar_empleados
