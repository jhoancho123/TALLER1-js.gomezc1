# app.py

from flask import Flask, render_template, redirect, url_for, session, flash
from controller.auth_controller import AuthController

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # Necesario para las sesiones y mensajes flash

# Instanciamos el controlador
auth_controller = AuthController()

# Rutas
@app.route('/login', methods=['GET', 'POST'])
def login():
    return auth_controller.login()

@app.route('/saludo')
def saludo():
    if 'usuario_id' not in session:
        flash("Debes iniciar sesión para ver esta página", 'danger')
        return redirect(url_for('login'))
    
    return auth_controller.saludo()

@app.route('/admin')
def admin():
    """Ruta solo para administradores"""
    if not auth_controller.verificar_permiso('admin'):
        return redirect(url_for('login'))
    
    return render_template('admin.html')  # Página solo para administradores

@app.route('/logout')
def logout():
    session.clear()  # Limpiar sesión al cerrar sesión
    flash("Has cerrado sesión.", 'info')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
