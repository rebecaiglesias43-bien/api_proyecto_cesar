from flask import current_app
from datetime import datetime

class PagoModel:
    METODOS_VALIDOS = ['efectivo', 'tarjeta', 'transferencia', 'cheque', 'deposito']
    
    def __init__(self, id_pago=None, id_factura=None, metodo=None, fecha=None, monto=None):
        self.id_pago = id_pago
        self.id_factura = id_factura
        self.metodo = metodo
        self.fecha = fecha
        self.monto = monto
    
    def to_dict(self):
        return {
            'id_pago': self.id_pago,
            'id_factura': self.id_factura,
            'metodo': self.metodo,
            'fecha': str(self.fecha) if self.fecha else None,
            'monto': float(self.monto) if self.monto else None
        }
    
    @staticmethod
    def _validar_crear(id_factura, metodo, fecha, monto):
        """Valida datos para crear un pago"""
        errores = []
        
        # Validar id_factura
        if not id_factura:
            errores.append("id_factura es requerido")
        else:
            if not isinstance(id_factura, int) or id_factura <= 0:
                errores.append("id_factura debe ser un número positivo")
            else:
                cursor = current_app.mysql.connection.cursor()
                cursor.execute("SELECT fac_id, fac_total FROM facturas WHERE fac_id = %s", (id_factura,))
                factura = cursor.fetchone()
                cursor.close()
                
                if not factura:
                    errores.append(f"La factura con id {id_factura} no existe")
                else:
                    total_factura = float(factura[1]) if factura[1] else 0
                    
                    # Validar monto no sea mayor al total de la factura
                    if monto is not None:
                        try:
                            monto_float = float(monto)
                            if monto_float > total_factura:
                                errores.append(f"El monto no puede ser mayor al total de la factura ({total_factura})")
                        except (ValueError, TypeError):
                            pass  # Se validará en la siguiente sección
        
        # Validar metodo
        if not metodo:
            errores.append("metodo es requerido")
        elif metodo.lower() not in PagoModel.METODOS_VALIDOS:
            errores.append(f"metodo debe ser uno de: {', '.join(PagoModel.METODOS_VALIDOS)}")
        
        # Validar fecha
        if not fecha:
            errores.append("fecha es requerida")
        else:
            try:
                fecha_obj = datetime.strptime(str(fecha), '%Y-%m-%d')
                if fecha_obj > datetime.now():
                    errores.append("La fecha no puede ser en el futuro")
            except ValueError:
                errores.append("fecha debe estar en formato YYYY-MM-DD")
        
        # Validar monto
        if monto is None:
            errores.append("monto es requerido")
        else:
            try:
                monto_float = float(monto)
                if monto_float <= 0:
                    errores.append("monto debe ser mayor a 0")
            except (ValueError, TypeError):
                errores.append("monto debe ser un número válido")
        
        return errores
    
    @staticmethod
    def _validar_actualizar(id_pago, **datos):
        """Valida datos para actualizar un pago"""
        errores = []
        
        if not id_pago or not isinstance(id_pago, int) or id_pago <= 0:
            errores.append("id_pago debe ser un número positivo válido")
        
        if 'monto' in datos and datos['monto'] is not None:
            try:
                monto_float = float(datos['monto'])
                if monto_float <= 0:
                    errores.append("monto debe ser mayor a 0")
            except (ValueError, TypeError):
                errores.append("monto debe ser un número válido")
        
        if 'metodo' in datos and datos['metodo']:
            if datos['metodo'].lower() not in PagoModel.METODOS_VALIDOS:
                errores.append(f"metodo debe ser uno de: {', '.join(PagoModel.METODOS_VALIDOS)}")
        
        if 'fecha' in datos and datos['fecha']:
            try:
                fecha_obj = datetime.strptime(str(datos['fecha']), '%Y-%m-%d')
                if fecha_obj > datetime.now():
                    errores.append("La fecha no puede ser en el futuro")
            except ValueError:
                errores.append("fecha debe estar en formato YYYY-MM-DD")
        
        return errores
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT pag_id, pag_factura_id, pag_metodo, pag_fecha, pag_monto FROM pagos")
        pagos = cursor.fetchall()
        cursor.close()
        resultado = []
        for p in pagos:
            resultado.append(PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_pago):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT pag_id, pag_factura_id, pag_metodo, pag_fecha, pag_monto FROM pagos WHERE pag_id = %s", (id_pago,))
        p = cursor.fetchone()
        cursor.close()
        if p:
            return PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict()
        return None
    
    @staticmethod
    def listar_por_factura(id_factura):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT pag_id, pag_factura_id, pag_metodo, pag_fecha, pag_monto FROM pagos WHERE pag_factura_id = %s", (id_factura,))
        pagos = cursor.fetchall()
        cursor.close()
        resultado = []
        for p in pagos:
            resultado.append(PagoModel(p[0], p[1], p[2], p[3], p[4]).to_dict())
        return resultado
    
    @staticmethod
    def crear(id_factura, metodo, fecha, monto):
        # Validar antes de insertar
        errores = PagoModel._validar_crear(id_factura, metodo, fecha, monto)
        if errores:
            return {'error': "; ".join(errores)}
        
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO pagos (pag_factura_id, pag_metodo, pag_fecha, pag_monto) VALUES (%s, %s, %s, %s)", (id_factura, metodo, fecha, monto))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return PagoModel.obtener_por_id(id_generado)
    
    @staticmethod
    def actualizar(id_pago, **datos):
        # Validar antes de actualizar
        errores = PagoModel._validar_actualizar(id_pago, **datos)
        if errores:
            return {'error': "; ".join(errores)}
        
        # Construir query dinámicamente
        campos = []
        valores = []
        for clave, valor in datos.items():
            if valor is not None:
                if clave == 'metodo':
                    campos.append(f'pag_metodo = %s')
                elif clave == 'fecha':
                    campos.append(f'pag_fecha = %s')
                elif clave == 'monto':
                    campos.append(f'pag_monto = %s')
                valores.append(valor)
        
        if not campos:
            return PagoModel.obtener_por_id(id_pago)
        
        valores.append(id_pago)
        query = f"UPDATE pagos SET {', '.join(campos)} WHERE pag_id = %s"
        
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(query, valores)
        current_app.mysql.connection.commit()
        cursor.close()
        
        return PagoModel.obtener_por_id(id_pago)