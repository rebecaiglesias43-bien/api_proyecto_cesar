/*
SQLyog Community v13.3.1 (64 bit)
MySQL - 10.4.32-MariaDB : Database - sistema_estetica
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bdestetica` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `bdestetica`;

/*Table structure for table `citas` */

DROP TABLE IF EXISTS `citas`;

CREATE TABLE `citas` (
  `cit_id` int(11) NOT NULL AUTO_INCREMENT,
  `cit_cliente_id` int(11) DEFAULT NULL,
  `cit_empleado_id` int(11) DEFAULT NULL,
  `cit_fecha` date DEFAULT NULL,
  `cit_hora` time DEFAULT NULL,
  `cit_estado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cit_id`),
  KEY `cit_cliente_id` (`cit_cliente_id`),
  KEY `cit_empleado_id` (`cit_empleado_id`),
  CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`cit_cliente_id`) REFERENCES `clientes` (`cli_id`),
  CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`cit_empleado_id`) REFERENCES `empleados` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `citas` */

insert  into `citas`(`cit_id`,`cit_cliente_id`,`cit_empleado_id`,`cit_fecha`,`cit_hora`,`cit_estado`) values 
(1,1,1,'2026-04-01','10:00:00','pendiente');

/*Table structure for table `clientes` */

DROP TABLE IF EXISTS `clientes`;

