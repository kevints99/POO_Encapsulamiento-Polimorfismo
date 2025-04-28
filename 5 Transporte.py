class Transporte:
    def tipo_transporte(self):
        print("Tipo de transporte desconocido.")

class Coche(Transporte):
    def tipo_transporte(self):
        print("Transporte terrestre.")

class Avion(Transporte):
    def tipo_transporte(self):
        print("Transporte aereo.")

class Barco(Transporte):
    def tipo_transporte(self):
        print("Transporte maritimo.")

# Validación:
if __name__ == "__main__":
    coche = Coche()
    avion = Avion()
    barco = Barco()

    coche.tipo_transporte()
    avion.tipo_transporte()
    barco.tipo_transporte()
