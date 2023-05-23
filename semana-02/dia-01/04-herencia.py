class Persona:
    def __init__(self, nom, ema):
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print('NOMBRE: ' + self.nombre)
        print('EMAIL: ' + self.email)

class Alumno(Persona):
    nota = 0
    def mostrar_alumno(self):
        print('NOMBRE: ' + self.nombre)
        print('EMAIL: ' + self.email)
        print('NOTA: ' + str(self.nota))
        

class Profesor(Persona):
    especialidad = ''
    def mostrar_profesor(self):
        print('NOMBRE: ' + self.nombre)
        print('EMAIL: ' + self.email)
        print('ESPECIALIDAD: ' + self.especialidad)
        
alumno1 = Alumno('Juan Perez','cperez@gmail.com')
alumno1.nota = 20
alumno1.mostrar_alumno()

prof = Profesor('Jorge Garnica','jorgegarnica@gmail.com')
prof.especialidad = 'Frontend'
prof.mostrar_profesor()

