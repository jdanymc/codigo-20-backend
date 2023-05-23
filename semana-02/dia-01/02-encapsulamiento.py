class Usuario:
    email = "mail@mail.com"
    password = "codigo2023"
    def login(self, email,password):
        if(self.email == email and self.password == password):
            print('Bienvenido '+ self.email)
        else:
            print('Datos incorrectos')

usuario1 = Usuario()

email = input('Ingrese email: ')
password = input('Ingrese password: ')
print('*'*20)
usuario1.login(email,password)
print('*'*20)
