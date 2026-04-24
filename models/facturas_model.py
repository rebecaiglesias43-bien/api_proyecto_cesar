from flask import current_app
from datetime import datetime

class FacturaModel:
    ESTADOS_VALIDOS = ['pendiente', 'pagado', 'cancelado']
    
    def __init__(self, id_factura=None, id_cita=None, fecha=None, total=None, estado=None):
        self.id_factura = id_factura
        self.id_cita = id_cita
        self.fecha = fecha
        self.total = total
        self.estado = estado
    
    def to_dict(self):
        return {
            'id_factura': self.id_factura,
            'id_cita': self.id_cita,
            'fecha': str(self.fecha) if self.fecha else None,
            'total': float(self.total) if self.total else None,
            'estado': self.estado
        }
    
    @staticmethod
    def _validar_crear(id_cita, fecha, total, estado):
        """Valida datos para crear una factura"""
        errores = []
        
        # Validar id_cita
        if not id_cita:
            errores.append("id_cita es requerido")
        else:
            if not isinstance(id_cita, int) or id_cita <= 0:
                errores.append("id_cita debe ser un número positivo")
            else:
                cursor = current_app.mysql.connection.cursor()
                cursor.execute("SELECT cit_id FROM citas WHERE cit_id = %s", (id_cita,))
                if not cursor.fetchone():
                    errores.append(f"La cita con id {id_cita} no existe")
                cursor.close()
        
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
        
        # Validar total
        if total is None:
            errores.append("total es requerido")
        else:
            try:
                total_float = float(total)
                if total_float <= 0:
                    errores.append("total debe ser mayor a 0")
            except (ValueError, TypeError):
                errores.append("total debe ser un número válido")
        
        # Validar estado
        if not estado:
            errores.append("estado es requerido")
        elif estado.lower() not in FacturaModel.ESTADOS_VALIDOS:
            errores.append(f"estado debe ser uno de: {', '.join(FacturaModel.ESTADOS_VALIDOS)}")
        
        return errores
    
    @staticmethod
    def _validar_actualizar(id_factura, **datos):
        """Valida datos para actualizar una factura"""
        errores = []
        
        if not id_factura or not isinstance(id_factura, int) or id_factura <= 0:
            errores.append("id_factura debe ser un número positivo válido")
        
        if 'total' in datos and datos['total'] is not None:
            try:
                total_float = float(datos['total'])
                if total_float <= 0:
                    errores.append("total debe ser mayor a 0")
            except (ValueError, TypeError):
                errores.append("total debe ser un número válido")
        
        if 'estado' in datos and datos['estado']:
            if datos['estado'].lower() not in FacturaModel.ESTADOS_VALIDOS:
                errores.append(f"estado debe ser uno de: {', '.join(FacturaModel.ESTADOS_VALIDOS)}")
        
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
        cursor.execute("SELECT fac_id, fac_cita_id, fac_fecha, fac_total, fac_estado FROM facturas")
        facturas = cursor.fetchall()
        cursor.close()
        resultado = []
        for f in facturas:
            resultado.append(FacturaModel(f[0], f[1], f[2], f[3], f[4]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_factura):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT fac_id, fac_cita_id, fac_fecha, fac_total, fac_estado FROM facturas WHERE fac_id = %s", (id_factura,))
        f = cursor.fetchone()
        cursor.close()
        if f:
            return FacturaModel(f[0], f[1], f[2], f[3], f[4]).to_dict()
        return None
    
    @staticmethod
    def obtener_por_cita(id_cita):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT fac_id, fac_cita_id, fac_fecha, fac_total, fac_estado FROM facturas WHERE fac_cita_id = %s", (id_cita,))
        f = cursor.fetchone()
        cursor.close()
        if f:
            return FacturaModel(f[0], f[1], f[2], f[3], f[4]).to_dict()
        return None
    
    @staticmethod
    def crear(id_cita, fecha, total, estado):
        # Validar antes de insertar
        errores = FacturaModel._validar_crear(id_cita, fecha, total, estado)
        if errores:
            return {'error': "; ".join(errores)}
        
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO facturas (fac_cita_id, fac_fecha, fac_total, fac_estado) VALUES (%s, %s, %s, %s)", (id_cita, fecha, total, estado))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return FacturaModel.obtener_por_id(id_generado)
    
    @staticmethod
    def actualizar(id_factura, **datos):
        # Validar antes de actualizar
        errores = FacturaModel._validar_actualizar(id_factura, **datos)
        if errores:
            return {'error': "; ".join(errores)}
        
        # Construir query dinámicamente
        campos = []
        valores = []
        for clave, valor in datos.items():
            if valor is not None:
                if clave == 'estado':
                    campos.append(f'fac_estado = %s')
                elif clave == 'total':
                    campos.append(f'fac_total = %s')
                elif clave == 'fecha':
                    campos.append(f'fac_fecha = %s')
                valores.append(valor)
        
        if not campos:
            return FacturaModel.obtener_por_id(id_factura)
        
        valores.append(id_factura)
        query = f"UPDATE facturas SET {', '.join(campos)} WHERE fac_id = %s"
        
        cursor = current_app.mysql.connection.cursor()
        cursor.execute(query, valores)
        current_app.mysql.connection.commit()
        cursor.close()
        
        return FacturaModel.obtener_por_id(id_factura)
    
    @staticmethod
    def actualizar_estado(id_factura, estado):
        """Método de conveniencia para actualizar solo el estado"""
        return FacturaModel.actualizar(id_factura, estado=estado)