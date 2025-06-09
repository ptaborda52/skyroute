#Cuenta cuántas veces cada ciudad ha sido elegida en ventas activas.
#Agrupa por d.ciudad para obtener el total de viajes por ciudad.
#Ordena los resultados en orden descendente (DESC) para mostrar primero las ciudades más elegidas.
SELECT d.ciudad AS ciudad, COUNT(v.id) AS cantidad_viajes
FROM ventas v
JOIN destinos d ON v.id_destino = d.id
WHERE v.estado = 'activa'  -- Solo contar ventas activas
GROUP BY d.ciudad
ORDER BY cantidad_viajes DESC;