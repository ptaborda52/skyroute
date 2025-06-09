#Esta consulta calcula los ingresos, cantidad de viajes y promedio de ingreso por viaje dentro de un rango de fechas.
#Usa SUM(d.costo) para calcular el total de ingresos dentro del período.
#Usa COUNT(v.id) para contar la cantidad de ventas registradas.
#Usa AVG(d.costo) para obtener el promedio de ingresos por venta.
#la misma consulta sirve para saber lo que sumaban las ventas anuladas reemplazando "activa" por "anulada"
#debe completar los rangos de las fechas de la cnsulta

SELECT SUM(d.costo) AS total_ingresos, 
       COUNT(v.id) AS cantidad_viajes, 
       AVG(d.costo) AS promedio_ingreso_por_viaje
FROM ventas v
JOIN destinos d ON v.id_destino = d.id
WHERE v.estado = 'activa' 
  AND v.fecha_registro BETWEEN '2025-06-08 02:53:26' AND '2025-06-08 17:59:49';