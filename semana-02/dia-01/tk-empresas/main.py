from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
cursor.execute('''
               create table if not exists empresas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ruc TEXT(20),
                    rsocial TEXT
                );
               ''')

class Empresa:
    def __init__(self,window):
        self.wind = window
        self.wind.title('CRUD EMPRESAS')
        self.wind.geometry("630x390")
        self.wind.configure(bg='#49A')
        
        # Creando el Frame Container
        frame = LabelFrame(self.wind, text = 'Registra de Nueva Empresa')    
        frame.grid(row=0, column=0, columnspan=3, pady=20, padx=20)
        
        #ruc
        lb_ruc = Label(frame, text = 'RUC : ')
        lb_ruc.grid(row = 1, column = 0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row = 1, column = 1)
        self.txt_ruc.focus()
        
        
        #razon social
        lb_rsocial = Label(frame, text = 'Razón Social : ')
        lb_rsocial.grid(row = 2, column = 0)
        self.txt_rsocial = Entry(frame)
        self.txt_rsocial.grid(row = 2, column = 1)
        
        #ciudad
        lb_ciudad = Label(frame, text = 'Ciudad : ')
        lb_ciudad.grid(row = 3, column = 0)
        self.txt_ciudad = Entry(frame)
        self.txt_ciudad.grid(row = 3, column = 1)
        
        #boton insertar nueva empresa
        btn_insertar = Button(frame, text = 'Insertar Empresa', command = self.insertar_empresa)
        btn_insertar.grid(row = 4, column=1)
        
        #treeview
        self.trv_empresas = Treeview(height=10)
        self.trv_empresas['columns'] = ['ruc','rsocial','ciudad']
        self.trv_empresas.column('#0',width=0,stretch=NO)
        self.trv_empresas.column('ruc')
        self.trv_empresas.column('rsocial')
        self.trv_empresas.column('ciudad')
        self.trv_empresas.heading('ruc',text='RUC',anchor=CENTER)
        self.trv_empresas.heading('rsocial',text='Razón Social',anchor=CENTER)
        self.trv_empresas.heading('ciudad',text='Ciudad',anchor=CENTER)
        self.trv_empresas.grid(row=2,column=0,padx=10)
        self.mostrar_empresas()
        
    def insertar_empresa(self):
        ruc = self.txt_ruc.get()
        rsocial = self.txt_rsocial.get()
        ciudad = self.txt_ciudad.get()
        cursor.execute('''
                       insert into empresas(ruc,rsocial,ciudad) values(?,?,?)
                       ''',(ruc,rsocial,ciudad))
        conn.commit()
        messagebox.showinfo("Mensaje", "Empresa Registrada Correctamente!!!")
        self.txt_ruc.delete(0,END)
        self.txt_rsocial.delete(0,END)
        self.txt_ciudad.delete(0,END)
        self.txt_ruc.focus()
        self.mostrar_empresas()
        
    def mostrar_empresas(self):
        lista_empresas = cursor.execute('''
                                        select * from empresas
                                        ''').fetchall()
        self.trv_empresas.delete(*self.trv_empresas.get_children())
        for empresa in lista_empresas:
            self.trv_empresas.insert('',END,text=empresa[0],values=(empresa[1],empresa[2],empresa[3]))
            
            
wind_empresa = Tk()
app = Empresa(wind_empresa)
wind_empresa.mainloop()