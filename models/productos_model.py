from flask import current_app

class ProductoModel:
    def __init__(self, id_producto=None, nombre=None, precio=None, stock=None, estado=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.estado = estado
    
    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'precio': float(self.precio) if self.precio is not None else None,
            'stock': self.stock,
            'estado': self.estado
        }

    @staticmethod
    def listar_todos(mysql, page, per_page):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM productos")
        total = cursor.fetchone()[0]
        offset = (page - 1) * per_page
        cursor.execute(
            "SELECT pro_id, pro_nombre, pro_precio, pro_stock, pro_estado "
            "FROM productos ORDER BY pro_id LIMIT %s OFFSET %s",
            (per_page, offset)
        )
        productos = cursor.fetchall()
        cursor.close()
        data = [ProductoModel(p[0], p[1], p[2], p[3], p[4]).to_dict() for p in productos]
        total_pages = (total + per_page - 1) // per_page if total else 0
        return {
            'data': data,
            'total': total,
            'page': page,
            'per_page': per_page,
            'total_pages': total_pages
        }

    @staticmethod
    def obtener_por_id(mysql, id_producto):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT pro_id, pro_nombre, pro_precio, pro_stock, pro_estado FROM productos WHERE pro_id = %s", (id_producto,))
        p = cursor.fetchone()
        cursor.close()
        if p:
            return ProductoModel(p[0], p[1], p[2], p[3], p[4]).to_dict()
        return None

    @staticmethod
    def crear(mysql, nombre, precio, stock, estado):
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO productos (pro_nombre, pro_precio, pro_stock, pro_estado) VALUES (%s, %s, %s, %s)", (nombre, precio, stock, estado))
        mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return ProductoModel.obtener_por_id(mysql, id_generado)
