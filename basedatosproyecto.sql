CREATE DATABASE IF NOT EXISTS proyectosena_bd;
USE proyectosena_bd;

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT PRIMARY KEY,
    nombre_usuario VARCHAR(100),
    correo VARCHAR(150),
    contrasena VARCHAR(255),
    rol VARCHAR(50),
    estado VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(200),
    id_usuarioFK INT,
    FOREIGN KEY (id_usuarioFK) REFERENCES usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS empleado (
    id_empleadoPK INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    telefono VARCHAR(20),
    especialidad VARCHAR(100),
    cargo VARCHAR(50),
    id_usuarioFK INT,
    FOREIGN KEY (id_usuarioFK) REFERENCES usuario(id_usuario)
);

CREATE TABLE IF NOT EXISTS servicio (
    id_servicioPK INT PRIMARY KEY,
    nombre_servicio VARCHAR(100),
    precio DECIMAL(10, 2),
    descripcion TEXT,
    duracion_aprox VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS cita (
    id_citaPK INT PRIMARY KEY,
    fecha DATE,
    hora TIME,
    estado VARCHAR(20),
    id_clienteFK INT,
    id_empleadoFK INT,
    FOREIGN KEY (id_clienteFK) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_empleadoFK) REFERENCES empleado(id_empleadoPK)
);

CREATE TABLE IF NOT EXISTS detalle_cita (
    id_detallecitaPK INT PRIMARY KEY,
    id_citaFK INT,
    id_servicioFK INT,
    precio_servicio DECIMAL(10, 2),
    FOREIGN KEY (id_citaFK) REFERENCES cita(id_citaPK),
    FOREIGN KEY (id_servicioFK) REFERENCES servicio(id_servicioPK)
);

CREATE TABLE IF NOT EXISTS factura (
    id_factura INT PRIMARY KEY,
    id_citaFK INT,
    total DECIMAL(10, 2),
    fecha_emision DATETIME,
    FOREIGN KEY (id_citaFK) REFERENCES cita(id_citaPK)
);

CREATE TABLE IF NOT EXISTS detalle_factura (
    id_detallefactura INT PRIMARY KEY,
    id_facturaFK INT,
    id_servicioFK INT,
    cantidad INT DEFAULT 1,
    precio_unitario DECIMAL(10, 2),
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (id_facturaFK) REFERENCES factura(id_factura),
    FOREIGN KEY (id_servicioFK) REFERENCES servicio(id_servicioPK)
);

CREATE TABLE IF NOT EXISTS pago (
    id_pago INT PRIMARY KEY,
    id_facturaFK INT,
    monto DECIMAL(10, 2),
    metodo_pago VARCHAR(50),
    FOREIGN KEY (id_facturaFK) REFERENCES factura(id_factura)
);

CREATE TABLE IF NOT EXISTS item (
    id_item INT PRIMARY KEY,
    nombre VARCHAR(100),
    stock_actual INT,
    precio_unidad DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS proveedor (
    id_proveedor INT PRIMARY KEY,
    nombre_contacto VARCHAR(100),
    empresa VARCHAR(100),
    telefono VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS proveedor_item (
    id_proveedorFK INT,
    id_itemFK INT,
    PRIMARY KEY (id_proveedorFK, id_itemFK),
    FOREIGN KEY (id_proveedorFK) REFERENCES proveedor(id_proveedor),
    FOREIGN KEY (id_itemFK) REFERENCES item(id_item)
);

CREATE TABLE IF NOT EXISTS inventario_movimiento (
    id_movimiento INT PRIMARY KEY,
    id_itemFK INT,
    tipo_movimiento VARCHAR(50),
    cantidad INT,
    fecha_movimiento DATETIME,
    FOREIGN KEY (id_itemFK) REFERENCES item(id_item)
);