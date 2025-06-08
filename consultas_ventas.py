from conexion_base_datos import conectar_bd

def menu_consultas_ventas():
    while True:
        print("\nMenú de Consultas de Ventas:")
        print("1. Filtrar ventas por Cliente, Destino o Estado")
        print("2. Ventas anuladas mediante el botón de arrepentimiento")
        print("3. Reporte general de ingresos")
        print("4. Ventas activas")
        print("5. Volver al menú de Ventas")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            filtrar_ventas()
        elif opcion == "2":
            consultar_ventas_anuladas_arrepentimiento()
        elif opcion == "3":
            generar_reporte_ingresos()
        elif opcion == "4":
            mostrar_ventas_activas()
        elif opcion == "5":
            print("\nVolviendo al menú de Ventas...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

def filtrar_ventas():
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    print("\n Filtrar Ventas:")
    print("1. Buscar por cuit de Cliente")
    print("2. Buscar por ID de Destino")
    print("3. Buscar por Estado de Venta")

    opcion_filtro = input("Seleccione una opción: ")

    try:
        cursor = conexion.cursor(dictionary=True)

        if opcion_filtro == "1":
            cuit_cliente = input("Ingrese cuit del Cliente: ")
            sql = "SELECT * FROM ventas WHERE cuit_cliente = %s"
            cursor.execute(sql, (cuit_cliente,))
        elif opcion_filtro == "2":
            id_destino = input("Ingrese ID de Destino: ")
            sql = "SELECT * FROM ventas WHERE id_destino = %s"
            cursor.execute(sql, (id_destino,))
        elif opcion_filtro == "3":
            estado = input("Ingrese Estado de la Venta (activa/anulada): ")
            sql = "SELECT * FROM ventas WHERE estado = %s"
            cursor.execute(sql, (estado,))
        else:
            print(" Opción inválida.")
            return

        resultados = cursor.fetchall()
        if resultados:
            print("\n Ventas encontradas:")
            for venta in resultados:
                print(f"• ID Venta: {venta['id']}, Cliente: {venta['cuit_cliente']}, Destino: {venta['id_destino']}, Estado: {venta['estado']}")
        else:
            print(" No se encontraron ventas con esos criterios.")

    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()
def consultar_ventas_anuladas_arrepentimiento():
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return
    
    cursor = conexion.cursor()

    #  Filtrar solo ventas anuladas mediante botón de arrepentimiento
    sql = """
        SELECT id, cuit_cliente, id_destino, fecha_viaje, fecha_registro 
        FROM ventas
        WHERE estado = 'anulada' AND tipo_anulacion = 'arrepentimiento'
    """
    cursor.execute(sql)
    ventas_anuladas = cursor.fetchall()

    print("\n Ventas anuladas mediante el botón de arrepentimiento:")
    if ventas_anuladas:
        for venta in ventas_anuladas:
            print(f"ID: {venta[0]}, CUIT Cliente: {venta[1]}, Destino: {venta[2]}, Fecha Viaje: {venta[3]}, Fecha Registro: {venta[4]}")
    else:
        print(" No hay ventas anuladas mediante arrepentimiento.")

    cursor.close()
    conexion.close()

def generar_reporte_ingresos():
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    # 🔹 Solicitar fechas al usuario con validación
    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ").strip()
    fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ").strip()

    # Verificar que las fechas no estén vacías
    if not fecha_inicio or not fecha_fin:
        print(" Error: Debe ingresar ambas fechas.")
        return

    try:
        cursor = conexion.cursor()
        sql = """
    SELECT SUM(d.costo) AS total_ingresos, 
           COUNT(v.id) AS cantidad_viajes, 
           AVG(d.costo) AS promedio_ingreso_por_viaje
    FROM ventas v
    JOIN destinos d ON v.id_destino = d.id
    WHERE v.estado = 'activa' 
    AND v.fecha_registro BETWEEN %s AND %s;
"""

        cursor.execute(sql, (fecha_inicio, fecha_fin))
        resultado = cursor.fetchone()

        if resultado and resultado[0] is not None:
            print(f"\n **Reporte de ingresos entre {fecha_inicio} y {fecha_fin}:**")
            print(f"🔹 **Total ingresos:** ${resultado[0]:,.2f}")
            print(f"🔹 **Cantidad de viajes:** {resultado[1]}")
            print(f"🔹 **Promedio de ingreso por viaje:** ${resultado[2]:,.2f}")
        else:
            print(" No se encontraron ventas activas en ese período.")

    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()

def mostrar_ventas_activas():
    conexion = conectar_bd()
    if not conexion:
        print(" Error: No se pudo conectar a la base de datos.")
        return

    try:
        cursor = conexion.cursor(dictionary=True)
        sql = "SELECT * FROM ventas WHERE estado = 'activa'"
        cursor.execute(sql)

        resultados = cursor.fetchall()
        if resultados:
            print("\n✔ Ventas activas:")
            for venta in resultados:
                print(f"• ID Venta: {venta['id']}, Cliente: {venta['cuit_cliente']}, Destino: {venta['id_destino']}, Fecha Viaje: {venta['fecha_viaje']}")
        else:
            print(" No hay ventas activas.")

    except Exception as e:
        print(f" Error SQL: {e}")
    finally:
        cursor.close()
        conexion.close()