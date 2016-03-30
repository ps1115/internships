USE pasantiasnuevo;

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

INSERT INTO tipo_pasantia VALUES ('EP-3420', 'Pasantia larga');
INSERT INTO tipo_pasantia VALUES ('EP-1420', 'Pasantia intermedia');
INSERT INTO tipo_pasantia VALUES ('ET-2420', 'Pasantia intermedia');

/*

-- Periodos

INSERT INTO periodo VALUES (77, 'Abril-Septiembre, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);
INSERT INTO periodo VALUES (78, 'Octubre-Marzo, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);
INSERT INTO periodo VALUES (79, 'Julio-Septiembre, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);

-- Empresas

INSERT INTO empresa
   VALUES (77, 'pmendoza@empresaspolar.com', 'password', 'Nombre mascota', 'Balto', 'Empresas Polar', NULL, NULL,
      NULL, 'Los Cortijos', NULL, 'Alimentos y bebidas', NULL, NULL, 0, 1,
      CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
      );

INSERT INTO usuario
   VALUES ('77', 'Juan Carlos', 'Medina Perez', NULL, NULL, NULL,NULL);

-- Tutores Academicos

INSERT INTO tutor_academico VALUES ('77');

-- Tutores Industriales
INSERT INTO `pasantiasnuevo`.`tutor_industrial`
(`id`,
`email`,
`nombre`,
`apellido`,
`ci`,
`password`,
`pregunta_secreta`,
`respuesta_pregunta_secreta`,
`id_empresa`,
`profesion`,
`cargo`,
`id_universidad`,
`departamento`,
`direccion`,
`id_pais`,
`id_estado`,
`telefono`,
`intentos`,
`habilitado`)
VALUES
(<{id: }>,
<{email: }>,
<{nombre: }>,
<{apellido: }>,
<{ci: }>,
<{password: }>,
<{pregunta_secreta: }>,
<{respuesta_pregunta_secreta: }>,
<{id_empresa: }>,
<{profesion: }>,
<{cargo: }>,
<{id_universidad: }>,
<{departamento: }>,
<{direccion: }>,
<{id_pais: }>,
<{id_estado: }>,
<{telefono: }>,
<{intentos: 0}>,
<{habilitado: 1}>);

INSERT INTO tutor_industrial
   VALUES ('plopez@gmail.com', NULL, NULL, NULL, NULL, 'Nombre suegra', 'Marisa', 77,
      1, 'Ingeniero', 'Jefe de departamento', 'Desarrollo', 'Los Cortijos', NULL, NULL, '0424-1518824',
      0, 1
      );

-- Pasantias

INSERT INTO pasantia
   VALUES ('EP-3420', 77, 2016, '2016-03-10', '325698kjsa',
      'Análisis de pruebas mediante el uso de redes neurales', 'Sistemas de informacion',
      'Principios de pruebas', 'si', 'Pruebas optimas', 0, 0, 0,
      '2016-03-10', 78,  2017, 0, 'no mencion', '2016-03-10', 'en curso',
      'plopez@gmail.com', NULL, '77', '77', NULL, NULL, NULL, NULL, NULL
      );
INSERT INTO pasantia
   VALUES ('EP-1420', 77, 2016, '2016-03-10', 'sdio7hij2',
      'Análisis de pruebas mediante el uso de redes neurales', 'Sistemas de informacion',
      'Principios de pruebas', 'si', 'Pruebas optimas', 0, 0, 0,
      '2016-03-10', 78,  2017, 0, 'no mencion', '2016-03-10', 'en curso',
      'plopez@gmail.com', NULL, '77', '77', NULL, NULL, NULL, NULL, NULL
      );
INSERT INTO pasantia
   VALUES ('ET-2420', 78, 2016, '2016-03-10', 'sdj2323',
      'Análisis de pruebas mediante el uso de redes neurales', 'Sistemas de informacion',
      'Principios de pruebas', 'si', 'Pruebas optimas', 0, 0, 0,
      '2016-03-10', 78,  2017, 0, 'no mencion', '2016-03-10', 'en curso',
      'plopez@gmail.com', NULL, '77', '77', NULL, NULL, NULL, NULL, NULL
      );

*/
