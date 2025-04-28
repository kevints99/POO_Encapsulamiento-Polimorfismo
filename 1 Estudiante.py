class Estudiante:
    def __init__(self, nombre, codigo):
        self._nombre = None
        self._codigo = None
        self._notas = []
        self.nombre = nombre
        self.codigo = codigo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor.isalnum():
            raise ValueError("El código debe ser alfanumérico.")
        self._codigo = valor

    def agregar_nota(self, nota):
        if 0.0 <= nota <= 5.0:
            self._notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self):
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)

    def es_aprobado(self):
        return self.calcular_promedio() >= 3.0

# Validación:
if __name__ == "__main__":
    est = Estudiante("Kevin", "A123")
    est.agregar_nota(4.5)
    est.agregar_nota(3.8)
    print("Promedio:", est.calcular_promedio())  # Debería dar ~4.15
    print("Aprobado?", est.es_aprobado())       # True
