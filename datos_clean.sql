USE sistema_estetica;

INSERT INTO usuario (nombre_usuario, contrasena, correo, rol, estado) VALUES
('juan.perez', '123456', 'juan@email.com', 'cliente', 'activo'),
('maria.gomez', '123456', 'maria@email.com', 'cliente', 'activo'),
('carlos.lopez', '123456', 'carlos@email.com', 'cliente', 'activo'),
('ana.martinez', '123456', 'ana@email.com', 'empleado', 'activo'),
('luis.rodriguez', '123456', 'luis@email.com', 'empleado', 'activo'),
('laura.fernandez', '123456', 'laura@email.com', 'empleado', 'activo');

INSERT INTO cliente (id_usuario, nombre, apellido, telefono, direccion) VALUES
(1, 'Juan', 'Perez', '3111234567', 'Calle 123'),
(2, 'Maria', 'Gomez', '3109876543', 'Carrera 89'),
(3, 'Carlos', 'Lopez', '3004567890', 'Avenida 123');

INSERT INTO empleado (id_usuario, nombre, apellido, telefono, cargo, especialidad) VALUES
(4, 'Ana', 'Martinez', '3151234567', 'Estilista Senior', 'Corte'),
(5, 'Luis', 'Rodriguez', '3149876543', 'Especialista', 'Manicure'),
(6, 'Laura', 'Fernandez', '3124567890', 'Maquilladora', 'Maquillaje');

INSERT INTO servicio (nombre_servicio, descripcion, precio, duracion_aprox) VALUES
('Corte de cabello hombre', 'Corte basico', 35000, 30),
('Corte de cabello mujer', 'Corte con lavado', 45000, 45),
('Manicure basico', 'Limpieza y esmaltado', 25000, 30),
('Pedicure basico', 'Limpieza y esmaltado', 35000, 40),
('Maquillaje social', 'Maquillaje para eventos', 80000, 60),
('Peinado', 'Peinado con plancha', 50000, 45),
('Tinte de cabello', 'Tinte completo', 120000, 90),
('Alisado', 'Alisado con keratina', 150000, 120);

INSERT INTO cita (id_cliente, id_empleado, fecha, hora, estado) VALUES
(1, 1, '2026-03-27', '09:00:00', 'confirmada'),
(2, 2, '2026-03-27', '10:30:00', 'confirmada'),
(3, 1, '2026-03-27', '14:00:00', 'pendiente'),
(1, 3, '2026-03-28', '11:00:00', 'pendiente'),
(2, 2, '2026-03-28', '15:30:00', 'cancelada'),
(3, 1, '2026-03-29', '09:30:00', 'confirmada');

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

INSERT INTO factura (id_cita, fecha, total, estado) VALUES
(1, '2026-03-27', 60000, 'pagada'),
(2, '2026-03-27', 95000, 'pagada'),
(3, '2026-03-27', 60000, 'pendiente'),
(4, '2026-03-28', 130000, 'pendiente'),
(6, '2026-03-29', 120000, 'pagada');

INSERT INTO proveedor (nombre_proveedor, telefono, correo, direccion) VALUES
('Distribuidora Capilar', '3157894561', 'ventas@capilar.com', 'Calle 45'),
('Cosmeticos Bella Vista', '3104567892', 'contacto@bellavista.com', 'Carrera 78'),
('Proveedores Union', '3117894563', 'pedidos@union.com', 'Avenida 123'),
('Insumos de Belleza', '3124567894', 'ventas@belleza.com', 'Calle 12');