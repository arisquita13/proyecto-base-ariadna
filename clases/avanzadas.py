import math

class Operaciones:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.resultado = 0
        
    def leerNumeros(self):
        while True:
            try:
                self.num1 = int(input("Número 1: "))
                break
            except Exception:
                print("Número inválido")
                continue
        while True:
            try:
                self.num2 = int(input("Número 2: "))
                break
            except Exception:
                print("Número inválido")
                continue
    
    def leerUnNumero(self):
        while True:
            try:
                self.num1 = int(input("Ingrese el número: "))
                break
            except Exception:
                print("Número inválido")
                continue
    
    def sumar(self):
        self.resultado = "La suma de " + str(self.num1) + " + " + str(self.num2) + " es igual a " + str(self.num1 + self.num2)
    
    def restar(self):
        self.resultado = "La resta de " + str(self.num1) + " - " + str(self.num2) + " es igual a " + str(self.num1 - self.num2)
    
    def multiplicar(self):
        self.resultado = "La multiplicación de " + str(self.num1) + " * " + str(self.num2) + " es igual a " + str(self.num1 * self.num2)
    
    def dividir(self):
        if self.num2 == 0:
            self.resultado = "Error: No se puede dividir entre cero"
        else:
            self.resultado = "La división de " + str(self.num1) + " / " + str(self.num2) + " es igual a " + str(self.num1 / self.num2)
    
    def modulo(self):
        if self.num2 == 0:
            self.resultado = "Error: No se puede calcular el módulo con divisor cero"
        else:
            self.resultado = "El módulo de " + str(self.num1) + " % " + str(self.num2) + " es igual a " + str(self.num1 % self.num2)
    
    def potencia(self):
        self.resultado = "La potencia de " + str(self.num1) + " ^ " + str(self.num2) + " es igual a " + str(self.num1 ** self.num2)
    
    def raiz_cuadrada(self):
        if self.num1 < 0:
            self.resultado = "Error: No se puede calcular la raíz cuadrada de un número negativo"
        else:
            self.resultado = "La raíz cuadrada de " + str(self.num1) + " es igual a " + str(math.sqrt(self.num1))
    
    def mostrarResultado(self):
        print(self.resultado)


# Función principal para ejecutar la calculadora
def main():
    calculadora = Operaciones()
    
    while True:
        print("\n=== CALCULADORA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Módulo")
        print("6. Potencia")
        print("7. Raíz cuadrada")
        print("8. Salir")
        
        opcion = input("Seleccione una opción (1-8): ")
        
        if opcion == "8":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            calculadora.leerNumeros()
            
            if opcion == "1":
                calculadora.sumar()
            elif opcion == "2":
                calculadora.restar()
            elif opcion == "3":
                calculadora.multiplicar()
            elif opcion == "4":
                calculadora.dividir()
            elif opcion == "5":
                calculadora.modulo()
            elif opcion == "6":
                calculadora.potencia()
            
            calculadora.mostrarResultado()
        
        elif opcion == "7":
            calculadora.leerUnNumero()
            calculadora.raiz_cuadrada()
            calculadora.mostrarResultado()
        
        else:
            print("Opción inválida. Por favor, seleccione 1-8.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
