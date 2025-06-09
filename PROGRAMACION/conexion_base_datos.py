import mysql.connector
import config  # Importa los datos de conexión

def conectar_bd():
    """Establece la conexión con la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DATABASE,
            port=config.PORT
        )
        print(" Conexión a MySQL exitosa.")
        return conexion
    except mysql.connector.Error as e:
        print(f" Error de conexión: {e}")
        return None
