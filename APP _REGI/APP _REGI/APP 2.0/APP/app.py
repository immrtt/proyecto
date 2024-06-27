from flask import Flask, render_template, jsonify, request
import psycopg2

app = Flask(__name__)

# Configura la conexión a la base de datos
cnx = psycopg2.connect(user="mayra", password="", host="servidor-personal.postgres.database.azure.com", port=5432, database="postgres")

# Ruta principal que muestra el formulario HTML
@app.route('/')
def index():
    return render_template('add.html')

# Ruta para manejar la solicitud POST del formulario
@app.route('/add_trabajador', methods=['POST'])
def get_data():
    # Obtener los datos del formulario HTML
    rut = request.form['t-rut']
    nombres = request.form['t-nombres']
    apellidos = request.form['t-apellidos']
    sexo = request.form['t-sexo']
    telefono = request.form['t-telefono']
    fecha_nacimiento = request.form['t-fechanacimiento']
    fecha_ingreso = request.form['t-fechaingreso']
    correo = request.form['t-correo']

    try:
        # Crear un cursor para ejecutar consultas SQL
        cursor = cnx.cursor()
        
        # Consulta SQL para insertar datos en la tabla trabajadores
        sql = "INSERT INTO empleado (rut, nombres, apellidos, sexo, telefono, fecha_nacimiento, fecha_ingreso, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(sql, (rut, nombres, apellidos, sexo, telefono, fecha_nacimiento, fecha_ingreso, correo))
        
        # Confirmar la inserción de datos
        cnx.commit()
        
        # Cerrar el cursor
        cursor.close()
        
        # Devolver una respuesta JSON indicando el éxito de la operación
        return jsonify({"message": "Datos insertados correctamente"}), 200
    
    except Exception as e:
        # En caso de error, devolver un mensaje de error en formato JSON
        return jsonify({"error": str(e)}), 500

# Punto de entrada para ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
