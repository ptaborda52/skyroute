#Esta consulta obtiene la última venta de cada cliente y su fecha de registro.
#Utiliza MAX(fecha_registro) para obtener la última venta de cada cliente.
#Se filtra cada venta comparando con su cliente (id_cliente), asegurando que solo se seleccione la última.
SELECT v.cuit_cliente, v.id AS id_venta, v.fecha_registro
FROM ventas v
WHERE v.fecha_registro = (
    SELECT MAX(v2.fecha_registro)
    FROM ventas v2
    WHERE v2.cuit_cliente = v.cuit_cliente
);