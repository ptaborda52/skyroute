from conexion_base_datos import conectar_bd
from consultas_ventas import menu_consultas_ventas
from datetime import datetime, timedelta #CORRECCION ERROR CONVERTIR FECHA DE USUARIO A FORMATO MYSQL

def convertir_fecha(fecha_usuario):
    """
    Convierte una fecha en formato 'dd/mm/aaaa' a 'aaaa-mm-dd' para MySQL.
    Devuelve None si el formato es incorrecto.
    """
    try:
        fecha_dt = datetime.strptime(fecha_usuario, "%d/%m/%Y")
        return fecha_dt.strftime("%Y-%m-%d")
    except ValueError:
        print(" Error: Formato de fecha incorrecto. Use dd/mm/aaaa.")
        return None

def menu_ventas():
    while True:
        print("\nMenú Ventas:")
        print("1. Registrar venta")
        print("2. Modificar venta")
        print("3. Botón de arrepentimiento o Anular una venta")
        print("4. Consultar ventas")
        print("5. Volver al menú principal")

        opcion_ventas = input("Seleccione una opción: ")

        if opcion_ventas == "1":
            print("\n--- Registrar Venta ---")
            print("\n Consulte antes el ID de nuestros destinos disponibles.\n")
            cuit_cliente = input("Ingrese cuit del Cliente: ")
            id_destino = input("Ingrese ID del Destino: ")
            fecha_viaje = input("Ingrese Fecha del Viaje (dd/mm/aaaa): ")
            registrar_venta(cuit_cliente, id_destino, fecha_viaje)

        elif opcion_ventas == "2":
            print("\nSeleccionó: Modificar venta.")
            print("\n Recuerde el id de la venta proporcionado al registro.")
            print("\n Puede consultar el ID de la venta a modificar en el menú de Consultas de Ventas.")
            id_venta = input("\n Ingrese ID de la venta a modificar: ")

            # Pedimos los nuevos datos antes de llamar a la función
            cuit_cliente = input("Ingrese el nuevo CUIT del Cliente: ")
            id_destino = input("Ingrese el nuevo ID del Destino: ")
            fecha_viaje = input("Ingrese la nueva Fecha del Viaje (dd/mm/aaaa): ")

            modificar_venta(id_venta, cuit_cliente, id_destino, fecha_viaje)  # Ahora pasamos todos los argumentos

        elif opcion_ventas == "3":
            print("\nSeleccionó: Botón de arrepentimiento o anular una venta.")
            print("\n Recuerde el id de la venta proporcionado al registro.")
            print("\n Puede consultar el ID de la venta a anular en el menú de Consultas de Ventas.")
            id_venta = input("\n Ingrese ID de la venta a anular: ")
            print("\nSeleccione el tipo de anulación:")
            print("1. Administrador")
            print("2. Botón de arrepentimiento (últimos 60 días)")
            tipo_opcion = input("Ingrese opción (1 o 2): ")
    
            if tipo_opcion == "1":
                tipo = "admin"
            elif tipo_opcion == "2":
                print("\n PODES PEDIR LA CANCELACIÓN DE UNA VENTA REALIZADA EN LOS ÚLTIMOS 60 DÍAS CORRIDOS.\n")
                tipo = "arrepentimiento"
            else:
                print(" Opción inválida. Volviendo al menú...")
                return
            anular_venta(id_venta, tipo)
            
        elif opcion_ventas == "4":
            print("\nAccediendo al Submenú de Consultas de Ventas...")
            menu_consultas_ventas()

        elif opcion_ventas == "5":
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

def registrar_venta(cuit_cliente, id_destino, fecha_viaje):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    fecha_viaje_mysql = convertir_fecha(fecha_viaje)  # Convertimos la fecha antes de enviarla a MySQL

    if fecha_viaje_mysql:
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO ventas (cuit_cliente, id_destino, fecha_viaje) VALUES (%s, %s, %s)"
            cursor.execute(sql, (cuit_cliente, id_destino, fecha_viaje_mysql))
            conexion.commit()
             #  Obtener el ID de la venta recién insertada
            cursor.execute("SELECT LAST_INSERT_ID()")
            id_venta = cursor.fetchone()[0]

            print(" Venta registrada correctamente.")
            print(f" ID de la venta registrada: {id_venta}")  # Ahora muestra el ID de la venta

        except Exception as e:
            print(f" Error SQL: {e}")
        finally:
            cursor.close()
            conexion.close()
def modificar_venta(id_venta, cuit_cliente, id_destino, fecha_viaje):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    fecha_viaje_mysql = convertir_fecha(fecha_viaje)  # Convertimos la fecha antes de enviarla a MySQL

    try:
        cursor = conexion.cursor()

        #  Verificar si la venta realmente existe
        cursor.execute("SELECT COUNT(*) FROM ventas WHERE id = %s", (id_venta,))
        existe = cursor.fetchone()[0]

        if existe == 0:
            print(f" Error: La venta con ID {id_venta} no existe.")
            return

        #  Si la venta existe, proceder con la modificación
        sql = "UPDATE ventas SET cuit_cliente = %s, id_destino = %s, fecha_viaje = %s WHERE id = %s"
        cursor.execute(sql, (cuit_cliente, id_destino, fecha_viaje_mysql, id_venta))
        conexion.commit()
        print(" Venta modificada correctamente.")
    
    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()
def anular_venta(id_venta, tipo):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    try:
        cursor = conexion.cursor()

        #  Verificar si la venta realmente existe
        cursor.execute("SELECT fecha_registro FROM ventas WHERE id = %s", (id_venta,))
        resultado = cursor.fetchone()

        if not resultado:
            print(f" Error: La venta con ID {id_venta} no existe.")
            return

        fecha_registro = resultado[0]  # Extraer la fecha de registro
        # Validar que la venta se realizó en los últimos **3 minutos** equivalente a 60dias (1 dia cada 3segundos)
        limite_fecha = datetime.now() - timedelta(minutes=3)
        # Si el tipo es "arrepentimiento"
        if tipo == "arrepentimiento":
            if fecha_registro < limite_fecha:
                print(" Error: Solo se pueden anular ventas realizadas en los últimos 60 días.")
                return
        #  Anular la venta y marcar el tipo de anulación
        sql = "UPDATE ventas SET estado = 'anulada', tipo_anulacion = %s WHERE id = %s"
        cursor.execute(sql, (tipo, id_venta))
        conexion.commit()

        print(f" Venta con ID {id_venta} anulada correctamente bajo el tipo '{tipo}'.")
    
    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()