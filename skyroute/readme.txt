 Integrantes del grupo:
   - Paola Garcia (DNI: 29463402) paosuga14
   - Pablo Taborda (DNI: 28270596) ptaborda52
   - Julio Orjindo (DNI: 26482639)

# ***********************************************************************************
# Sistema: SkyRoute - Sistema de Gestión de Pasajes
# Propósito del sistema. (V1.1 Prototipo funcional): 
#   Este programa permite gestionar clientes, destinos y ventas de pasajes.
#   Facilitar el registro, consulta y modificación de datos de manera interactiva.
#
# Cómo ejecutar el programa:
#   - nstalar Python
#	Si aún no lo tienes, descarga e instala la última versión desde python.org.
# 	Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
#   - Verificar instalación
#	Abre una terminal (CMD, PowerShell o Terminal en macOS/Linux) y ejecuta:
#	"python --version"
#	Esto debe mostrar la versión instalada. Si ves un error, revisa si Python 
#	está correctamente agregado a las variables de entorno.
#   - Instalar MySQL ("https://www.mysql.com/downloads/")
#   - Navegar hasta la ubicación del archivo `main.py`.
#   - Ejecutar el programa con el siguiente comando:
#     python main.py
#   - Abrir MySQL de la siguiente forma: "mysql -u root -p" e ingresar la contraseña
#	(en ps o smd)
#   - Ejecutar los comandos del archivo: "query" para estructurar la base de datos.-
# ***********************************************************************************
	Este sistema fue desarrollado por TRIOSOFT SOLUTION SAS
	Este software gestiona clientes, destinos y ventas para SkyRoute S.R.L.
	Versión 1.1 - año 2025 - TODOS LOS DERECHOS RESERVADOS
AYUDA
Menú Principal:			
1. Gestión de Clientes			
	Menú Clientes:		
	1. Agregar cliente		
		Ingrese cuit	
		Ingrese Razón Social	
		Ingrese Email	
	2. Modificar cliente		
		Nueva Razón Social:	
		Nuevo Email:	
	3. Eliminar cliente		
		cuit:	
	4. Mostrar clientes		
		1. Listar todos	
		2. Buscar por cuit	
		3. Filtrar por razón social	
		4. Filtrar por email	
	5. Volver al menú principal		
2. Gestión de Destinos			
	1. Agregar destino		
		Ciudad: 	
		País: 	
		Costo: 	
	2. Modificar destino		
		Ciudad: 	
		País: 	
		Costo: 	
	3. Eliminar destino		
		Id del Destino	
	4. Mostrar destinos		
		1. Listar todos	
		2. Buscar por ID	
		3. Filtrar por ciudad	
		4. Filtrar por país	
	5. Volver al menú principal		
3. Gestión de Ventas			
	1. Registrar venta		
		cuit del Cliente:	
		ID del Destino: 	
		Fecha del Viaje (dd/mm/aaaa): 	
	2. Modificar venta		
		Id:	
		cuit:	
		ID del Destino: 	
		Fecha del Viaje (dd/mm/aaaa): 	
	3. Botón de arrepentimiento o Anular una venta		
		Id:	
			1. Administrador
			2. Botón de arrepentimiento (últimos 60 días)
	4. Consultar ventas		
		1. Filtrar ventas por Cliente, Destino o Estado	
			1. cuit:
			2. ID de Destino
			3. Estado de Venta
		2. Ventas anuladas mediante el botón de arrepentimiento	
		3. Reporte general de ingresos	
		4. Ventas activas	
		5. Volver al menú de Ventas	
	5. Volver al menú principal		
4. Acerca del Sistema			
5. Salir			


Detalle del repositorio;
conexion_base_datos.py		567	 bytes
config.py		165	 bytes
consultas_ventas.py		4942	 bytes
gestion_clientes.py		8770	 bytes
gestion_destinos.py		7392	 bytes
gestion_ventas.py		5176	 bytes
main.py		2416	 bytes
query		843	 bytes
8 archivos		30.271	 bytes



