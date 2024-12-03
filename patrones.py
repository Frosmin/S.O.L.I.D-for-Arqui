from abc import ABC, abstractmethod


class Pedido:
    def __init__(self):
        self.items = []

    def agregar_item(self, nombre, precio, cantidad):
        self.items.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        
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
   
   
######################################################################################################################
 
        
        
 #Strategy       
        
class EstrategiaCalculo(ABC):
    @abstractmethod
    def calcular(self, pedido):
        pass

class CalculoNormal(EstrategiaCalculo):
    def calcular(self, pedido):
        return sum(item["precio"] * item["cantidad"] for item in pedido.items)

class CalculoConDescuento(EstrategiaCalculo):
    def __init__(self, descuento):
        self.descuento = descuento

    def calcular(self, pedido):
        total = sum(item["precio"] * item["cantidad"] for item in pedido.items)
        return total * (1 - self.descuento)        
        
        
class CalculadorCosto:
    def __init__(self, estrategia: EstrategiaCalculo):
        self.estrategia = estrategia

    def calcular_total(self, pedido):
        return self.estrategia.calcular(pedido)






    
######################################################################################################################
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
      
  #Factory Method 
  #proporciona una interfaz para crear objetos     
class ProcesadorPagoFactory:
    @staticmethod
    def crear_procesador(tipo):
        if tipo == "tarjeta":
            return PagoTarjeta()
        elif tipo == "efectivo":
            return PagoEfectivo()
        elif tipo == "paypal":
            return PagoPayPal()
        else:
            raise ValueError("Tipo de procesador de pago no soportado.")


###################################################################################################################

#Adapter


# sistema externo
class PagoCripomonedas:
    def procesar(self, cantidad):
        print(f"Procesando ${cantidad} con cripto.")

# Adaptador
class CriptoAdapter(ProcesadorPago):
    def __init__(self, cripto_pago):
        self.cripto_pago = cripto_pago

    def procesar_pago(self, monto):
        self.cripto_pago.procesar(monto)




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
    
    #Strategy   
    descuento = CalculoConDescuento(0.1)
    calculador_costo = CalculadorCosto(descuento)
    #calculador_costo = CalculadorCosto(CalculoNormal()) #sin descuento
    
    #Factory Method 
    procesador_pago = ProcesadorPagoFactory.crear_procesador("paypal")
    sistema = SistemaRestaurante(procesador_pago)
    
    #Adapter
    # cripto_pago = CriptoAdapter(PagoCripomonedas())
    # sistema = SistemaRestaurante(cripto_pago)
    
    
    
    generador_recibo = GeneradorReciboTexto()
    pedido1 = Pedido()
    pedido1.agregar_item("pollo", 20, 2)
    pedido1.agregar_item("jugo", 6, 1)
    
    
    
    sistema.realizar_pedido(pedido1, generador_recibo, calculador_costo)
   