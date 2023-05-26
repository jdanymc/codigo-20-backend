from flask import Flask, render_template, request, redirect,url_for, flash,session
from . import admin # importa bluerprint
import pyrebase
from app.firebase_config import firebaseConfig

fb_app = pyrebase.initialize_app(firebaseConfig)
auth = fb_app.auth()

@admin.route('/')
def index():
    if('token' not in session):
        return redirect(url_for('admin.login'))
   
    return render_template('admin/index.html')

#vistas para login

@admin.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            usuario = auth.sign_in_with_email_and_password(email,password)
            data_usuario = auth.get_account_info(usuario['idToken'])
            print(data_usuario)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.index'))
            #return render_template('admin/index.html')
        except:
            print('Usuario no válido')
            flash('Usuario o password no válido')
            #return render_template('admin/login.html')
        
    return render_template('admin/login.html')

@admin.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('admin.index'))

@admin.route('/proyectos')
def proyectos():
    if('token' not in session):
        return redirect(url_for('admin.login'))
    return render_template('admin/proyectos.html')