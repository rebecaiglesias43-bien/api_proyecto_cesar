-- ============================================
-- BASE DE DATOS COMPLETA SISTEMA_ESTETICA
-- CON ESTRUCTURA Y DATOS DE PRUEBA
-- ============================================

CREATE DATABASE IF NOT EXISTS sistema_estetica;
USE sistema_estetica;

-- =========================
-- USUARIO
-- =========================
CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    correo VARCHAR(100),
    rol VARCHAR(30),
    estado VARCHAR(20)
);

-- =========================
-- EMPLEADO
-- =========================
CREATE TABLE IF NOT EXISTS empleado (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(20),
    cargo VARCHAR(50),
    especialidad VARCHAR(100),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- =========================
-- HORARIO EMPLEADO
-- =========================
CREATE TABLE IF NOT EXISTS horario_empleado (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    dia_semana VARCHAR(15),
    hora_inicio TIME,
    hora_fin TIME,
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

-- =========================
-- CLIENTE
-- =========================
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(20),
    direccion VARCHAR(150),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

-- =========================
-- SERVICIO
-- =========================
CREATE TABLE IF NOT EXISTS servicio (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servicio VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10,2),
    duracion_aprox INT
);

-- =========================
-- ITEM (PRODUCTOS)
-- =========================
CREATE TABLE IF NOT EXISTS item (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    cantidad_stock INT,
    estado VARCHAR(20)
);

-- =========================
-- RELACION N:M SERVICIO - ITEM
-- =========================
CREATE TABLE IF NOT EXISTS servicio_item (
    id_servicio_item INT AUTO_INCREMENT PRIMARY KEY,
    id_servicio INT,
    id_item INT,
    cantidad_usada INT,
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio),
    FOREIGN KEY (id_item) REFERENCES item(id_item)
);

-- =========================
-- CITA
-- =========================
CREATE TABLE IF NOT EXISTS cita (
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_empleado INT,
    fecha DATE,
    hora TIME,
    estado VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

-- =========================
-- DETALLE CITA
-- =========================
CREATE TABLE IF NOT EXISTS detalle_cita (
    id_detallecita INT AUTO_INCREMENT PRIMARY KEY,
    id_cita INT,
    id_servicio INT,
    precio_servicio DECIMAL(10,2),
    FOREIGN KEY (id_cita) REFERENCES cita(id_cita),
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio)
);

-- =========================
-- FACTURA
-- =========================
CREATE TABLE IF NOT EXISTS factura (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cita INT,
    fecha DATE,
    total DECIMAL(10,2),
    estado VARCHAR(20),
    FOREIGN KEY (id_cita) REFERENCES cita(id_cita)
);

-- =========================
-- DETALLE FACTURA
-- =========================
CREATE TABLE IF NOT EXISTS detalle_factura (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_factura INT,
    id_servicio INT,
    subtotal DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES factura(id_factura),
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio)
);

-- =========================
-- PAGO
-- =========================
CREATE TABLE IF NOT EXISTS pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_factura INT,
    metodo_pago VARCHAR(50),
    fecha_pago DATE,
    monto DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES factura(id_factura)
);

-- =========================
-- PROVEEDOR
-- =========================
CREATE TABLE IF NOT EXISTS proveedor (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre_proveedor VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    direccion VARCHAR(150)
);

-- =========================
-- PROVEEDOR ITEM
-- =========================
CREATE TABLE IF NOT EXISTS proveedor_item (
    id_prov_item INT AUTO_INCREMENT PRIMARY KEY,
    id_proveedor INT,
    id_item INT,
    precio_compra DECIMAL(10,2),
    FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor),
    FOREIGN KEY (id_item) REFERENCES item(id_item)
);

-- =========================
-- INVENTARIO MOVIMIENTO
-- =========================
CREATE TABLE IF NOT EXISTS inventario_movimiento (
    id_inventario INT AUTO_INCREMENT PRIMARY KEY,
    id_item INT,
    tipo VARCHAR(20),
    cantidad INT,
    fecha_actualizacion DATE,
    motivo VARCHAR(50),
    FOREIGN KEY (id_item) REFERENCES item(id_item)
);

-- ============================================
-- DATOS DE PRUEBA
-- ============================================

-- 1. USUARIOS
INSERT INTO usuario (nombre_usuario, contrasena, correo, rol, estado) VALUES
('juan.perez', '123456', 'juan@email.com', 'cliente', 'activo'),
('maria.gomez', '123456', 'maria@email.com', 'cliente', 'activo'),
('carlos.lopez', '123456', 'carlos@email.com', 'cliente', 'activo'),
('ana.martinez', '123456', 'ana@email.com', 'empleado', 'activo'),
('luis.rodriguez', '123456', 'luis@email.com', 'empleado', 'activo'),
('admin.sistema', 'admin123', 'admin@empresa.com', 'administrador', 'activo');

