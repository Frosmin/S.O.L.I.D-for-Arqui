from abc import ABC, abstractmethod

# Principio 1: Responsabilidad Única (SRP)
class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, precio, cantidad):
        self.items.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

class CalculadorCosto:
    def calcular_total(self, pedido):
        return sum(item["precio"] * item["cantidad"] 
                   for item in pedido.items)

# Principio 2: Abierto/Cerrado (OCP)
# 1. Crear interfaz/clase abstracta base
class IGeneradorRecibo(ABC):
    @abstractmethod
    def generar_recibo(self, pedido, total):
        pass

class GeneradorReciboTexto(IGeneradorRecibo):
    def generar_recibo(self, pedido, total):
        recibo = "Recibo:\n"
        for item in pedido.items:
            recibo = recibo + f'{item["cantidad"]}x {item["nombre"]} - ${item["precio"] * item["cantidad"]}\n'
        recibo = recibo + f"Total: ${total}\n"
        return recibo
    
class GeneradorReciboHTML(IGeneradorRecibo):
    def generar_recibo(self, pedido, total):
        recibo = "<h1>Recibo:</h1>"
        recibo = recibo + "<ul>"
        for item in pedido.items:
            recibo = recibo + f'<li>{item["cantidad"]}x {item["nombre"]} - ${item["precio"] * item["cantidad"]}</li>'
        recibo = recibo + f"</ul><p>Total: ${total}</p>"
        return recibo


# Principio 3: Sustitución de Liskov (LSP)

# Principio 4: Segregación de Interfaces (ISP)
# Las interfaces ya están divididas (ProcesadorPago no obliga a implementar otras funciones irrelevantes).
class ProcesadorPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoTarjeta(ProcesadorPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con tarjeta de crédito.")

class PagoEfectivo(ProcesadorPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} en efectivo.")

class PagoPayPal(ProcesadorPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} a través de PayPal.")


# Principio 5: Inversión de Dependencias (DIP)
class SistemaRestaurante:
    def __init__(self, procesador_pago: ProcesadorPago):
        self.procesador_pago = procesador_pago

    def realizar_pedido(self, pedido, generador_recibo, calculador_costo):
        total = calculador_costo.calcular_total(pedido)
        recibo = generador_recibo.generar_recibo(pedido, total)
        print(recibo)
        self.procesador_pago.procesar_pago(total)


# Ejemplo de uso
if __name__ == "__main__":
    calculador_costo = CalculadorCosto()
    generador_recibo = GeneradorReciboTexto()
    procesador_pago = PagoEfectivo()
    sistema = SistemaRestaurante(procesador_pago)

    
    pedido1 = Pedido()
    pedido1.agregar_item("pollo", 20, 2)
    pedido1.agregar_item("jugo", 6, 1)
    
    
    
    sistema.realizar_pedido(pedido1, generador_recibo, calculador_costo)
   