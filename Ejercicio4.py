
class Cuenta:

	def __init__(self,titular,cantidad):
		self.titular = titular
		self.cantidad = cantidad


	def imprimir(self):
		print("Titular: ",self.titular)
		print("Cantidad: ", self.cantidad)



class CajaAhorro(Cuenta):
	
	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)

	
	def imprimir(self):
		print("Cuenta de caja de ahorros")
		super().imprimir()



class PlazoFijo(Cuenta):
	
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo = plazo
		self.interes = interes



	def importeInteres(self):
		importe=self.cantidad*self.interes/100
		print("El importe de interés es: ",importe)



	def imprimir(self):
		print("Cuenta a plazo fijo")
		super().imprimir()
		print("Plazo para pagar en meses es: ",self.plazo)
		print("Interés: ",self.interes)
		self.importeInteres()



def main():
    caja1 = CajaAhorro("Luis Migel pacheco",10000000)
    caja1.imprimir()
    plazo1 = PlazoFijo("Isabel",800000,8,0.2)
    plazo1.imprimir()
    
if __name__ == "__main__":
    main()

