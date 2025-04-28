class Empleado:
    def __init__(self, nombre, rol, clave_acceso):
        self.__nombre = nombre
        self.__rol = rol
        self.__clave_acceso = self.__cifrar_clave(clave_acceso)

    # Método privado para cifrar (revertir la clave)
    def __cifrar_clave(self, clave):
        return clave[::-1]

    @property
    def nombre(self):
        return self.__nombre

    @property
    def rol(self):
        return self.__rol

    def verificar_clave(self, clave_ingresada):
        return self.__cifrar_clave(clave_ingresada) == self.__clave_acceso

    def cambiar_clave(self, clave_antigua, nueva_clave):
        if self.verificar_clave(clave_antigua):
            self.__clave_acceso = self.__cifrar_clave(nueva_clave)
            print("Clave actualizada exitosamente.")
        else:
            print("Clave antigua incorrecta. No se actualizó.")

#  Validacion
if __name__ == "__main__":
    emp = Empleado("Kevin", "Admin", "clave123")

    print(emp.nombre)  # Kevin
    print(emp.rol)     # Admin

    # Intentar verificar la clave correcta
    print(emp.verificar_clave("clave123"))  # True

    # Cambiar la clave con la correcta
    emp.cambiar_clave("clave123", "nuevaClave456")
    
    # Verificar con la nueva clave
    print(emp.verificar_clave("nuevaClave456"))  # True
