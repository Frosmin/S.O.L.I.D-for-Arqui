Explicación del Código y Principios SOLID
1. Single Responsibility Principle (SRP)
Pedido solo se encarga de almacenar los elementos del pedido.
CalculadorCosto es responsable de calcular el costo total de un pedido.
SistemaRestaurante administra el flujo principal del pedido, delegando tareas específicas a otras clases.
IGeneradorRecibo y sus implementaciones (GeneradorReciboTexto, GeneradorReciboHTML) se encargan únicamente de generar recibos en distintos formatos.
ProcesadorPago y sus implementaciones (PagoTarjeta, PagoEfectivo, PagoPayPal) manejan los pagos.
2. Open/Closed Principle (OCP)
IGeneradorRecibo permite agregar nuevos tipos de recibos (por ejemplo, recibos en PDF o Texto) sin modificar el código existente.
ProcesadorPago permite incorporar nuevos métodos de pago (como criptomonedas) mediante la implementación de la interfaz sin alterar las clases actuales.
3. Liskov Substitution Principle (LSP)
Las subclases (PagoTarjeta, PagoEfectivo, PagoPayPal) se comportan de manera intercambiable donde sea que se espere un ProcesadorPago. Esto asegura que el SistemaRestaurante pueda procesar cualquier tipo de pago sin cambiar su lógica interna.
4. Interface Segregation Principle (ISP)
La interfaz ProcesadorPago está diseñada para cumplir con una responsabilidad específica: procesar pagos. Esto evita obligar a las clases que implementan esta interfaz a cumplir con métodos irrelevantes. Por ejemplo, no se les exige manejar recibos o calcular costos.
5. Dependency Inversion Principle (DIP)
El SistemaRestaurante depende de abstracciones (ProcesadorPago y IGeneradorRecibo) en lugar de implementaciones concretas. Esto permite cambiar el generador de recibos o el método de pago sin modificar la lógica del sistema.