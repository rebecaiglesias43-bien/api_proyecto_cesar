from flask import current_app

class DetalleFacturaModel:
    def __init__(self, id_detalle=None, id_factura=None, id_servicio=None, subtotal=None):
        self.id_detalle = id_detalle
        self.id_factura = id_factura
        self.id_servicio = id_servicio
        self.subtotal = subtotal
    
    def to_dict(self):
        return {
            'id_detalle': self.id_detalle,
            'id_factura': self.id_factura,
            'id_servicio': self.id_servicio,
            'subtotal': float(self.subtotal) if self.subtotal else None
        }
    
    @staticmethod
    def _validar_crear(id_factura, id_servicio, subtotal):
        """Valida datos para crear un detalle de factura"""
        errores = []
        
        # Validar id_factura
        if not id_factura:
            errores.append("id_factura es requerido")
        else:
            if not isinstance(id_factura, int) or id_factura <= 0:
                errores.append("id_factura debe ser un número positivo")
            else:
                cursor = current_app.mysql.connection.cursor()
                cursor.execute("SELECT fac_id FROM facturas WHERE fac_id = %s", (id_factura,))
                if not cursor.fetchone():
                    errores.append(f"La factura con id {id_factura} no existe")
                cursor.close()
        
        # Validar id_servicio
        if not id_servicio:
            errores.append("id_servicio es requerido")
        else:
            if not isinstance(id_servicio, int) or id_servicio <= 0:
                errores.append("id_servicio debe ser un número positivo")
            else:
                cursor = current_app.mysql.connection.cursor()
                cursor.execute("SELECT ser_id FROM servicios WHERE ser_id = %s", (id_servicio,))
                if not cursor.fetchone():
                    errores.append(f"El servicio con id {id_servicio} no existe")
                cursor.close()
        
        # Validar subtotal
        if subtotal is None:
            errores.append("subtotal es requerido")
        else:
            try:
                subtotal_float = float(subtotal)
                if subtotal_float <= 0:
                    errores.append("subtotal debe ser mayor a 0")
            except (ValueError, TypeError):
                errores.append("subtotal debe ser un número válido")
        
        return errores
    
    @staticmethod
    def _validar_actualizar(id_detalle, **datos):
        """Valida datos para actualizar un detalle de factura"""
        errores = []
        
        if not id_detalle or not isinstance(id_detalle, int) or id_detalle <= 0:
            errores.append("id_detalle debe ser un número positivo válido")
        
        if 'subtotal' in datos and datos['subtotal'] is not None:
            try:
                subtotal_float = float(datos['subtotal'])
                if subtotal_float <= 0:
                    errores.append("subtotal debe ser mayor a 0")
            except (ValueError, TypeError):
                errores.append("subtotal debe ser un número válido")
        
        return errores
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dfa_id, dfa_factura_id, dfa_servicio_id, dfa_subtotal FROM detalle_facturas")
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    @staticmethod
    def listar_por_factura(id_factura):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dfa_id, dfa_factura_id, dfa_servicio_id, dfa_subtotal FROM detalle_facturas WHERE dfa_factura_id = %s", (id_factura,))
        detalles = cursor.fetchall()
        cursor.close()
        resultado = []
        for d in detalles:
            resultado.append(DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict())
        return resultado
    
    @staticmethod
    def crear(id_factura, id_servicio, subtotal):
        # Validar antes de insertar
        errores = DetalleFacturaModel._validar_crear(id_factura, id_servicio, subtotal)
        if errores:
            return {'error': "; ".join(errores)}
        
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO detalle_facturas (dfa_factura_id, dfa_servicio_id, dfa_subtotal) VALUES (%s, %s, %s)", (id_factura, id_servicio, subtotal))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dfa_id, dfa_factura_id, dfa_servicio_id, dfa_subtotal FROM detalle_facturas WHERE dfa_id = %s", (id_generado,))
        d = cursor.fetchone()
        cursor.close()
        if d:
            return DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict()
        return None
    
    @staticmethod
    def actualizar(id_detalle, **datos):
        # Validar antes de actualizar
        errores = DetalleFacturaModel._validar_actualizar(id_detalle, **datos)
        if errores:
            return {'error': "; ".join(errores)}
        
        # Construir query dinámicamente
        campos = []
        valores = []
        for clave, valor in datos.items():
            if valor is not None:
                if clave == 'subtotal':
                    campos.append(f'dfa_subtotal = %s')
                elif clave == 'id_servicio':
                    campos.append(f'dfa_servicio_id = %s')
                valores.append(valor)
        
        if not campos:
            return DetalleFacturaModel.obtener_por_id(id_detalle)
        
        valores.append(id_detalle)
        query = f"UPDATE detalle_facturas SET {', '.join(campos)} WHERE dfa_id = %s"
        
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(query, valores)
        current_app.mysql.connection.commit()
        cursor.close()
        
        return DetalleFacturaModel.obtener_por_id(id_detalle)
    
    @staticmethod
    def obtener_por_id(id_detalle):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT dfa_id, dfa_factura_id, dfa_servicio_id, dfa_subtotal FROM detalle_facturas WHERE dfa_id = %s", (id_detalle,))
        d = cursor.fetchone()
        cursor.close()
        if d:
            return DetalleFacturaModel(d[0], d[1], d[2], d[3]).to_dict()
        return None