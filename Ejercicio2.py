
class Agenda:
	
	def __init__(self):
		self.contactos=[]


	def menu(self):
		print()
		menu = [
			['Agenda Personal'],
			['1. Añadir Contacto',"anadir"],
			['2. Lista de contactos'],
			['3. Buscar contacto'],
			['4. Editar contacto'],
			['5. Cerrar agenda']
		]

		for i in range(6):
			print(menu[i][0])

		opcion =int(input("Por favor digite una opcion: "))
		if opcion==1:
			self.anadir()
		elif opcion==2:
			self.lista()
		elif opcion==3:
			self.buscar()
		elif opcion==4:
			self.editar()
		elif opcion==5:
			print("----Agenda cerrada----")
			exit()

	
		self.menu()


	
	def anadir(self):
		
		print("\nAñadir nuevo contacto")
		nom=input("Digite el nombre: ")
		telf=int(input("Digite el teléfono: "))
		email=input("Digite el email: ")
		self.contactos.append({'nombre':nom,'telf':telf,'email':email})
		

	
	def lista(self):
		
		print("\nLista de contactos \n")
		
		if len(self.contactos) == 0:
			print("No existen contactos en la agenda")
		else:
			for i in range(len(self.contactos)):
				print(self.contactos[i]['nombre'])
		

	
	def buscar(self):
		print("\nBuscar contactos")
		nom=input("Digite el nombre del contacto: ")
		for i in range(len(self.contactos)):
			if nom == self.contactos[i]['nombre']:
				print("Información del contacto")
				print("Nombre: ",self.contactos[i]['nombre'])
				print("Teléfono: ",self.contactos[i]['telf'])
				print("E-mail: ",self.contactos[i]['email'])
				return i
		
	
	def editar(self):
		print("\nEditar contacto \n")		
		data=self.buscar()
		condition=False
		while condition==False:
			print("Seleccione una opción: ")
			print("1. Nombre")
			print("2. Teléfono")
			print("3. E-mail")
			print("4. Volver")
			option=int(input("Digite una opción: "))
			if option==1:
				nom=input("Digite el nuevo nombre: ")
				self.contactos[data]['nombre']=nom
			elif option==2:
				telf=input("Digite el nuevo teléfono: ")
				self.contactos[data]['telf']=telf
			elif option==3:
				email=input("Digite el nuevo email: ")
				self.contactos[data]['email']=email
			elif option==4:
				condition=True


def main():
    agenda=Agenda()
    agenda.menu()
    
if __name__ == "__main__":
    main()
