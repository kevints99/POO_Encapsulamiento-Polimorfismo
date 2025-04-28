class Persona:
    def __init__(self, nombre, edad, documento):
        self.__nombre = nombre
        self.__edad = edad
        self.__documento = documento

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

    @property
    def documento(self):
        return self.__documento

class Paciente(Persona):
    def __init__(self, nombre, edad, documento):
        super().__init__(nombre, edad, documento)
        self.__diagnostico = "Sin diagnostico"
        self.__historial = []

    def agregar_historial(self, entrada):
        self.__historial.append(entrada)

    def ver_historial(self):
        return self.__historial

    def ver_diagnostico(self):
        return self.__diagnostico

class Doctor(Persona):
    def __init__(self, nombre, edad, documento, especialidad):
        super().__init__(nombre, edad, documento)
        self.__especialidad = especialidad

    def ver_especialidad(self):
        return self.__especialidad

    def modificar_diagnostico(self, paciente, nuevo_diagnostico):
        if isinstance(paciente, Paciente):
            paciente._Paciente__diagnostico = nuevo_diagnostico
            print("Diagnostico actualizado")
        else:
            print("El paciente no es valido")

if __name__ == "__main__":
    paciente = Paciente("Ana", 30, "123456")
    paciente.agregar_historial("Consulta general")
    paciente.agregar_historial("Radiografia")
    print(paciente.ver_historial())
    print(paciente.ver_diagnostico())

    doctor = Doctor("Dr. Smith", 45, "D654321", "Cardiologia")
    print(doctor.ver_especialidad())
    doctor.modificar_diagnostico(paciente, "Fractura de pierna")
    print(paciente.ver_diagnostico())
