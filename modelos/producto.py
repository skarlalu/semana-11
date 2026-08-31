class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str):
        if not valor.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        self._codigo = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = float(valor)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = int(valor)

    def vender(self, cantidad: int) -> None:
        """Disminuye el stock del producto de forma controlada."""
        if cantidad > self._stock:
            raise ValueError("No hay stock suficiente para realizar la venta.")
        self.stock -= cantidad

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            codigo=data["codigo"],
            nombre=data["nombre"],
            categoria=data["categoria"],
            precio=data["precio"],
            stock=data["stock"]
        )