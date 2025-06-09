#Devuelve todas las ventas anuladas con el tipo de anulación "arrepentimiento".
#Filtra la tabla ventas para mostrar solo las que fueron anuladas.
#Específicamente selecciona las ventas cuyo tipo_anulacion es 'arrepentimiento'.
SELECT id, cuit_cliente, id_destino, fecha_viaje, fecha_registro 
FROM ventas 
WHERE estado = 'anulada' 
  AND tipo_anulacion = 'arrepentimiento';