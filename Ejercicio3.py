
class Banco:
	
	def __init__(self):
		self.cliente1=Cliente("Yairinis Del Toro")
		self.cliente2=Cliente("Jois Contreras")
		self.cliente3=Cliente("Elis Mejia")
	
	def operacion(self):
		self.cliente1.depositar(500000), self.cliente2.depositar(250000), self.cliente3.depositar(100000), self.cliente1.extraer(50000)
	
	def depositos(self):
		total=self.cliente1.mostrar_total()+self.cliente2.mostrar_total()+self.cliente3.mostrar_total()
		print("El total de dinero depositado en el banco es de: ",total)
		self.cliente1.imprimir()
		self.cliente2.imprimir()
		self.cliente3.imprimir()

class Cliente:
	
	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0
	
	def depositar(self,cantidad):
		self.cantidad+=cantidad
	
	def extraer(self,cantidad):
		self.cantidad-=cantidad
	
	def mostrar_total(self):
		return self.cantidad
	
	def imprimir(self):
		print(self.nombre, " tiene depositado en el banco la cantidad de ",self.cantidad)

def main():
    banco1=Banco()
    banco1.operacion()
    banco1.depositos()
if __name__ == "__main__":
    main()
