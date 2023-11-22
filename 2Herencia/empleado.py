class Empleado:
    def __init__(self,nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def enrolamiento(self):
        return f"se registra al empleado de nombre: {self.nombre}"


class Gerente(Empleado):
    def __init__(self,nombre, salario, departamento,cant_subordinados):
        super().__init__(nombre,salario,departamento)
        self.cant_subordinados = cant_subordinados
    
    def proyecto(self):
        return "gerente inicia proyecto"


class Trabajador(Empleado):
    def __init__(self,nombre,salario, departamento,gremio):
        super().__init__(nombre,salario,departamento)
        self.gremio = gremio

    def trabajo(self):
        return f"empleado {self.nombre} incia jornada laboral"


mariano=Trabajador("mariano",340,"desarrollo","comercio")
print(mariano.enrolamiento())
print(mariano.trabajo())