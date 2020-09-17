
class Estudiante:
	
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    
    def imprimir(self):        
    	print("\nNombre: ",self.nombre)
    	print("Nota: ",self.nota)
 
    def resultado(self):
    	if self.nota < 3:
    		print("El estudiante ha reprobado la materia \n")
    	else:
    		print("El estudiante ha aprobado la materia \n")

def main():
    estudiante1 = Estudiante()
    estudiante1.inicializar("Luisa Fernandez",3.0)
    estudiante1.imprimir()
    estudiante1.resultado()
    
    estudiante2 = Estudiante()
    estudiante2.inicializar("Luis Pacheco",2.9)
    estudiante2.imprimir()
    estudiante2.resultado()
    
    estudiante3 = Estudiante()
    estudiante3.inicializar("Maria Diaz",4.4)
    estudiante3.imprimir()
    estudiante3.resultado()

if __name__ == "__main__":
    main()