import json
import os
from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

class ArchivoServicio:
    CARPETA_DATOS = "datos"
    RUTA_PRODUCTOS = os.path.join(CARPETA_DATOS, "productos.json")
    RUTA_USUARIOS = os.path.join(CARPETA_DATOS, "usuarios.json")
    RUTA_VENTAS = os.path.join(CARPETA_DATOS, "ventas.json")

    @staticmethod
    def _asegurar_carpeta():
        if not os.path.exists(ArchivoServicio.CARPETA_DATOS):
            os.makedirs(ArchivoServicio.CARPETA_DATOS)

    # --- PRODUCTOS ---
    @staticmethod
    def cargar_productos() -> list[Producto]:
        ArchivoServicio._asegurar_carpeta()
        if not os.path.exists(ArchivoServicio.RUTA_PRODUCTOS):
            return []
        try:
            with open(ArchivoServicio.RUTA_PRODUCTOS, "r", encoding="utf-8") as f:
                contenido = f.read()
                if not contenido.strip():
                    return []
                data = json.loads(contenido)
                return [Producto.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error al leer productos.json (formato inválido o datos incompletos): {e}")
            return []
        except PermissionError:
            print("Error: Permiso denegado para leer el archivo de productos.")
            return []

    @staticmethod
    def guardar_productos(productos: list[Producto]):
        ArchivoServicio._asegurar_carpeta()
        try:
            data = [p.to_dict() for p in productos]
            with open(ArchivoServicio.RUTA_PRODUCTOS, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo de productos.")

    # --- USUARIOS ---
    @staticmethod
    def cargar_usuarios() -> list[Usuario]:
        ArchivoServicio._asegurar_carpeta()
        if not os.path.exists(ArchivoServicio.RUTA_USUARIOS):
            return []
        try:
            with open(ArchivoServicio.RUTA_USUARIOS, "r", encoding="utf-8") as f:
                contenido = f.read()
                if not contenido.strip():
                    return []
                data = json.loads(contenido)
                return [Usuario.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error al leer usuarios.json: {e}")
            return []
        except PermissionError:
            print("Error: Permiso denegado para leer el archivo de usuarios.")
            return []

    @staticmethod
    def guardar_usuarios(usuarios: list[Usuario]):
        ArchivoServicio._asegurar_carpeta()
        try:
            data = [u.to_dict() for u in usuarios]
            with open(ArchivoServicio.RUTA_USUARIOS, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo de usuarios.")

    # --- VENTAS ---
    @staticmethod
    def cargar_ventas() -> list[Venta]:
        ArchivoServicio._asegurar_carpeta()
        if not os.path.exists(ArchivoServicio.RUTA_VENTAS):
            return []
        try:
            with open(ArchivoServicio.RUTA_VENTAS, "r", encoding="utf-8") as f:
                contenido = f.read()
                if not contenido.strip():
                    return []
                data = json.loads(contenido)
                return [Venta.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error al leer ventas.json: {e}")
            return []
        except PermissionError:
            print("Error: Permiso denegado para leer el archivo de ventas.")
            return []

    @staticmethod
    def guardar_ventas(ventas: list[Venta]):
        ArchivoServicio._asegurar_carpeta()
        try:
            data = [v.to_dict() for v in ventas]
            with open(ArchivoServicio.RUTA_VENTAS, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("Error: Permiso denegado para escribir en el archivo de ventas.")