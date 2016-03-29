-- Paises

INSERT INTO `pasantiasnuevo`.`pais`
(`nombre`)
VALUES ('Venezuela');

INSERT INTO `pasantiasnuevo`.`pais`
(`nombre`)
VALUES ('U.S.A.');

-- Estados

INSERT INTO `pasantiasnuevo`.`estado`
(`nombre`,`id_pais`)
VALUES
('Distrito Capital',1);

INSERT INTO `pasantiasnuevo`.`estado`
(`nombre`,`id_pais`)
VALUES
('Miranda',1);

INSERT INTO `pasantiasnuevo`.`estado`
(`nombre`,`id_pais`)
VALUES
('Aragua',1);

INSERT INTO `pasantiasnuevo`.`estado`
(`nombre`,`id_pais`)
VALUES
('Florida',2);


-- Areas Laborales

INSERT INTO `pasantiasnuevo`.`area_laboral`
(`nombre`,`descripcion`)
VALUES
('Informatica','Consultoria, desarrollo de software,etc');

INSERT INTO `pasantiasnuevo`.`area_laboral`
(`nombre`,`descripcion`)
VALUES
('Legal','Asesoria legal, resolucion de casos');

INSERT INTO `pasantiasnuevo`.`area_laboral`
(`nombre`,`descripcion`)
VALUES
('Electricidad','Instalaciones electricas');

INSERT INTO `pasantiasnuevo`.`area_laboral`
(`nombre`,`descripcion`)
VALUES
('Arquitectura','Diseño de planos');


-- Universidades

INSERT INTO `pasantiasnuevo`.`universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad Simón Bolívar',1);

INSERT INTO `pasantiasnuevo`.`universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad Católica Andrés Bello',1);

INSERT INTO `pasantiasnuevo`.`universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad Metropolitana',1);

INSERT INTO `pasantiasnuevo`.`universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad De Florida',2);


-- Categorias

INSERT INTO `pasantiasnuevo`.`categoria`
(`nombre`)
VALUES
('Categoria Ejemplo');

-- Dedicaciones

INSERT INTO `pasantiasnuevo`.`dedicacion`
(`nombre`)
VALUES
('Dedicacion Ejemplo');

-- Divisiones

INSERT INTO `pasantiasnuevo`.`division`
(`nombre`)
VALUES
('Division Ejemplo');


-- Departamentos

INSERT INTO `pasantiasnuevo`.`departamento`
(`nombre`,
`id_division`,
`email_dep`,
`sede`)
VALUES
('Ciencias de la Informacion',
1,
'cdlais@usb.ve',
'Sartenejas');

-- Coordinaciones

INSERT INTO `pasantiasnuevo`.`coordinacion`
(`nombre`,
`usbid`,
`sede`)
VALUES
('Coordinacion De Ing. De Computacion',
'coord-comp@usb.ve',
'Sartenejas');

-- Carreras

INSERT INTO `pasantiasnuevo`.`carrera`
(`codigo`,
`nombre`,
`duracion`,
`sede`,
`coordinacion`)
VALUES
('0800',
'Ing. De Computacion',
'Larga',
'Sartenejas',
'1');

-- Tipos de Pasantias

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0100',
'Sartenejas Corta');

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0130',
'Sartenejas Mediana');

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0160',
'Sartenejas Larga');

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0190',
'Sartenejas Caso Especial');

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0200',
'Litoral Corta');

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0230',
'Litoral Mediana');

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0260',
'Litoral Larga');

INSERT INTO `pasantiasnuevo`.`tipo_pasantia`
(`codigo`,
`nombre`)
VALUES
('0290',
'Litoral Caso Especial');
