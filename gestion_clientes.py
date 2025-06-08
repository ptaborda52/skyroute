from conexion_base_datos import conectar_bd #conectamos a la base de datos
import re  # Importar módulo para expresiones regulares lo utilizamos en validaciones de email
#menu principal del modulo de gestion de clientes
def menu_clientes():
    while True: #ciclo principal del modulo.
        print("\nMenú Clientes:")
        print("1. Agregar cliente")
        print("2. Modificar cliente")
        print("3. Eliminar cliente")
        print("4. Mostrar clientes")
        print("5. Volver al menú principal")

        opcion_clientes = input("Seleccione una opción: ")
#agragar clientes nuevos.
        if opcion_clientes == "1":
            print("\nSeleccionó: Agregar cliente.")
            cuit = input("Ingrese cuit: ")  
            razon_social = input("Ingrese Razón Social: ")
            email = input("Ingrese Email: ")
            agregar_cliente(cuit, razon_social, email)  
#modificamos clientes existentes.
        elif opcion_clientes == "2":
            print("\nSeleccionó: Modificar cliente.")
            cuit = input("Ingrese cuit del cliente a modificar: ")

            if cliente_existe(cuit, conectar_bd()): #verifica que el cliente este cargado para que desde aca no se puedan agregar clientes nuevos.
                razon_social = input("Ingrese nueva Razón Social: ")
                email = input("Ingrese nuevo Email: ")
                modificar_cliente(cuit, razon_social, email)
            else:
                print(" Error: No se encontró un cliente con ese cuit.")
#eliminamos clientes existentes.
        elif opcion_clientes == "3":
            print("\nSeleccionó: Eliminar cliente.")
            print("\n No se podra eliminar un cliente si tiene ventas registradas.")
            cuit = input("Ingrese cuit del cliente a eliminar: ")

            if cliente_existe(cuit, conectar_bd()):
                #agregamos esta validacion para evitar eliminaciones accidentales.
                confirmar = input(f" ¿Estás seguro de que quieres eliminar al cliente con cuit {cuit}? (s/n): ")
                if confirmar.lower() == "s": #al probar el sistema y poniamos "S" en mayusculas no nos tomaba la entrasa asi que encontramos este comando.
                    eliminar_cliente(cuit)
                else:
                    print(" Operación cancelada.")
            else:
                print(" Error: No se encontró un cliente con ese cuit.")
#menu consulta de clientes.
        elif opcion_clientes == "4":
            print("\nSeleccionó: Mostrar clientes con filtros.")
            print("1. Listar todos")
            print("2. Buscar por cuit")
            print("3. Filtrar por razón social")
            print("4. Filtrar por email")
        
            filtro = input("Seleccione una opción: ")
            if filtro == "1":
                mostrar_clientes()
            elif filtro == "2":
                cuit = input("Ingrese cuit: ")
                mostrar_clientes(filtro="cuit", valor=cuit)
            elif filtro == "3":
                razon_social = input("Ingrese Razón Social (o parte de ella): ")
                mostrar_clientes(filtro="razon_social", valor=razon_social)
            elif filtro == "4":
                email = input("Ingrese Email (o parte de él): ")
                mostrar_clientes(filtro="email", valor=email)
        elif opcion_clientes == "5":
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.") #aca cerramos el ciclo principal del modulo.

def es_cuit_valido(cuit): #nos aseguramos de no ingresar un cuit erroneo.
    """Verifica que el cuit tenga exactamente 11 caracteres y sea numérico."""
    return cuit.isdigit() and len(cuit) == 11 #retorna True si el cuit es valido, False si no lo es. (para que sea valido deben darse las 2 condiciones: insdigit (solo numeros) len (cantidad de digitos))

def es_email_valido(email): #nos aseguramos de no ingresar un email erroneo.
    """Verifica que el email tenga un formato válido usando expresiones regulares."""
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email)

def cliente_existe(cuit, conexion): #verificamos que el cliente este en nuestra base de datos para trabajar sobre el.
    """Verifica si el cuit ya está registrado en la base de datos."""
    cursor = conexion.cursor()
    sql = "SELECT COUNT(*) FROM clientes WHERE cuit = %s"
    cursor.execute(sql, (cuit,))
    resultado = cursor.fetchone()[0] #cuenta los registros que coinciden con el cuit ingresado.
    cursor.close()
    return resultado > 0  # Retorna True si el cliente ya existe
def agregar_cliente(cuit, razon_social, email):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    if not es_cuit_valido(cuit):
        print(" Error: cuit inválido.")
        return
    if not es_email_valido(email):
        print(" Error: El email ingresado no tiene un formato válido.")
        return
    if cliente_existe(cuit, conexion):
        print(" Error: Este cuit ya está registrado en la base de datos.")
        conexion.close()
        return
# como en las pruebas obtuvimos errores inesperados usamos la funcion Try/Except para manejar errores SQL y evitar que el programa se detenga.
    try: #ejecuta el codigo pero si ocurre un error lo captura y pasa a except. 
        cursor = conexion.cursor()
        sql = "INSERT INTO clientes (cuit, razon_social, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (cuit, razon_social, email))
        conexion.commit() #guarda en base de datos los cambios realizados.
        print(" Cliente agregado correctamente.")
        print("\nCliente ingresado:")
        print(f"• cuit: {cuit}")
        print(f"• Razón Social: {razon_social}")
        print(f"• Email: {email}")
    except Exception as e: #captura el error y lo muestra en pantalla.
        print(f" Error SQL: {e}")
    finally: #finaliza el codigo y se ejecuta siempre, incluso si hubo un error.
        cursor.close()
        conexion.close()
def modificar_cliente(cuit, nueva_razon_social, nuevo_email):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    if not es_email_valido(nuevo_email):
        print(" Error: El email ingresado no tiene un formato válido.")
        return

    try:
        cursor = conexion.cursor()
        sql = """
            UPDATE clientes 
            SET razon_social = %s, email = %s 
            WHERE cuit = %s
        """
        cursor.execute(sql, (nueva_razon_social, nuevo_email, cuit))
        conexion.commit()
        print(" Cliente modificado correctamente.")

        print("\nDatos actualizados:")
        print(f"• cuit: {cuit}")
        print(f"• Nueva Razón Social: {nueva_razon_social}")
        print(f"• Nuevo Email: {nuevo_email}")

    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_cliente(cuit):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM clientes WHERE cuit = %s"
        cursor.execute(sql, (cuit,))
        conexion.commit()
        print(" Cliente eliminado correctamente.")
    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()
def mostrar_clientes(filtro=None, valor=None):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    try:
        cursor = conexion.cursor(dictionary=True)  # Para obtener resultados como diccionarios

        if filtro is None:
            sql = "SELECT * FROM clientes"
            cursor.execute(sql)
        else:
            sql = f"SELECT * FROM clientes WHERE {filtro} LIKE %s"
            cursor.execute(sql, (f"%{valor}%",))

        resultados = cursor.fetchall() #devuelve una lista con tuplas que representan las filas de la tabla clientes.
        cursor.close()
        conexion.close()

        if resultados:
            print("\n Clientes encontrados:")
            for cliente in resultados:
                print(f"• cuit: {cliente['cuit']}, Razón Social: {cliente['razon_social']}, Email: {cliente['email']}")
        else:
            print(" No se encontraron clientes con los criterios ingresados.")

    except Exception as e:
        print(f" Error SQL: {e}")