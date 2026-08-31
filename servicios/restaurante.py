from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self):
        self._productos: list[Producto] = ArchivoServicio.cargar_productos()
        self._usuarios: list[Usuario] = ArchivoServicio.cargar_usuarios()
        self._ventas: list[Venta] = ArchivoServicio.cargar_ventas()

    # --- PRODUCTOS ---
    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False
        self._productos.append(producto)
        ArchivoServicio.guardar_productos(self._productos)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        for p in self._productos:
            if p.codigo.lower() == codigo.lower().strip():
                return p
        return None

    def listar_productos(self) -> list[Producto]:
        return self._productos

    # --- USUARIOS ---
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        ArchivoServicio.guardar_usuarios(self._usuarios)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for u in self._usuarios:
            if u.identificacion.lower() == identificacion.lower().strip():
                return u
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    # --- VENTAS Y REGLAS DE NEGOCIO ---
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        # Realizar operación
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)

        # Persistir cambios en ambas colecciones
        ArchivoServicio.guardar_ventas(self._ventas)
        ArchivoServicio.guardar_productos(self._productos)
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        ventas_usuario: list[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id.lower() == identificacion_usuario.lower().strip():
                ventas_usuario.append(venta)
        return ventas_usuario