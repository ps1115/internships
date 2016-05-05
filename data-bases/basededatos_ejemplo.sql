USE spe;

-- Paises

INSERT INTO `pais`
(`nombre`)
VALUES ('Venezuela');

INSERT INTO `pais`
(`nombre`)
VALUES ('U.S.A.');

-- Estados

INSERT INTO `estado`
(`nombre`,`id_pais`)
VALUES
('Distrito Capital',1);

INSERT INTO `estado`
(`nombre`,`id_pais`)
VALUES
('Miranda',1);

INSERT INTO `estado`
(`nombre`,`id_pais`)
VALUES
('Aragua',1);

INSERT INTO `estado`
(`nombre`,`id_pais`)
VALUES
('Florida',2);


-- Areas Laborales

INSERT INTO `area_laboral`
(`nombre`,`descripcion`)
VALUES
('Informatica','Consultoria, desarrollo de software,etc');

INSERT INTO `area_laboral`
(`nombre`,`descripcion`)
VALUES
('Legal','Asesoria legal, resolucion de casos');

INSERT INTO `area_laboral`
(`nombre`,`descripcion`)
VALUES
('Electricidad','Instalaciones electricas');

INSERT INTO `area_laboral`
(`nombre`,`descripcion`)
VALUES
('Arquitectura','Diseño de planos');


-- Universidades

INSERT INTO `universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad Simón Bolívar',1);

INSERT INTO `universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad Católica Andrés Bello',1);

