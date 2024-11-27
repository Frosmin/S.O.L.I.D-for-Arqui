# Interfaces
from abc import ABC, abstractmethod

class INotificador(ABC):
    @abstractmethod
    def notificar(self, mensaje):
        pass

class IPrestable(ABC):
    @abstractmethod
    def prestar(self):
        pass
    
    @abstractmethod
    def devolver(self):
        pass

# Clases base
class Libro:
    def __init__(self, titulo, autor, id):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponible = True

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

class LibroDigital(Libro, IPrestable):
    def __init__(self, titulo, autor, id, formato):
        super().__init__(titulo, autor, id)
        self.formato = formato

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.libros_prestados = []

    def get_nombre(self):
        return self.nombre

    def agregar_libro_prestado(self, libro):
        self.libros_prestados.append(libro)

    def remover_libro_prestado(self, libro):
        self.libros_prestados.remove(libro)

class NotificacionEmail(INotificador):
    def notificar(self, mensaje):
        # Simulación de envío de email
        print(f"Enviando email: {mensaje}")

class NotificacionSMS(INotificador):
    def notificar(self, mensaje):
        # Simulación de envío de SMS
        print(f"Enviando SMS: {mensaje}")

class ServicioPrestamo:
    def __init__(self, notificador: INotificador):
        self.notificador = notificador

    def realizar_prestamo(self, libro: Libro, usuario: Usuario):
        if libro.prestar():
            usuario.agregar_libro_prestado(libro)
            self.notificador.notificar(f"Libro {libro.get_titulo()} prestado a {usuario.get_nombre()}")
            return True
        return False

    def realizar_devolucion(self, libro: Libro, usuario: Usuario):
        libro.devolver()
        usuario.remover_libro_prestado(libro)
        self.notificador.notificar(f"Libro {libro.get_titulo()} devuelto por {usuario.get_nombre()}")

# Ejemplo de uso
def main():
    # Crear instancias
    libro = LibroDigital("Python Programming", "John Doe", "123-456", "PDF")
    usuario = Usuario("Ana García", "ana@email.com")
    notificador = NotificacionEmail()
    servicio = ServicioPrestamo(notificador)

    # Realizar préstamo
    servicio.realizar_prestamo(libro, usuario)
    
    # Realizar devolución
    servicio.realizar_devolucion(libro, usuario)

if __name__ == "__main__":
    main()