-- 2. CLIENTES
INSERT INTO cliente (id_usuario, nombre, apellido, telefono, direccion) VALUES
(1, 'Juan', 'Perez', '3111234567', 'Calle 123 #45-67, Bogota'),
(2, 'Maria', 'Gomez', '3109876543', 'Carrera 89 #12-34, Medellin'),
(3, 'Carlos', 'Lopez', '3004567890', 'Avenida Siempre Viva 123, Cali');

-- 3. EMPLEADOS
INSERT INTO empleado (id_usuario, nombre, apellido, telefono, cargo, especialidad) VALUES
(4, 'Ana', 'Martinez', '3151234567', 'Estilista Senior', 'Corte de cabello'),
(5, 'Luis', 'Rodriguez', '3149876543', 'Especialista', 'Manicure y Pedicure'),
(NULL, 'Laura', 'Fernandez', '3124567890', 'Maquilladora', 'Maquillaje');

-- 4. SERVICIOS
INSERT INTO servicio (nombre_servicio, descripcion, precio, duracion_aprox) VALUES
('Corte de cabello hombre', 'Corte con maquina y tijera', 35000, 30),
('Corte de cabello mujer', 'Corte, lavado y secado', 45000, 45),
('Manicure basico', 'Limpieza, corte y esmaltado', 25000, 30),
('Pedicure basico', 'Limpieza, corte y esmaltado', 35000, 40),
('Maquillaje social', 'Maquillaje para eventos', 80000, 60),
('Peinado', 'Peinado con plancha o tenaza', 50000, 45),
('Tinte de cabello', 'Tinte completo', 120000, 90),
('Alisado', 'Alisado con keratina', 150000, 120);

-- 5. CITAS
INSERT INTO cita (id_cliente, id_empleado, fecha, hora, estado) VALUES
(1, 1, '2026-03-27', '09:00:00', 'confirmada'),
(2, 2, '2026-03-27', '10:30:00', 'confirmada'),
(3, 1, '2026-03-27', '14:00:00', 'pendiente'),
(1, 3, '2026-03-28', '11:00:00', 'pendiente'),
(2, 2, '2026-03-28', '15:30:00', 'cancelada'),
(3, 1, '2026-03-29', '09:30:00', 'confirmada');

-- 6. DETALLE CITAS
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

-- 7. FACTURAS
INSERT INTO factura (id_cita, fecha, total, estado) VALUES
(1, '2026-03-27', 60000, 'pagada'),
(2, '2026-03-27', 95000, 'pagada'),
(3, '2026-03-27', 60000, 'pendiente'),
(4, '2026-03-28', 130000, 'pendiente'),
(6, '2026-03-29', 120000, 'pagada');

-- 8. PROVEEDORES
INSERT INTO proveedor (nombre_proveedor, telefono, correo, direccion) VALUES
('Distribuidora Capilar S.A.S', '3157894561', 'ventas@capilar.com', 'Calle 45 #23-12, Bogota'),
('Cosmeticos Bella Vista', '3104567892', 'contacto@bellavista.com', 'Carrera 78 #34-56, Medellin'),
('Proveedores Union', '3117894563', 'pedidos@proveedoresunion.com', 'Avenida Principal #123, Cali'),
('Insumos de Belleza', '3124567894', 'ventas@insumosbelleza.com', 'Calle 12 #8-90, Barranquilla');

-- 9. ITEMS (PRODUCTOS)
INSERT INTO item (nombre, precio, cantidad_stock, estado) VALUES
('Shampoo profesional', 45000, 50, 'activo'),
('Acondicionador', 48000, 45, 'activo'),
('Tinte cabello negro', 35000, 30, 'activo'),
('Tinte cabello castano', 35000, 25, 'activo'),
('Esmalte rojo', 8000, 100, 'activo'),
('Esmalte rosado', 8000, 85, 'activo'),
('Keratinas', 75000, 20, 'activo'),
('Cepillos profesionales', 25000, 15, 'activo');

-- 10. VERIFICAR DATOS
SELECT '=== VERIFICACION ===' as '';
SELECT 'citas' as tabla, COUNT(*) as total FROM cita
UNION ALL
SELECT 'facturas', COUNT(*) FROM factura
UNION ALL
SELECT 'proveedores', COUNT(*) FROM proveedor
UNION ALL
SELECT 'servicios', COUNT(*) FROM servicio;