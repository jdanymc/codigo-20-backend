class Alumno:
    def __init__(self,nom,ema,nota):
        self.nombre = nom
        self.email = ema
        self.nota = nota
    
    def mostrar(self):
        print('NOMBRE: ' + self.nombre)
        print('EMAIL: ' + self.email)
        print('NOTA: ' + str(self.nota))
        
class Profesor:
    def __init__(self,nom,ema,esp):
        self.nombre = nom
        self.email = ema
        self.especialidad = esp
    
    def mostrar(self):
        print('NOMBRE: ' + self.nombre)
        print('EMAIL: ' + self.email)
        print('ESPECIALIDAD: ' + str(self.especialidad))

    
alumno1 = Alumno('Juan Perez','cperez@gmail.com',20)
alumno1.mostrar()
profesor1 = Profesor('Cesar Mayra','cperez@gmail.com','Backend')
profesor1.mostrar()
