# models/usuario.py

class Usuario:
    def __init__(self, id: int, username: str, password: str, rol: str):
        self.id = id
        self.username = username
        self.password = password
        self.rol = rol  # Ahora el rol es parte de cada usuario (admin, usuario, etc.)

    def __repr__(self):
        return f"Usuario(id={self.id}, username='{self.username}', rol='{self.rol}')"

    def check_password(self, password: str) -> bool:
        """Verifica si la contraseña ingresada es correcta"""
        return self.password == password

    def tiene_permiso(self, rol_requerido: str) -> bool:
        """Verifica si el usuario tiene el rol requerido"""
        return self.rol == rol_requerido
