class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña

mi_usuario = Usuario("David.devcamp", "murcielago")

print("tu nombre de usuario es:", mi_usuario.usuario)
print("Tu Contraseña es:", mi_usuario.contraseña)