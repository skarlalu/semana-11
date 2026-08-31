from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n========================================")
    print("         SISTEMA DE RESTAURANTE         ")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar usuario")
    print("5. Listar usuarios")
    print("6. Realizar venta")
    print("7. Consultar ventas de un usuario")
    print("8. Salir")
    print("========================================")

def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            try:
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                categoria = input("Categoría: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))

                nuevo_prod = Producto(codigo, nombre, categoria, precio, stock)
                if restaurante.registrar_producto(nuevo_prod):
                    print("¡Producto registrado y guardado con éxito!")
                else:
                    print("Error: Ya existe un producto con ese código.")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "2":
            print("\n--- Lista de Productos ---")
            productos = restaurante.listar_productos()
            if not productos:
                print("No hay productos registrados.")
            else:
                for p in productos:
                    print(f"Código: {p.codigo} | Nombre: {p.nombre} | Cat: {p.categoria} | Precio: ${p.precio:.2f} | Stock: {p.stock}")

        elif opcion == "3":
            print("\n--- Buscar Producto ---")
            codigo = input("Ingrese el código del producto: ")
            p = restaurante.buscar_producto(codigo)
            if p:
                print(f"Encontrado -> Nombre: {p.nombre} | Categoría: {p.categoria} | Precio: ${p.precio:.2f} | Stock: {p.stock}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            print("\n--- Registrar Usuario ---")
            try:
                cedula = input("Identificación (Cédula/ID): ")
                nombre = input("Nombre completo: ")
                correo = input("Correo electrónico: ")

                nuevo_usu = Usuario(cedula, nombre, correo)
                if restaurante.registrar_usuario(nuevo_usu):
                    print("¡Usuario registrado y guardado con éxito!")
                else:
                    print("Error: Ya existe un usuario con esa identificación.")
            except ValueError as e:
                print(f"Error de validación: {e}")

        elif opcion == "5":
            print("\n--- Lista de Usuarios ---")
            usuarios = restaurante.listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for u in usuarios:
                    print(f"ID: {u.identificacion} | Nombre: {u.nombre} | Correo: {u.correo}")

        elif opcion == "6":
            print("\n--- Realizar Venta ---")
            cedula = input("Identificación del usuario comprador: ")
            codigo = input("Código del producto a vender: ")
            try:
                cantidad = int(input("Cantidad solicitada: "))
                exito = restaurante.vender_producto(codigo, cedula, cantidad)
                if exito:
                    print("¡Venta realizada con éxito! Stock actualizado y registrada en ventas.json.")
                else:
                    print("Error: Venta rechazada (Verifique que el usuario y producto existan, o que haya stock suficiente).")
            except ValueError:
                print("Error: Ingrese un número válido para la cantidad.")

        elif opcion == "7":
            print("\n--- Consultar Ventas por Usuario ---")
            cedula = input("Ingrese la identificación del usuario: ")
            ventas = restaurante.consultar_ventas_usuario(cedula)
            if not ventas:
                print("No se encontraron ventas para este usuario.")
            else:
                print(f"\nVentas realizadas por el usuario {cedula}:")
                for v in ventas:
                    prod = restaurante.buscar_producto(v.producto_codigo)
                    nombre_prod = prod.nombre if prod else "Producto desconocido"
                    print(f"- Producto: [{v.producto_codigo}] {nombre_prod} | Cantidad adquirida: {v.cantidad}")

        elif opcion == "8":
            print("\nSaliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()