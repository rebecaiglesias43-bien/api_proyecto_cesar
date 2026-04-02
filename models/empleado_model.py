from flask import current_app

class EmpleadoModel:
    def __init__(self, id_empleado=None, id_usuario=None, nombre=None, apellido=None, telefono=None, cargo=None, especialidad=None):
        self.id_empleado = id_empleado
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.cargo = cargo
        self.especialidad = especialidad
    
    def to_dict(self):
        return {
            'id_empleado': self.id_empleado,
            'id_usuario': self.id_usuario,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'cargo': self.cargo,
            'especialidad': self.especialidad
        }
    
    @staticmethod
    def listar_todos():
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT emp_id, emp_usuario_id, emp_nombre, emp_apellido, emp_telefono, emp_cargo, emp_especialidad FROM empleados")
        empleados = cursor.fetchall()
        cursor.close()
        resultado = []
        for e in empleados:
            resultado.append(EmpleadoModel(e[0], e[1], e[2], e[3], e[4], e[5], e[6]).to_dict())
        return resultado
    
    @staticmethod
    def obtener_por_id(id_empleado):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("SELECT emp_id, emp_usuario_id, emp_nombre, emp_apellido, emp_telefono, emp_cargo, emp_especialidad FROM empleados WHERE emp_id = %s", (id_empleado,))
        e = cursor.fetchone()
        cursor.close()
        if e:
            return EmpleadoModel(e[0], e[1], e[2], e[3], e[4], e[5], e[6]).to_dict()
        return None
    
    @staticmethod
    def crear(id_usuario, nombre, apellido, telefono, cargo, especialidad):
        cursor = current_app.mysql.connection.cursor()
        cursor.execute("INSERT INTO empleados (emp_usuario_id, emp_nombre, emp_apellido, emp_telefono, emp_cargo, emp_especialidad) VALUES (%s, %s, %s, %s, %s, %s)", (id_usuario, nombre, apellido, telefono, cargo, especialidad))
        current_app.mysql.connection.commit()
        id_generado = cursor.lastrowid
        cursor.close()
        return EmpleadoModel.obtener_por_id(id_generado)