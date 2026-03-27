CREATE DATABASE sistema_estetica;
USE sistema_estetica;

-- =========================
-- USUARIO
-- =========================
CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    correo VARCHAR(100),
    rol VARCHAR(30),
    estado VARCHAR(20)
);

-- =========================
-- EMPLEADO
-- =========================
CREATE TABLE empleado (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(20),
    cargo VARCHAR(50),
    especialidad VARCHAR(100),

    FOREIGN KEY (id_usuario)
    REFERENCES usuario(id_usuario)
);

-- =========================
-- HORARIO EMPLEADO
-- =========================
CREATE TABLE horario_empleado (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    dia_semana VARCHAR(15),
    hora_inicio TIME,
    hora_fin TIME,

    FOREIGN KEY (id_empleado)
    REFERENCES empleado(id_empleado)
);

-- =========================
-- CLIENTE
-- =========================
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT UNIQUE,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    telefono VARCHAR(20),
    direccion VARCHAR(150),

    FOREIGN KEY (id_usuario)
    REFERENCES usuario(id_usuario)
);

-- =========================
-- SERVICIO
-- =========================
CREATE TABLE servicio (
    id_servicio INT AUTO_INCREMENT PRIMARY KEY,
    nombre_servicio VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10,2),
    duracion_aprox INT
);

-- =========================
-- ITEM (PRODUCTOS)
-- =========================
CREATE TABLE item (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    cantidad_stock INT,
    estado VARCHAR(20)
);

-- =========================
-- RELACIÓN N:M
-- SERVICIO - ITEM
-- =========================
CREATE TABLE servicio_item (
    id_servicio_item INT AUTO_INCREMENT PRIMARY KEY,
    id_servicio INT,
    id_item INT,
    cantidad_usada INT,

    FOREIGN KEY (id_servicio)
    REFERENCES servicio(id_servicio),

    FOREIGN KEY (id_item)
    REFERENCES item(id_item)
);

-- =========================
-- CITA
-- =========================
CREATE TABLE cita (
    id_cita INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_empleado INT,
    fecha DATE,
    hora TIME,
    estado VARCHAR(20),

    FOREIGN KEY (id_cliente)
    REFERENCES cliente(id_cliente),

    FOREIGN KEY (id_empleado)
    REFERENCES empleado(id_empleado)
);

-- =========================
-- DETALLE CITA
-- =========================
CREATE TABLE detalle_cita (
    id_detallecita INT AUTO_INCREMENT PRIMARY KEY,
    id_cita INT,
    id_servicio INT,
    precio_servicio DECIMAL(10,2),

    FOREIGN KEY (id_cita)
    REFERENCES cita(id_cita),

    FOREIGN KEY (id_servicio)
    REFERENCES servicio(id_servicio)
);

-- =========================
-- FACTURA
-- =========================
CREATE TABLE factura (
    id_factura INT AUTO_INCREMENT PRIMARY KEY,
    id_cita INT,
    fecha DATE,
    total DECIMAL(10,2),
    estado VARCHAR(20),

    FOREIGN KEY (id_cita)
    REFERENCES cita(id_cita)
);

-- =========================
-- DETALLE FACTURA
-- =========================
CREATE TABLE detalle_factura (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_factura INT,
    id_servicio INT,
    subtotal DECIMAL(10,2),

    FOREIGN KEY (id_factura)
    REFERENCES factura(id_factura),

    FOREIGN KEY (id_servicio)
    REFERENCES servicio(id_servicio)
);

-- =========================
-- PAGO
-- =========================
CREATE TABLE pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    id_factura INT,
    metodo_pago VARCHAR(50),
    fecha_pago DATE,
    monto DECIMAL(10,2),

    FOREIGN KEY (id_factura)
    REFERENCES factura(id_factura)
);

-- =========================
-- PROVEEDOR
-- =========================
CREATE TABLE proveedor (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre_proveedor VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    direccion VARCHAR(150)
);

-- =========================
-- PROVEEDOR ITEM
-- =========================
CREATE TABLE proveedor_item (
    id_prov_item INT AUTO_INCREMENT PRIMARY KEY,
    id_proveedor INT,
    id_item INT,
    precio_compra DECIMAL(10,2),

    FOREIGN KEY (id_proveedor)
    REFERENCES proveedor(id_proveedor),

    FOREIGN KEY (id_item)
    REFERENCES item(id_item)
);

-- =========================
-- INVENTARIO MOVIMIENTO
-- =========================
CREATE TABLE inventario_movimiento (
    id_inventario INT AUTO_INCREMENT PRIMARY KEY,
    id_item INT,
    tipo VARCHAR(20),
    cantidad INT,
    fecha_actualizacion DATE,
    motivo VARCHAR(50),

    FOREIGN KEY (id_item)
    REFERENCES item(id_item)
);