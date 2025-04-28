class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base

    @property
    def nombre(self):
        return self.__nombre

    @property
    def sueldo_base(self):
        return self.__sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo
        else:
            raise ValueError("El sueldo base no puede ser negativo.")

    def calcular_salario(self):
        return self.__sueldo_base

class EmpleadoFijo(Empleado):
    def calcular_salario(self):
        return self.sueldo_base

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, sueldo_base, horas_trabajadas):
        super().__init__(nombre, sueldo_base)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.sueldo_base * self.horas_trabajadas

class EmpleadoTemporal(Empleado):
    def __init__(self, nombre, sueldo_base, dias_trabajados):
        super().__init__(nombre, sueldo_base)
        self.dias_trabajados = dias_trabajados

    def calcular_salario(self):
        return (self.sueldo_base / 30) * self.dias_trabajados

# Validación:
if __name__ == "__main__":
    empleados = [
        EmpleadoFijo("Kevin", 3000),
        EmpleadoPorHoras("Ana", 20, 160),     # 20 USD/hora * 160 horas
        EmpleadoTemporal("Luis", 3000, 15)    # 15 días trabajados
    ]

    for emp in empleados:
        print(f"{emp.nombre}: {emp.calcular_salario()} USD")
