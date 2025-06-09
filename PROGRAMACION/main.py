# ***************************************************
# Archivo: main.py
# Sistema: SkyRoute - Sistema de Gestión de Pasajes
# Propósito del sistema:
#   Este programa permite gestionar clientes, destinos y ventas de pasajes.
#   Facilita el registro, consulta y modificación de datos de manera interactiva.
# Integrantes del grupo:
#   - Paola Garcia (DNI: 29463402)
#   - Pablo Taborda (DNI: 28270596)
#   - Julio Orjindo (DNI: 26482639)
# ***************************************************
print("\n***************************************************")
print("¡Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes!")
print("Software gestionado por TRIOSOFT SOLUTION SAS")
print("***************************************************\n")

# Bucle principal del sistema
def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Gestión de Clientes")
        print("2. Gestión de Destinos")
        print("3. Gestión de Ventas")
        print("4. Acerca del Sistema")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        from gestion_clientes import menu_clientes
        from gestion_destinos import menu_destinos
        from gestion_ventas import menu_ventas
        if opcion == "1":
            print("\nAccediendo a Gestión de Clientes...")
            menu_clientes() # Abre menu clientes en modulo gestion_clientes
        elif opcion == "2":
            print("\nAccediendo a Gestión de Destinos...")
            menu_destinos() # Abre menu destinos en modulo gestion_destinos
        elif opcion == "3":
            print("\nAccediendo a Gestión de Ventas...")
            menu_ventas() # Abre menu ventas
        elif opcion == "4":
                    print("\nAcerca del Sistema:")
                    print("Este sistema fue desarrollado por TRIOSOFT SOLUTION SAS.")
                    print("Este software gestiona clientes, destinos y ventas para SkyRoute S.R.L.")
                    print("Versión 1.1 - año 2025 - TODOS LOS DERECHOS RESERVADOS")
                    print("Prototipo funcional con estructuración clara.")
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")

# Iniciar el programa
menu_principal()
