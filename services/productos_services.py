from decimal import Decimal, InvalidOperation

from models.productos_model import ProductoModel

class ProductoService:
    def __init__(self, mysql):
        self.mysql = mysql

    def listar_todos(self, page, per_page):
        return ProductoModel.listar_todos(self.mysql, page, per_page)

    def obtener_por_id(self, id_producto):
        return ProductoModel.obtener_por_id(self.mysql, id_producto)

    def _validar_payload(self, data):
        if not isinstance(data, dict):
            raise ValueError('El cuerpo de la solicitud debe ser un objeto JSON')

        nombre = data.get('nombre')
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError('El campo "nombre" es requerido y debe ser una cadena de texto')
        nombre = nombre.strip()
        if len(nombre) > 100:
            raise ValueError('El campo "nombre" supera el maximo de 100 caracteres')

        precio = data.get('precio')
        if precio is None:
            raise ValueError('El campo "precio" es requerido')
        try:
            precio = Decimal(str(precio))
        except (InvalidOperation, TypeError, ValueError):
            raise ValueError('El campo "precio" debe ser un numero valido')
        if precio < 0:
            raise ValueError('El campo "precio" no puede ser negativo')

        stock = data.get('stock')
        if stock is None:
            raise ValueError('El campo "stock" es requerido')
        if isinstance(stock, bool) or not isinstance(stock, int):
            raise ValueError('El campo "stock" debe ser un numero entero')
        if stock < 0:
            raise ValueError('El campo "stock" no puede ser negativo')

        estado = data.get('estado')
        if not isinstance(estado, str) or not estado.strip():
            raise ValueError('El campo "estado" es requerido y debe ser una cadena de texto')
        estado = estado.strip().lower()
        if len(estado) > 20:
            raise ValueError('El campo "estado" supera el maximo de 20 caracteres')
        if estado not in {'activo', 'inactivo'}:
            raise ValueError('El campo "estado" debe ser "activo" o "inactivo"')

        return nombre, precio, stock, estado

    def crear(self, data):
        nombre, precio, stock, estado = self._validar_payload(data)
        return ProductoModel.crear(self.mysql, nombre, precio, stock, estado)