CREATE TABLE `clientes` (
  `cli_id` int(11) NOT NULL AUTO_INCREMENT,
  `cli_usuario_id` int(11) DEFAULT NULL,
  `cli_nombre` varchar(50) DEFAULT NULL,
  `cli_apellido` varchar(50) DEFAULT NULL,
  `cli_telefono` varchar(20) DEFAULT NULL,
  `cli_direccion` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`cli_id`),
  UNIQUE KEY `cli_usuario_id` (`cli_usuario_id`),
  CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`cli_usuario_id`) REFERENCES `usuarios` (`usu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `clientes` */

insert  into `clientes`(`cli_id`,`cli_usuario_id`,`cli_nombre`,`cli_apellido`,`cli_telefono`,`cli_direccion`) values 
(1,2,'Juan','Perez','3009876543','Calle 123');

/*Table structure for table `detalle_citas` */

DROP TABLE IF EXISTS `detalle_citas`;

CREATE TABLE `detalle_citas` (
  `dci_id` int(11) NOT NULL AUTO_INCREMENT,
  `dci_cita_id` int(11) DEFAULT NULL,
  `dci_servicio_id` int(11) DEFAULT NULL,
  `dci_precio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`dci_id`),
  KEY `dci_cita_id` (`dci_cita_id`),
  KEY `dci_servicio_id` (`dci_servicio_id`),
  CONSTRAINT `detalle_citas_ibfk_1` FOREIGN KEY (`dci_cita_id`) REFERENCES `citas` (`cit_id`),
  CONSTRAINT `detalle_citas_ibfk_2` FOREIGN KEY (`dci_servicio_id`) REFERENCES `servicios` (`ser_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `detalle_citas` */

insert  into `detalle_citas`(`dci_id`,`dci_cita_id`,`dci_servicio_id`,`dci_precio`) values 
(1,1,1,20000.00);

/*Table structure for table `detalle_facturas` */

DROP TABLE IF EXISTS `detalle_facturas`;

CREATE TABLE `detalle_facturas` (
  `dfa_id` int(11) NOT NULL AUTO_INCREMENT,
  `dfa_factura_id` int(11) DEFAULT NULL,
  `dfa_servicio_id` int(11) DEFAULT NULL,
  `dfa_subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`dfa_id`),
  KEY `dfa_factura_id` (`dfa_factura_id`),
  KEY `dfa_servicio_id` (`dfa_servicio_id`),
  CONSTRAINT `detalle_facturas_ibfk_1` FOREIGN KEY (`dfa_factura_id`) REFERENCES `facturas` (`fac_id`),
  CONSTRAINT `detalle_facturas_ibfk_2` FOREIGN KEY (`dfa_servicio_id`) REFERENCES `servicios` (`ser_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `detalle_facturas` */

insert  into `detalle_facturas`(`dfa_id`,`dfa_factura_id`,`dfa_servicio_id`,`dfa_subtotal`) values 
(1,1,1,20000.00);

/*Table structure for table `empleados` */

DROP TABLE IF EXISTS `empleados`;

CREATE TABLE `empleados` (
  `emp_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_usuario_id` int(11) DEFAULT NULL,
  `emp_nombre` varchar(50) DEFAULT NULL,
  `emp_apellido` varchar(50) DEFAULT NULL,
  `emp_telefono` varchar(20) DEFAULT NULL,
  `emp_cargo` varchar(50) DEFAULT NULL,
  `emp_especialidad` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  UNIQUE KEY `emp_usuario_id` (`emp_usuario_id`),
  CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`emp_usuario_id`) REFERENCES `usuarios` (`usu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `empleados` */

insert  into `empleados`(`emp_id`,`emp_usuario_id`,`emp_nombre`,`emp_apellido`,`emp_telefono`,`emp_cargo`,`emp_especialidad`) values 
(1,1,'Ana','Lopez','3001234567','Estilista','Corte y peinado'),
(3,2,'Juan','Perez','3009876543','Asistente','Recepcion'),
(10,3,'Laura','Martinez','3009998888','Recepcionista','Atencion al cliente');

/*Table structure for table `facturas` */

DROP TABLE IF EXISTS `facturas`;

CREATE TABLE `facturas` (
  `fac_id` int(11) NOT NULL AUTO_INCREMENT,
  `fac_cita_id` int(11) DEFAULT NULL,
  `fac_fecha` date DEFAULT NULL,
  `fac_total` decimal(10,2) DEFAULT NULL,
  `fac_estado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`fac_id`),
  KEY `fac_cita_id` (`fac_cita_id`),
  CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`fac_cita_id`) REFERENCES `citas` (`cit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `facturas` */

insert  into `facturas`(`fac_id`,`fac_cita_id`,`fac_fecha`,`fac_total`,`fac_estado`) values 
(1,1,'2026-04-01',20000.00,'pagado');

/*Table structure for table `horarios` */

DROP TABLE IF EXISTS `horarios`;

CREATE TABLE `horarios` (
  `hor_id` int(11) NOT NULL AUTO_INCREMENT,
  `hor_empleado_id` int(11) DEFAULT NULL,
  `hor_dia_semana` varchar(15) DEFAULT NULL,
  `hor_hora_inicio` time DEFAULT NULL,
  `hor_hora_fin` time DEFAULT NULL,
  PRIMARY KEY (`hor_id`),
  KEY `hor_empleado_id` (`hor_empleado_id`),
  CONSTRAINT `horarios_ibfk_1` FOREIGN KEY (`hor_empleado_id`) REFERENCES `empleados` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `horarios` */

insert  into `horarios`(`hor_id`,`hor_empleado_id`,`hor_dia_semana`,`hor_hora_inicio`,`hor_hora_fin`) values 
(1,3,'Lunes','09:00:00','17:00:00');

/*Table structure for table `inventario_movimientos` */

DROP TABLE IF EXISTS `inventario_movimientos`;

CREATE TABLE `inventario_movimientos` (
  `inm_id` int(11) NOT NULL AUTO_INCREMENT,
  `inm_producto_id` int(11) DEFAULT NULL,
  `inm_tipo` varchar(20) DEFAULT NULL,
  `inm_cantidad` int(11) DEFAULT NULL,
  `inm_fecha` date DEFAULT NULL,
  `inm_motivo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`inm_id`),
  KEY `inm_producto_id` (`inm_producto_id`),
  CONSTRAINT `inventario_movimientos_ibfk_1` FOREIGN KEY (`inm_producto_id`) REFERENCES `productos` (`pro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `inventario_movimientos` */

/*Table structure for table `pagos` */

DROP TABLE IF EXISTS `pagos`;

CREATE TABLE `pagos` (
  `pag_id` int(11) NOT NULL AUTO_INCREMENT,
  `pag_factura_id` int(11) DEFAULT NULL,
  `pag_metodo` varchar(50) DEFAULT NULL,
  `pag_fecha` date DEFAULT NULL,
  `pag_monto` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`pag_id`),
  KEY `pag_factura_id` (`pag_factura_id`),
  CONSTRAINT `pagos_ibfk_1` FOREIGN KEY (`pag_factura_id`) REFERENCES `facturas` (`fac_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `pagos` */

insert  into `pagos`(`pag_id`,`pag_factura_id`,`pag_metodo`,`pag_fecha`,`pag_monto`) values 
(1,1,'Efectivo','2026-04-02',20000.00);

/*Table structure for table `productos` */

DROP TABLE IF EXISTS `productos`;

CREATE TABLE `productos` (
  `pro_id` int(11) NOT NULL AUTO_INCREMENT,
  `pro_nombre` varchar(100) DEFAULT NULL,
  `pro_precio` decimal(10,2) DEFAULT NULL,
  `pro_stock` int(11) DEFAULT NULL,
  `pro_estado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`pro_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `productos` */

insert  into `productos`(`pro_id`,`pro_nombre`,`pro_precio`,`pro_stock`,`pro_estado`) values 
(1,'Shampoo',10000.00,50,'activo'),
(2,'Esmalte',5000.00,100,'activo');

/*Table structure for table `proveedores` */

DROP TABLE IF EXISTS `proveedores`;

CREATE TABLE `proveedores` (
  `prv_id` int(11) NOT NULL AUTO_INCREMENT,
  `prv_nombre` varchar(100) DEFAULT NULL,
  `prv_telefono` varchar(20) DEFAULT NULL,
  `prv_email` varchar(100) DEFAULT NULL,
  `prv_direccion` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`prv_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `proveedores` */

insert  into `proveedores`(`prv_id`,`prv_nombre`,`prv_telefono`,`prv_email`,`prv_direccion`) values 
(1,'Distribuidora Bella','3005556666','ventas@bellacosmetics.com','Calle 50 #20-30');

/*Table structure for table `proveedores_productos` */

DROP TABLE IF EXISTS `proveedores_productos`;

CREATE TABLE `proveedores_productos` (
  `ppr_id` int(11) NOT NULL AUTO_INCREMENT,
  `ppr_proveedor_id` int(11) DEFAULT NULL,
  `ppr_producto_id` int(11) DEFAULT NULL,
  `ppr_precio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ppr_id`),
  KEY `ppr_proveedor_id` (`ppr_proveedor_id`),
  KEY `ppr_producto_id` (`ppr_producto_id`),
  CONSTRAINT `proveedores_productos_ibfk_1` FOREIGN KEY (`ppr_proveedor_id`) REFERENCES `proveedores` (`prv_id`),
  CONSTRAINT `proveedores_productos_ibfk_2` FOREIGN KEY (`ppr_producto_id`) REFERENCES `productos` (`pro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `proveedores_productos` */

/*Table structure for table `servicios` */

DROP TABLE IF EXISTS `servicios`;

CREATE TABLE `servicios` (
  `ser_id` int(11) NOT NULL AUTO_INCREMENT,
  `ser_nombre` varchar(100) DEFAULT NULL,
  `ser_descripcion` text DEFAULT NULL,
  `ser_precio` decimal(10,2) DEFAULT NULL,
  `ser_duracion` int(11) DEFAULT NULL,
  PRIMARY KEY (`ser_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `servicios` */

insert  into `servicios`(`ser_id`,`ser_nombre`,`ser_descripcion`,`ser_precio`,`ser_duracion`) values 
(1,'Corte de cabello','Corte basico',20000.00,30),
(2,'Manicure','Servicio de unas',15000.00,45),
(3,'Manicure','Servicio de unas',15000.00,30);

/*Table structure for table `servicios_productos` */

DROP TABLE IF EXISTS `servicios_productos`;

CREATE TABLE `servicios_productos` (
  `sep_id` int(11) NOT NULL AUTO_INCREMENT,
  `sep_servicio_id` int(11) DEFAULT NULL,
  `sep_producto_id` int(11) DEFAULT NULL,
  `sep_cantidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`sep_id`),
  KEY `sep_servicio_id` (`sep_servicio_id`),
  KEY `sep_producto_id` (`sep_producto_id`),
  CONSTRAINT `servicios_productos_ibfk_1` FOREIGN KEY (`sep_servicio_id`) REFERENCES `servicios` (`ser_id`),
  CONSTRAINT `servicios_productos_ibfk_2` FOREIGN KEY (`sep_producto_id`) REFERENCES `productos` (`pro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `servicios_productos` */

/*Table structure for table `usuarios` */

DROP TABLE IF EXISTS `usuarios`;

CREATE TABLE `usuarios` (
  `usu_id` int(11) NOT NULL AUTO_INCREMENT,
  `usu_username` varchar(50) NOT NULL,
  `usu_password` varchar(255) NOT NULL,
  `usu_email` varchar(100) DEFAULT NULL,
  `usu_rol` varchar(30) DEFAULT NULL,
  `usu_estado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`usu_id`),
  UNIQUE KEY `usu_username` (`usu_username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `usuarios` */

insert  into `usuarios`(`usu_id`,`usu_username`,`usu_password`,`usu_email`,`usu_rol`,`usu_estado`) values 
(1,'admin','123456','admin@test.com','admin','activo'),
(2,'cliente1','123456','cliente@test.com','cliente','activo'),
(3,'laura_m','123456','laura@estetica.com','empleado','activo');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
