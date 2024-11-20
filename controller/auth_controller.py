from flask import render_template, request, redirect, url_for, flash, session
from models.usuario import Usuario

# Lista de usuarios de ejemplo (en la práctica, estos vendrían de una base de datos)
usuarios = {
    'admin': Usuario(1, 'admin', 'admin123', 'admin'),
    'user1': Usuario(2, 'user1', 'usuario123', 'usuario'),
    'guest': Usuario(3, 'guest', 'guest123', 'guest')
}

class AuthController:
    def login(self):
        """Maneja el login del usuario"""
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            usuario = usuarios.get(username)
            
            # Verificar si el usuario existe y si la contraseña es correcta
            if usuario and usuario.check_password(password):
                session['usuario_id'] = usuario.id
                session['username'] = usuario.username
                session['rol'] = usuario.rol  # Guardamos el rol en la sesión
                flash(f"Bienvenido, {usuario.username}!", 'success')
                return redirect(url_for('saludo'))  # Redirigir a la página de saludo
            else:
                flash("Usuario o contraseña incorrectos", 'danger')
        
        return render_template('login.html')

    def saludo(self):
        """Muestra el saludo después del login exitoso"""
        if 'username' in session:
            username = session['username']
            return render_template('saludo.html', username=username)
        else:
            flash("Por favor, inicia sesión primero.", 'danger')
            return redirect(url_for('login'))


    def verificar_permiso(self, rol_requerido):
        """Verifica si el usuario tiene el permiso necesario para acceder a una ruta"""
        if 'rol' not in session or session['rol'] != rol_requerido:
            flash('No tienes permiso para acceder a esta página', 'danger')
            return redirect(url_for('login'))
        return True
