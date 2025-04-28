class CarteraCripto:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__saldo_btc = 0.0

    def consultar_saldo(self):
        print(f"Saldo actual de BTC: {self.__saldo_btc}")

    def comprar_btc(self, monto_usd, precio_actual_btc):
        if monto_usd <= 0 or precio_actual_btc <= 0:
            print("Montos inválidos")
            return
        btc_comprados = monto_usd / precio_actual_btc
        self.__saldo_btc += btc_comprados
        print(f"Compraste {btc_comprados:.6f} BTC")

    def vender_btc(self, monto_btc, precio_actual_btc):
        if monto_btc > self.__saldo_btc:
            print("No puedes vender más BTC de los disponibles")
            return
        if monto_btc <= 0 or precio_actual_btc <= 0:
            print("Montos inválidos")
            return
        self.__saldo_btc -= monto_btc
        usd_recibidos = monto_btc * precio_actual_btc
        print(f"Vendiste {monto_btc:.6f} BTC por {usd_recibidos:.2f} USD")

if __name__ == "__main__":
    cartera = CarteraCripto("Kevin")
    cartera.consultar_saldo()
    cartera.comprar_btc(500, 25000)   # 0.02 BTC
    cartera.consultar_saldo()
    cartera.vender_btc(0.01, 25000)   # 0.01 BTC
    cartera.consultar_saldo()
