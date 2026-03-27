-- ============================================
-- DATOS DE PRUEBA PARA SISTEMA_ESTETICA
-- ============================================

USE sistema_estetica;

-- ============================================
-- 1. USUARIOS
-- ============================================
INSERT INTO usuario (nombre_usuario, contraseña, correo, rol, estado) VALUES
('juan.perez', '123456', 'juan@email.com', 'cliente', 'activo'),
('maria.gomez', '123456', 'maria@email.com', 'cliente', 'activo'),
('carlos.lopez', '123456', 'carlos@email.com', 'cliente', 'activo'),
('ana.martinez', '123456', 'ana@email.com', 'empleado', 'activo'),
('luis.rodriguez', '123456', 'luis@email.com', 'empleado', 'activo'),
('laura.fernandez', '123456', 'laura@email.com', 'empleado', 'activo'),
('admin.sistema', 'admin123', 'admin@empresa.com', 'administrador', 'activo');

-- ============================================
-- 2. CLIENTES
-- ============================================
INSERT INTO cliente (id_usuario, nombre, apellido, telefono, direccion) VALUES
(1, 'Juan', 'Perez', '3111234567', 'Calle 123 #45-67, Bogota'),
(2, 'Maria', 'Gomez', '3109876543', 'Carrera 89 #12-34, Medellin'),
(3, 'Carlos', 'Lopez', '3004567890', 'Avenida Siempre Viva 123, Cali');

-- ============================================
-- 3. EMPLEADOS
-- ============================================
INSERT INTO empleado (id_usuario, nombre, apellido, telefono, cargo, especialidad) VALUES
(4, 'Ana', 'Martinez', '3151234567', 'Estilista Senior', 'Corte de cabello'),
(5, 'Luis', 'Rodriguez', '3149876543', 'Especialista', 'Manicure y Pedicure'),
(6, 'Laura', 'Fernandez', '3124567890', 'Maquilladora', 'Maquillaje');

-- ============================================
-- 4. SERVICIOS
-- ============================================
INSERT INTO servicio (nombre_servicio, descripcion, precio, duracion_aprox) VALUES
('Corte de cabello hombre', 'Corte con maquina y tijera', 35000, 30),
('Corte de cabello mujer', 'Corte, lavado y secado', 45000, 45),
('Manicure basico', 'Limpieza, corte y esmaltado', 25000, 30),
('Pedicure basico', 'Limpieza, corte y esmaltado', 35000, 40),
('Maquillaje social', 'Maquillaje para eventos', 80000, 60),
('Peinado', 'Peinado con plancha o tenaza', 50000, 45),
('Tinte de cabello', 'Tinte completo', 120000, 90),
('Alisado', 'Alisado con keratina', 150000, 120);

-- ============================================
-- 5. CITAS (con nuevos IDs automáticos)
-- ============================================
INSERT INTO cita (id_cliente, id_empleado, fecha, hora, estado) VALUES
(1, 1, '2026-03-27', '09:00:00', 'confirmada'),
(2, 2, '2026-03-27', '10:30:00', 'confirmada'),
(3, 1, '2026-03-27', '14:00:00', 'pendiente'),
(1, 3, '2026-03-28', '11:00:00', 'pendiente'),
(2, 2, '2026-03-28', '15:30:00', 'cancelada'),
(3, 1, '2026-03-29', '09:30:00', 'confirmada');

-- ============================================
-- 6. DETALLE CITAS
-- ============================================
INSERT INTO detalle_cita (id_cita, id_servicio, precio_servicio) VALUES
(1, 1, 35000),
(1, 3, 25000),
(2, 2, 45000),
(2, 6, 50000),
(3, 4, 35000),
(3, 3, 25000),
(4, 5, 80000),
(4, 6, 50000),
(5, 2, 45000),
(6, 7, 120000);

-- ============================================
-- 7. FACTURAS
-- ============================================
INSERT INTO factura (id_cita, fecha, total, estado) VALUES
(1, '2026-03-27', 60000, 'pagada'),
(2, '2026-03-27', 95000, 'pagada'),
(3, '2026-03-27', 60000, 'pendiente'),
(4, '2026-03-28', 130000, 'pendiente'),
(6, '2026-03-29', 120000, 'pagada');

-- ============================================
-- 8. DETALLE FACTURAS
-- ============================================
INSERT INTO detalle_factura (id_factura, id_servicio, subtotal) VALUES
(1, 1, 35000),
(1, 3, 25000),
(2, 2, 45000),
(2, 6, 50000),
(3, 4, 35000),
(3, 3, 25000),
(4, 5, 80000),
(4, 6, 50000),
(5, 7, 120000);

-- ============================================
-- 9. PAGOS
-- ============================================
INSERT INTO pago (id_factura, metodo_pago, fecha_pago, monto) VALUES
(1, 'Efectivo', '2026-03-27', 60000),
(2, 'Tarjeta credito', '2026-03-27', 95000),
(5, 'Efectivo', '2026-03-29', 120000);

-- ============================================
-- 10. PROVEEDORES (nueva estructura)
-- ============================================
INSERT INTO proveedor (nombre_proveedor, telefono, correo, direccion) VALUES
('Distribuidora Capilar S.A.S', '3157894561', 'ventas@capilar.com', 'Calle 45 #23-12, Bogota'),
('Cosmeticos Bella Vista', '3104567892', 'contacto@bellavista.com', 'Carrera 78 #34-56, Medellin'),
('Proveedores Union', '3117894563', 'pedidos@proveedoresunion.com', 'Avenida Principal #123, Cali'),
('Insumos de Belleza', '3124567894', 'ventas@insumosbelleza.com', 'Calle 12 #8-90, Barranquilla');

