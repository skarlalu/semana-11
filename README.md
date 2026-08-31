Nombre: Karla Daniela Luque Navarrete
Descripción del Sistema
Aplicación desarrollada en Python para la gestión de productos y usuarios de un restaurante, aplicando principios de Programación Orientada a Objetos, manejo de excepciones y persistencia local en formato JSON mediante un servicio especializado.

Estructura del Proyecto
modelos/
__init__.py: Inicializador del paquete de modelos.
producto.py: Contiene la clase Producto con validaciones, encapsulamiento mediante propiedades y serialización a diccionario.
usuario.py: Contiene la clase Usuario para la gestión de clientes en memoria.
venta.py: Contiene la clase Venta para el registro de transacciones.

servicios/
__init__.py: Inicializador del paquete de servicios.
archivo_servicio.py: Maneja la lectura, escritura y control de errores específicos de los archivos JSON.
restaurante.py: Administra las colecciones en memoria y coordina el almacenamiento persistente con el servicio de archivos.

datos/
productos.json: Almacena persistentemente los productos del sistema.
usuarios.json: Almacena la información de los usuarios.
ventas.json: Almacena las ventas realizadas.

main.py: Punto de entrada del programa que gestiona la interacción por consola mediante un menú interactivo y bloques de control.
Instrucciones de Ejecución
Abra una terminal en el directorio principal del proyecto.
Ejecute el comando: python main.py

En el desarrollo de este proyecto se aplicaron tipos de datos básicos como str, int, float, bool y colecciones de tipo list para almacenar objetos de manera dinámica, evidenciando que una correcta modularización del software, la separación de responsabilidades entre capas y el uso de nombres descriptivos permiten estructurar aplicaciones robustas, escalables y fáciles de mantener.