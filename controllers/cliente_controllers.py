from flask import jsonify, current_app
import traceback

def cntlistado():
    try:
        print("=== Iniciando cntlistado ===")
        mysql = current_app.mysql
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()
        print(f"Clientes encontrados: {len(clientes)}")
        
        resultado = []
        for cliente in clientes:
            resultado.append({
                'id_cliente': cliente[0],
                'nombre': cliente[1],
                'apellido': cliente[2],
                'telefono': cliente[3],
                'direccion': cliente[4],
                'id_usuarioFK': cliente[5]
            })
        
        print(f"Resultado: {resultado}")
        return jsonify(resultado)
        
    except Exception as e:
        print("=== ERROR ===")
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500