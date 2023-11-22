class Empleado:
    def __init__(self,nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def enrolamiento(self):
        return f"se registra al empleado de nombre: {self.nombre}"
    
    def calcular_salario(self):
        return "se calcula el salario segun cada empleado"


class Gerente(Empleado):
    def __init__(self,nombre, salario, departamento,cant_subordinados):
        super().__init__(nombre,salario,departamento)
        self.cant_subordinados = cant_subordinados
    
    def proyecto(self):
        return "gerente inicia proyecto"

    def calcular_salario(self):
        if self.salario < 600000:
            self.salario = Trabajador(self.salario)+400000
        return "el salario final del Gerente es {self.salario}"


class Trabajador(Empleado):
    def __init__(self,nombre,salario, departamento,gremio):
        super().__init__(nombre,salario,departamento)
        self.gremio = gremio

    def trabajo(self):
        return f"empleado {self.nombre} incia jornada laboral"

    def calcular_salario(self):
       
        if self.salario < 200000:
            self.salario = 200000
            return "se ajusto el salario porque estaba por debajo del minimo"
        elif self.salario > 600000:
            self.salario = 600000
            return "se ajusto el salario porque estaba excedido"
        else:
             return "el salario final del trabajador {self.salario} es correcto"
        
mariano=Trabajador("mariano",3000,"desarrollo","comercio")
print(mariano.enrolamiento())
print(mariano.trabajo())
print(Empleado.calcular_salario(mariano))
print(mariano.calcular_salario())
print(mariano.salario)