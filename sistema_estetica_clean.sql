CREATE DATABASE IF NOT EXISTS sistema_estetica;
USE sistema_estetica;

DROP TABLE IF EXISTS inventario_movimiento;
DROP TABLE IF EXISTS proveedor_item;
DROP TABLE IF EXISTS servicio_item;
DROP TABLE IF EXISTS detalle_factura;
DROP TABLE IF EXISTS pago;
DROP TABLE IF EXISTS factura;
DROP TABLE IF EXISTS detalle_cita;
DROP TABLE IF EXISTS cita;
DROP TABLE IF EXISTS horario_empleado;
DROP TABLE IF EXISTS empleado;
DROP TABLE IF EXISTS cliente;
DROP TABLE IF EXISTS servicio;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS proveedor;
DROP TABLE IF EXISTS usuario;

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    correo VARCHAR(100),
    rol VARCHAR(30),
    estado VARCHAR(20)
);

CREATE TABLE empleado (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(20),
    cargo VARCHAR(50),
    especialidad VARCHAR(100),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE horario_empleado (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    dia_semana VARCHAR(15),
    hora_inicio TIME,
    hora_fin TIME,
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(20),
    direccion VARCHAR(150),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE servicio (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servicio VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10,2),
    duracion_aprox INT
);

CREATE TABLE item (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    cantidad_stock INT,
    estado VARCHAR(20)
);

CREATE TABLE servicio_item (
    id_servicio_item INT AUTO_INCREMENT PRIMARY KEY,
    id_servicio INT,
    id_item INT,
    cantidad_usada INT,
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio),
    FOREIGN KEY (id_item) REFERENCES item(id_item)
);

CREATE TABLE cita (
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_empleado INT,
    fecha DATE,
    hora TIME,
    estado VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

CREATE TABLE detalle_cita (
    id_detallecita INT AUTO_INCREMENT PRIMARY KEY,
    id_cita INT,
    id_servicio INT,
    precio_servicio DECIMAL(10,2),
    FOREIGN KEY (id_cita) REFERENCES cita(id_cita),
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio)
);

CREATE TABLE factura (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cita INT,
    fecha DATE,
    total DECIMAL(10,2),
    estado VARCHAR(20),
    FOREIGN KEY (id_cita) REFERENCES cita(id_cita)
);

CREATE TABLE detalle_factura (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_factura INT,
    id_servicio INT,
    subtotal DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES factura(id_factura),
    FOREIGN KEY (id_servicio) REFERENCES servicio(id_servicio)
);

CREATE TABLE pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_factura INT,
    metodo_pago VARCHAR(50),
    fecha_pago DATE,
    monto DECIMAL(10,2),
    FOREIGN KEY (id_factura) REFERENCES factura(id_factura)
);

CREATE TABLE proveedor (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre_proveedor VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    direccion VARCHAR(150)
);

CREATE TABLE proveedor_item (
    id_prov_item INT AUTO_INCREMENT PRIMARY KEY,
    id_proveedor INT,
    id_item INT,
    precio_compra DECIMAL(10,2),
    FOREIGN KEY (id_proveedor) REFERENCES proveedor(id_proveedor),
    FOREIGN KEY (id_item) REFERENCES item(id_item)
);

CREATE TABLE inventario_movimiento (
    id_inventario INT AUTO_INCREMENT PRIMARY KEY,
    id_item INT,
    tipo VARCHAR(20),
    cantidad INT,
    fecha_actualizacion DATE,
    motivo VARCHAR(50),
    FOREIGN KEY (id_item) REFERENCES item(id_item)
);

SHOW TABLES;