-- ============================================
-- 11. ITEMS (productos)
-- ============================================
INSERT INTO item (nombre, precio, cantidad_stock, estado) VALUES
('Shampoo profesional', 45000, 50, 'activo'),
('Acondicionador', 48000, 45, 'activo'),
('Tinte cabello negro', 35000, 30, 'activo'),
('Tinte cabello castano', 35000, 25, 'activo'),
('Esmalte rojo', 8000, 100, 'activo'),
('Esmalte rosado', 8000, 85, 'activo'),
('Keratinas', 75000, 20, 'activo'),
('Cepillos profesionales', 25000, 15, 'activo');

-- ============================================
-- 12. PROVEEDOR_ITEM (relación)
-- ============================================
INSERT INTO proveedor_item (id_proveedor, id_item, precio_compra) VALUES
(1, 1, 35000),
(1, 2, 38000),
(1, 3, 28000),
(1, 4, 28000),
(2, 5, 5000),
(2, 6, 5000),
(3, 7, 60000),
(4, 8, 18000);

-- ============================================
-- 13. SERVICIO_ITEM (relación servicio - productos)
-- ============================================
INSERT INTO servicio_item (id_servicio, id_item, cantidad_usada) VALUES
(1, 1, 1),  -- Corte hombre usa shampoo
(1, 2, 1),  -- Corte hombre usa acondicionador
(2, 1, 1),  -- Corte mujer usa shampoo
(2, 2, 1),  -- Corte mujer usa acondicionador
(3, 5, 1),  -- Manicure usa esmalte rojo
(4, 5, 1),  -- Pedicure usa esmalte rojo
(7, 3, 1),  -- Tinte usa tinte negro
(7, 4, 1);  -- Tinte usa tinte castano

-- ============================================
-- 14. INVENTARIO MOVIMIENTO
-- ============================================
INSERT INTO inventario_movimiento (id_item, tipo, cantidad, fecha_actualizacion, motivo) VALUES
(1, 'entrada', 20, '2026-03-01', 'Compra inicial'),
(2, 'entrada', 15, '2026-03-01', 'Compra inicial'),
(3, 'entrada', 10, '2026-03-01', 'Compra inicial'),
(5, 'salida', 5, '2026-03-02', 'Uso en servicios'),
(6, 'salida', 3, '2026-03-02', 'Uso en servicios'),
(1, 'salida', 2, '2026-03-03', 'Uso en servicios'),
(7, 'entrada', 5, '2026-03-04', 'Compra reposicion');

-- ============================================
-- 15. HORARIO EMPLEADOS
-- ============================================
INSERT INTO horario_empleado (id_empleado, dia_semana, hora_inicio, hora_fin) VALUES
(1, 'Lunes', '08:00:00', '17:00:00'),
(1, 'Martes', '08:00:00', '17:00:00'),
(1, 'Miercoles', '08:00:00', '17:00:00'),
(1, 'Jueves', '08:00:00', '17:00:00'),
(1, 'Viernes', '08:00:00', '17:00:00'),
(2, 'Lunes', '09:00:00', '18:00:00'),
(2, 'Martes', '09:00:00', '18:00:00'),
(2, 'Miercoles', '09:00:00', '18:00:00'),
(2, 'Jueves', '09:00:00', '18:00:00'),
(2, 'Viernes', '09:00:00', '18:00:00'),
(3, 'Martes', '10:00:00', '19:00:00'),
(3, 'Jueves', '10:00:00', '19:00:00'),
(3, 'Sabado', '09:00:00', '14:00:00');

-- ============================================
-- VERIFICAR DATOS INSERTADOS
-- ============================================
SELECT '=== VERIFICACION DE DATOS ===' as '';
SELECT 'usuario' as tabla, COUNT(*) as total FROM usuario
UNION ALL
SELECT 'cliente', COUNT(*) FROM cliente
UNION ALL
SELECT 'empleado', COUNT(*) FROM empleado
UNION ALL
SELECT 'servicio', COUNT(*) FROM servicio
UNION ALL
SELECT 'cita', COUNT(*) FROM cita
UNION ALL
SELECT 'detalle_cita', COUNT(*) FROM detalle_cita
UNION ALL
SELECT 'factura', COUNT(*) FROM factura
UNION ALL
SELECT 'detalle_factura', COUNT(*) FROM detalle_factura
UNION ALL
SELECT 'pago', COUNT(*) FROM pago
UNION ALL
SELECT 'proveedor', COUNT(*) FROM proveedor
UNION ALL
SELECT 'item', COUNT(*) FROM item
UNION ALL
SELECT 'proveedor_item', COUNT(*) FROM proveedor_item
UNION ALL
SELECT 'servicio_item', COUNT(*) FROM servicio_item
UNION ALL
SELECT 'inventario_movimiento', COUNT(*) FROM inventario_movimiento
UNION ALL
SELECT 'horario_empleado', COUNT(*) FROM horario_empleado;

-- Mostrar citas con nombres
SELECT '=== CITAS CON DATOS ===' as '';
SELECT c.id_cita, cl.nombre as cliente, e.nombre as empleado, 
       c.fecha, c.hora, c.estado
FROM cita c
JOIN cliente cl ON c.id_cliente = cl.id_cliente
JOIN empleado e ON c.id_empleado = e.id_empleado;

-- Mostrar facturas con totales
SELECT '=== FACTURAS ===' as '';
SELECT f.id_factura, cl.nombre as cliente, f.fecha, f.total, f.estado
FROM factura f
JOIN cita c ON f.id_cita = c.id_cita
JOIN cliente cl ON c.id_cliente = cl.id_cliente;

-- Mostrar proveedores
SELECT '=== PROVEEDORES ===' as '';
SELECT * FROM proveedor;