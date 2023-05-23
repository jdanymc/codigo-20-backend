from tkinter import *
from tkinter import messagebox
#intancia de la clase Tk

app = Tk()
app.geometry("300x100")
app.title('Mi Primera App con Tk')

def saludar():
    print("Hola Mundo")
    nombre_saludo = txt_nombre.get()
    messagebox.showinfo("mensaje", "Hola " + nombre_saludo)

#agregamos un frame
frame = LabelFrame(app, text="Nueva Ventana")
frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

#agregamos una etiqueta
lb_nombre = Label(frame, text="Nombre : ")
lb_nombre.grid(row=1, column=0)

#agregamos una entrada de texto
txt_nombre = Entry(frame)
txt_nombre.grid(row=1, column=1)

#agrergamos un boton
btn_saludo = Button(frame, text="Saludar", command=saludar)
btn_saludo.grid(row=2, column=2)
app.mainloop()