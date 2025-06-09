#Agrupa los viajes por año y mes (YEAR(fecha_viaje), MONTH(fecha_viaje)).
#Cuenta cuántos viajes se realizaron en cada mes (COUNT(v.id)).
#Ordena los resultados en orden descendente (DESC) para mostrar primero los meses con más viajes.
SELECT YEAR(v.fecha_viaje) AS año, 
       MONTH(v.fecha_viaje) AS mes, 
       COUNT(v.id) AS cantidad_viajes
FROM ventas v
WHERE v.estado = 'activa'  -- Solo contar viajes activos
GROUP BY YEAR(v.fecha_viaje), MONTH(v.fecha_viaje)
ORDER BY cantidad_viajes DESC;