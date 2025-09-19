class Avanzadas:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = None

    def leerNumeros(self):
        while True:
            try:
                self.num1 = float(input("Número base: "))
                break
            except Exception:
                print("Número inválido")
        while True:
            try:
                self.num2 = float(input("Exponente: "))
                break
            except Exception:
                print("Número inválido")

    def elevarPotencia(self):
        # num1 ^ num2
        self.resultado = self.num1 ** self.num2

    def mostrarResultado(self):
        print(f"Resultado: {self.resultado}")
