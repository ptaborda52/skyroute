from conexion_base_datos import conectar_bd

def menu_destinos():
    while True:
        print("\nMenú Destinos:")
        print("1. Agregar destino")
        print("2. Modificar destino")
        print("3. Eliminar destino")
        print("4. Mostrar destinos")
        print("5. Volver al menú principal")

        opcion_destinos = input("Seleccione una opción: ")

        if opcion_destinos == "1":
            print("\nSeleccionó: Agregar destino.")
            ciudad = input("Ingrese Ciudad: ")
            pais = input("Ingrese País: ")
            costo = input("Ingrese Costo: ")
            agregar_destino(ciudad, pais, costo)  

        elif opcion_destinos == "2":
            print("\nSeleccionó: Modificar destino.")
            print("\n Consulte el id del destino en la opcion 4- Mostrar destinos.\n")
            id_destino = input("Ingrese ID del destino a modificar: ")

            if destino_existe(id_destino, conectar_bd()):
                ciudad = input("Ingrese nueva Ciudad: ")
                pais = input("Ingrese nuevo País: ")
                costo = input("Ingrese nuevo Costo: ")
                modificar_destino(id_destino, ciudad, pais, costo)
            else:
                print(" Error: No se encontró un destino con ese ID.")

        elif opcion_destinos == "3":
            print("\nSeleccionó: Eliminar destino.")
            print("\n No se podrá eliminar un destino si tiene ventas registradas.")
            print("\n Consulte el id del destino en la opcion 4- Mostrar destinos.\n")
            id_destino = input("Ingrese ID del destino a eliminar: ")

            if destino_existe(id_destino, conectar_bd()):
                confirmar = input(f" ¿Estás seguro de eliminar el destino {id_destino}? (s/n): ")
                if confirmar.lower() == "s":
                    eliminar_destino(id_destino)
                else:
                    print(" Operación cancelada.")
            else:
                print(" Error: No se encontró un destino con ese ID.")

        elif opcion_destinos == "4":
            print("\nSeleccionó: Mostrar destinos con filtros.")
            print("1. Listar todos")
            print("2. Buscar por ID")
            print("3. Filtrar por ciudad")
            print("4. Filtrar por país")
            
            filtro = input("Seleccione una opción: ")
            if filtro == "1":
                mostrar_destinos()
            elif filtro == "2":
                id_destino = input("Ingrese ID: ")
                mostrar_destinos(filtro="id", valor=id_destino)
            elif filtro == "3":
                ciudad = input("Ingrese Ciudad (o parte de ella): ")
                mostrar_destinos(filtro="ciudad", valor=ciudad)
            elif filtro == "4":
                pais = input("Ingrese País (o parte de él): ")
                mostrar_destinos(filtro="pais", valor=pais)
            else:
                print(" Opción inválida.")

        elif opcion_destinos == "5":
            print("\nVolviendo al menú principal...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")
def agregar_destino(ciudad, pais, costo):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    if not es_costo_valido(costo):
        print(" Error: El costo ingresado no es válido.")

def mostrar_destinos(filtro=None, valor=None):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return
    try:
        cursor = conexion.cursor()
        if filtro == "id":
            sql = "SELECT * FROM destinos WHERE id = %s"
            cursor.execute(sql, (valor,))
        elif filtro == "ciudad":
            sql = "SELECT * FROM destinos WHERE ciudad LIKE %s"
            cursor.execute(sql, (f"%{valor}%",))
        elif filtro == "pais":
            sql = "SELECT * FROM destinos WHERE pais LIKE %s"
            cursor.execute(sql, (f"%{valor}%",))
        else:
            sql = "SELECT * FROM destinos"
            cursor.execute(sql)
        resultados = cursor.fetchall()
        if resultados:
            print("\nLista de destinos:")
            for destino in resultados:
                print(f"ID: {destino[0]}, Ciudad: {destino[1]}, País: {destino[2]}, Costo: {destino[3]}")
        else:
            print("No se encontraron destinos con ese filtro.")
    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()

def modificar_destino(id_destino, ciudad, pais, costo):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    if not es_costo_valido(costo):
        print(" Error: El costo ingresado no es válido.")
        return

    try:
        cursor = conexion.cursor()
        sql = "UPDATE destinos SET ciudad = %s, pais = %s, costo = %s WHERE id = %s"
        cursor.execute(sql, (ciudad, pais, costo, id_destino))
        conexion.commit()
        if cursor.rowcount > 0:
            print(" Destino modificado correctamente.")
        else:
            print(" No se encontró un destino con ese ID.")
    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()

def destino_existe(id_destino, conexion):
    """Verifica si el destino ya está registrado en la base de datos."""
    cursor = conexion.cursor()
    sql = "SELECT COUNT(*) FROM destinos WHERE id = %s"
    cursor.execute(sql, (id_destino,))
    resultado = cursor.fetchone()[0]
    cursor.close()
    return resultado > 0  # Retorna True si el destino ya existe

def eliminar_destino(id_destino):
    """Elimina un destino de la base de datos por su ID."""
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM destinos WHERE id = %s"
        cursor.execute(sql, (id_destino,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(" Destino eliminado correctamente.")
        else:
            print(" No se encontró un destino con ese ID.")
    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()

def es_costo_valido(costo):
    """Verifica si el costo ingresado es un número positivo."""
    try:
        valor = float(costo)
        return valor > 0
    except (ValueError, TypeError):
        return False

def agregar_destino(ciudad, pais, costo):
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    if not es_costo_valido(costo):
        print(" Error: El costo ingresado no es válido.")
        return

    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO destinos (ciudad, pais, costo) VALUES (%s, %s, %s)"
        cursor.execute(sql, (ciudad, pais, costo))
        conexion.commit()
        print(" Destino agregado correctamente.")

        print("\nDestino ingresado:")
        print(f"• Ciudad: {ciudad}")
        print(f"• País: {pais}")
        print(f"• Costo: {costo}")

    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()