INSERT INTO `universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad Metropolitana',1);

INSERT INTO `universidad`
(`nombre`,`id_pais`)
VALUES
('Universidad De Florida',2);


-- Categorias

INSERT INTO `categoria`
(`id`,`nombre`) VALUES (1,"asociado");
INSERT INTO `categoria`
(`id`,`nombre`) VALUES (2,"titular");
INSERT INTO `categoria`
(`id`,`nombre`) VALUES (3,"agregado");
INSERT INTO `categoria`
(`id`,`nombre`) VALUES (4,"asistente");

-- Coordinaciones

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`) 
VALUES 
(1, 'Tecnología e Ingeniería Eléctrica'
         , '00-11111'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`) 
 VALUES (2
         , 'Ingeniería Mecánica'
         , '11-11112'
         , 'Sartenejas');


INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (3
         , 'Ingeniería Química'
         , '00-11113'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (4
         , 'Tecnología e Ingeniería Electrónica'
         , '00-11114'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (5
         , 'Ingeniería de Materiales'
         , '00-11115'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (6
         , 'Ingeniería Geofísica'
         , '00-11116'
         , 'Sartenejas');


INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (18
         , 'Organización Empresarial e Ingeniería de Producción'
         , '00-11108'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (7
         , 'Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'
         , '11-11117'
         , 'Sartenejas');


INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`) VALUES (8
         , 'Coordinación de Ing. en Telecomunicaciones'
         , '11-11118'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (17
         , 'Coordinación de Química'
         , '11-11107'
         , 'Sartenejas');


INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (9
         , 'Coordinación de Matemáticas'
         , '11-11119'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (10
         , 'Coordinación de Física'
         , '11-11100'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (11
         , 'Coordinación de Biología'
         , '11-11000'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (12
         , 'Arquitectura'
         , '11-10000'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (13
         , 'Estudios Urbanos'
         , '11-10003'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (14
         , 'Licenciatura en Comercio Internacional'
         , '11-10004'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (15
         , 'Ingeniería de Computación'
         , '11-10005'
         , 'Sartenejas');

INSERT INTO `coordinacion`
(`id`,
`nombre`,
`usbid`,
`sede`)  VALUES (16
         , 'Turismo, Hotelería y Hospitalidad'
         , '11-10006'
         , 'Sartenejas');

-- Dedicaciones  

INSERT INTO `dedicacion` (`id`,`nombre`)
VALUES (1, 'exclusiva');
INSERT INTO `dedicacion` (`id`,`nombre`) VALUES (2, 'Tiempo integral');
INSERT INTO `dedicacion` (`id`,`nombre`) VALUES (3, 'Tiempo parcial');

-- Divisiones

INSERT INTO `division` (`id`,`nombre`) VALUES (1, 'División de Ciencias Sociales y Humanidades');
INSERT INTO `division` (`id`,`nombre`) VALUES (2, 'División de Ciencias Biológicas');
INSERT INTO `division` (`id`,`nombre`) VALUES (3, 'División de Ciencias Físicas y Matemáticas');


-- Departamentos

INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
VALUES (1, 'Departamento. de Matemáticas Puras y Aplicadas',
                                 3,
                                 'dep-ma@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`)  
VALUES (2, 'Departamento de Física',
                                 3,
                                 'dep-fs@usb.ve ',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`)  
VALUES (3, 'Departamento de Química',
                                 3,
                                 'dep-qm@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (4, 'Departamento de Mecánica',
                                 3,
                                 'mc-usb@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
VALUES (5, 'Departamento de Termodinámica',
                                 3,
                                 'teryfem@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (6, 'Departamento de Electrónica y Circuitos',
                                 3,
                                 'dep-ec@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (7, 'Departamento de Conversión de Energía',
                                 3,
                                 'dep-ct@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (8, 'Departamento de Procesos y Sistemas',
                                 3,
                                 'usb-ps@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (9, 'Departamento de Ciencia de los Materiales',
                                 3,
                                 'dep-mt@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (10, 'Departamento de Computación',
                                 3,
                                 'dep-ci@ldc.usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (11, 'Departamento de Ciencias de la Tierra',
                                 3,
                                 'dep-gc@usb.ve',
                                 'Sartenejas');
INSERT INTO `departamento` (`id`,`nombre`,`id_division`,`email_dep`,`sede`) 
 VALUES (12, 'Departamento de Cómputo Científico',
                                 3,
                                 'usb-cce@usb.ve ',
                                 'Sartenejas');


-- Carreras

INSERT INTO `carrera`
 (`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0100', 'Ingeniería Eléctrica', 'Larga',
                        'Sartenejas', 1, 1);
INSERT INTO `carrera`
 (`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0200', 'Ingeniería Mecánica', 'Larga',
                        'Sartenejas', 2, 2);
INSERT INTO `carrera`
 (`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0300', 'Ingeniería Química', 'Larga',
                        'Sartenejas', 3, 3);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0600', 'Ingeniería Electrónica', 'Larga',
                        'Sartenejas', 4, 4);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('1500', 'Ingeniería de Materiales', 'Larga',
                        'Sartenejas', 5, 5);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0800', 'Ingeniería de la Computación', 'Larga',
                        'Sartenejas', 6, 6);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('1200', 'Ingeniería Geofísica', 'Larga',
                        'Sartenejas', 7, 7);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('1700', 'Ingeniería de Producción', 'Larga',
                        'Sartenejas', 8, 8);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('4000', 'Ingeniería de Mantenimiento', 'Litoral',
                        'Sartenejas', 9, 9);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('1800', 'Ingeniería de Telecomunicaciones', 'Larga',
                        'Sartenejas', 10, 10);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0400', 'Licenciatura en Química', 'Larga',
                        'Sartenejas', 11, 11);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0500', 'Licenciatura en Matemáticas', 'Larga',
                        'Sartenejas', 12, 12);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('1000', 'Licenciatura en Física', 'Larga',
                        'Sartenejas', 13, 13);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('1900', 'Licenciatura en Biología', 'Larga',
                        'Sartenejas', 14, 14);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('0700', 'Arquitectura', 'Larga',
                        'Sartenejas', 15, 15);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('1100', 'Urbanismo', 'Larga',
                        'Sartenejas', 16, 16);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('3200', 'Licenciatura en Comercio Internacional', 'Larga',
                        'Sartenejas', 17, 17);
INSERT INTO `carrera`
(`codigo`,
 `nombre`,
 `duracion`,
 `sede`,
 `coordinacion`,
 `id`) VALUES ('3000', 'Licenciatura en Gestión de la Hospitalidad', 'Larga',
                        'Sartenejas', 18, 18);


-- Tipos de Pasantias

INSERT INTO `tipo_pasantia`(
`codigo`,`nombre`) VALUES ('EP-3420', 'Pasantia larga');

INSERT INTO `tipo_pasantia`(
`codigo`,`nombre`) VALUES ('EP-1420', 'Pasantia intermedia');

INSERT INTO `tipo_pasantia`(
`codigo`,`nombre`) VALUES ('ET-2420', 'Pasantia intermedia');

-- Periodos

INSERT INTO `periodo` (`id`,`nombre`,`fecha_inicio`,`fecha_fin`,`periodo_activo`) VALUES (77, 'Abril-Septiembre, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);
INSERT INTO `periodo` (`id`,`nombre`,`fecha_inicio`,`fecha_fin`,`periodo_activo`) VALUES (78, 'Octubre-Marzo, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);
INSERT INTO `periodo` (`id`,`nombre`,`fecha_inicio`,`fecha_fin`,`periodo_activo`) VALUES (79, 'Julio-Septiembre, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);

-- Empresas

INSERT INTO `empresa`
(`id`,
    `log`,
    `password`,
    `pregunta_secreta`,
    `respuesta_pregunta_secreta`,
    `nombre`,
    `id_pais`,
    `id_area_laboral`,
    `id_estado`,
    `direccion`,
    `pag_web`,
    `descripcion`,
    `telefono`,
    `contacto_RRHH`,
    `intentos`,
    `habilitado`,
    `fechaCreacion`,
    `ultimaModificacion`
)
VALUES (77, 'log', 'password', 'quien?', 'yo', 'Empresas Polar', 1, NULL, NUll,
      '4ta. Transv., Centro Empresarial Polar, Nivel 1, Los Cortijos de Lourdes, Caracas',
      'http://empresaspolar.com', 
      'Productos Alimenticios, Productos de Alimentos, Distribuidora de Alimentos, Fábrica de Alimentos, Licores, Distribuidora de Licores, Productos de Limpieza '
      , '0800-372 82 42', NULL, 0, 1,
      CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
      );

-- Usuarios

INSERT INTO `usuario`
(`usbid`,`nombre`,`apellido`,`ci`,`tipo`,`foto`,`llave`)
VALUES ('12-11402', 'Georvic', 'Tur', NULL, NULL, NULL,NULL
      );

INSERT INTO `usuario`
(`usbid`,`nombre`,`apellido`,`ci`,`tipo`,`foto`,`llave`)
   VALUES ('01-12345', 'Satouru', 'Fujinuma', NULL, NULL, NULL,NULL
      );

INSERT INTO `usuario`
(`usbid`,`nombre`,`apellido`,`ci`,`tipo`,`foto`,`llave`)
   VALUES ('01-14746', 'Jack', 'London', NULL, NULL, NULL,NULL
      );

INSERT INTO `usuario`
(`usbid`,`nombre`,`apellido`,`ci`,`tipo`,`foto`,`llave`)
   VALUES ('01-17746', 'Martin', 'Eden', NULL, NULL, NULL,NULL
      );

-- Usuarios_estudiantes

INSERT INTO `usuario_estudiante`
(`usbid_usuario`,`carnet`,`cohorte`,`carrera`,`estudiante_sede`,
`email_sec`,`telf_hab`,`telf_cel`,`direccion`,`sexo`)
 VALUES ('12-11402', 
      '12-11402', '12','0800', 
      'Sartenejas', 'algo@gmail.com', 
      NULL, NULL, 'Ningun lado', 'M');


-- Tutores Industriales
/*
INSERT INTO `tutor_industrial`
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
*/

INSERT INTO `tutor_industrial`
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
   VALUES (1,'plopez@gmail.com', 'Pedro', 'López', '5442257', 'password', 'Nombre suegra', 'Marisa', 77,
      'Ingeniero', 'Jefe de departamento',1, 'Desarrollo', 'Los Cortijos', NULL, NULL, '0424-1518824',
      0, 1
      );

-- Tutor académico

INSERT INTO `tutor_academico`
(`usbid`)
 VALUES ('01-12345');

-- Pasantias

INSERT INTO `pasantia` 
(`codigo`,
    `periodo`,
    `anio`,
    `fecha`,
    `cod_seguridad`,
    `titulo`,
    `area_proyecto` ,
    `resumen_proyecto` ,
    `confidencial`,
    `objetivos` ,
    `calificacion_total`,
    `calificacion_tutor_academico`,
    `calificacion_tutor_industrial` ,
    `fecha_acta_evaluacion`,
    `periodo_finaliza`  ,
    `anio_finaliza`,
    `tiene_mencion`,
    `observacion_mencion`,
    `fecha_validacion` ,
    `status` ,
    `id_tutor_industrial`,
    `id_jurado` ,
    `id_estudiante`,
    `id_tutor_academico`,
    `retirar`,
    `obtencion_pasantia`,
    `motivo_retiro_tutor_industrial`,
    `motivo_retiro_tutor_academico`,
    `motivo_retiro_estudiante`
	)
   VALUES ('EP-3420', 77, 2016, '2016-03-10', '325698kjsa',
      'Análisis de pruebas mediante el uso de redes neurales', 'Sistemas de informacion',
      'Principios de pruebas', 'si', 'Pruebas optimas', 0, 0, 0,
      '2016-03-10', 78,  2017, 0, 'no mencion', '2016-03-10', 'en curso',
      'plopez@gmail.com', NULL, '12-11402', '01-12345', NULL, NULL, NULL, NULL, NULL
      );
INSERT INTO `pasantia` 
(`codigo`,
    `periodo`,
    `anio`,
    `fecha`,
    `cod_seguridad`,
    `titulo`,
    `area_proyecto` ,
    `resumen_proyecto` ,
    `confidencial`,
    `objetivos` ,
    `calificacion_total`,
    `calificacion_tutor_academico`,
    `calificacion_tutor_industrial` ,
    `fecha_acta_evaluacion`,
    `periodo_finaliza`  ,
    `anio_finaliza`,
    `tiene_mencion`,
    `observacion_mencion`,
    `fecha_validacion` ,
    `status` ,
    `id_tutor_industrial`,
    `id_jurado` ,
    `id_estudiante`,
    `id_tutor_academico`,
    `retirar`,
    `obtencion_pasantia`,
    `motivo_retiro_tutor_industrial`,
    `motivo_retiro_tutor_academico`,
    `motivo_retiro_estudiante`
	)
   VALUES ('EP-1420', 77, 2016, '2016-03-10', 'sdio7hij2',
      'Análisis de pruebas mediante el uso de redes neurales', 'Sistemas de informacion',
      'Principios de pruebas', 'si', 'Pruebas optimas', 0, 0, 0,
      '2016-03-10', 78,  2017, 0, 'no mencion', '2016-03-10', 'en curso',
      'plopez@gmail.com', NULL,'12-11402', '01-12345', NULL, NULL, NULL, NULL, NULL
      );
INSERT INTO `pasantia` 
(`codigo`,
    `periodo`,
    `anio`,
    `fecha`,
    `cod_seguridad`,
    `titulo`,
    `area_proyecto` ,
    `resumen_proyecto` ,
    `confidencial`,
    `objetivos` ,
    `calificacion_total`,
    `calificacion_tutor_academico`,
    `calificacion_tutor_industrial` ,
    `fecha_acta_evaluacion`,
    `periodo_finaliza`  ,
    `anio_finaliza`,
    `tiene_mencion`,
    `observacion_mencion`,
    `fecha_validacion` ,
    `status` ,
    `id_tutor_industrial`,
    `id_jurado` ,
    `id_estudiante`,
    `id_tutor_academico`,
    `retirar`,
    `obtencion_pasantia`,
    `motivo_retiro_tutor_industrial`,
    `motivo_retiro_tutor_academico`,
    `motivo_retiro_estudiante`
	)
   VALUES ('ET-2420', 78, 2016, '2016-03-10', 'sdj2323',
      'Análisis de pruebas mediante el uso de redes neurales', 'Sistemas de informacion',
      'Principios de pruebas', 'si', 'Pruebas optimas', 0, 0, 0,
      '2016-03-10', 78,  2017, 0, 'no mencion', '2016-03-10', 'en curso',
      'plopez@gmail.com', NULL, '12-11402', '01-12345', NULL, NULL, NULL, NULL, NULL
      );



