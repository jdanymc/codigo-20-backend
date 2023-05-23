class Persona:
    def __init__(self, nom, ema):
        self.nombre = nom
        self.email = ema
    
    def mostrar(self):
        print('NOMBRE: ' + self.nombre)
        print('EMAIL: ' + self.email)

class Alumno(Persona):
    def __init__(self, nom, ema, nota):
        super().__init__(nom, ema)
        self.nota = nota
    def mostrar(self):
        print('*'*20+' DATOS DEL ALUMNO '+'*'*20)
        super().mostrar()
        print('NOTA: ' + str(self.nota))

class Profesor(Persona):
    def __init__(self, nom, ema, esp):
        super().__init__(nom, ema)
        self.especialidad = esp
    def mostrar(self):
        print('*'*20+' DATOS DEL PROFESOR '+'*'*20)
        super().mostrar()
        print('ESPECIALIDAD: ' + self.especialidad)
    
alumno1 = Alumno('Juan Perez','cperez@gmail.com',20)
alumno1.mostrar()

prof1 = Profesor('Jorge Garnica','jorgegarnica@gmail.com','Frontend')
prof1.mostrar()
prof2 = Profesor('Jorge Garnica','jorgegarnica@gmail.com','Frontend')
prof2.mostrar()
