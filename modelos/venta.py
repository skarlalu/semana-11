class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    @property
    def cantidad(self) -> int: # <--- Aquí estaba el error
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int):
        if valor <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")
        self._cantidad = int(valor)

    def to_dict(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            usuario_id=data["usuario_id"],
            producto_codigo=data["producto_codigo"],
            cantidad=data["cantidad"]
        )