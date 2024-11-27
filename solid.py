class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def alquilar_libro(self, libro):
        pass

    def devolver_libro(self, libro):
        pass
    
class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario

    def get_libro(self):
        return self.libro

    def get_usuario(self):
        return self.usuario
    
class Notificaion:
    def __init__(self, usuario):
        self.usuario = usuario

    def notificar(self, mensaje):
        pass