
INSERT INTO dedicacion VALUES (1, 'exclusiva');
INSERT INTO dedicacion VALUES (2, 'tiempo integral');
INSERT INTO dedicacion VALUES (3, 'tiempo parcial');

INSERT INTO categoria VALUES (1,"asociado");
INSERT INTO categoria VALUES (2,"titular");
INSERT INTO categoria VALUES (3,"agregado");
INSERT INTO categoria VALUES (4,"asistente");

INSERT INTO periodo VALUES (77, 'abril-septiembre,2016',CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);

INSERT INTO division VALUES (1, 'División de Ciencias Sociales y Humanidades');
INSERT INTO division VALUES (2, 'División de Ciencias Biológicas');
INSERT INTO division VALUES (3, 'División de Ciencias Físicas y Matemáticas');

INSERT INTO departamento VALUES (1, 'Departamento. de Matemáticas Puras y Aplicadas',
                                 3,
                                 'dep-ma@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (2, 'Departamento de Física',
                                 3,
                                 'dep-fs@usb.ve ',
                                 'Sartenejas');
INSERT INTO departamento VALUES (3, 'Departamento de Química',
                                 3,
                                 'dep-qm@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (4, 'Departamento de Mecánica',
                                 3,
                                 'mc-usb@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (5, 'Departamento de Termodinámica y Fenómenos de Transferencia',
                                 3,
                                 'teryfem@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (6, 'Departamento de Electrónica y Circuitos',
                                 3,
                                 'dep-ec@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (7, 'Departamento de Conversión y Transporte de Energía',
                                 3,
                                 'dep-ct@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (8, 'Departamento de Procesos y Sistemas',
                                 3,
                                 'usb-ps@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (9, 'Departamento de Ciencia de los Materiales',
                                 3,
                                 'dep-mt@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (10, 'Departamento de Computación y Tecnología de Información',
                                 3,
                                 'dep-ci@ldc.usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (11, 'Departamento de Ciencias de la Tierra',
                                 3,
                                 'dep-gc@usb.ve',
                                 'Sartenejas');
INSERT INTO departamento VALUES (12, 'Departamento de Cómputo Científico y Estadística',
                                 3,
                                 'usb-cce@usb.ve ',
                                 'Sartenejas');



-- INSERT INTO tipo_pasantia VALUES ('EP-3420', 'Pasantia Larga');
-- INSERT INTO tipo_pasantia VALUES ('EP-2420', 'Pasantia Intermedia (Carreras Largas)');
-- INSERT INTO tipo_pasantia VALUES ('ET-2420', 'Pasantia Intermedia (Carreras Cortas)');
-- INSERT INTO tipo_pasantia VALUES ('EP-1420', 'Pasantia Corta (Carreras Largas)');
-- INSERT INTO tipo_pasantia VALUES ('ET-1420', 'Pasantia Corta (Carreras Cortas)');


INSERT INTO carrera VALUES ('0100', 'Ingeniería Eléctrica', 'Larga',
                        'Sartenejas', 'Tecnología e Ingeniería Eléctrica', 1);
INSERT INTO carrera VALUES ('0200', 'Ingeniería Mecánica', 'Larga',
                        'Sartenejas', 'Ingeniería Mecánica', 2);
INSERT INTO carrera VALUES ('0300', 'Ingeniería Química', 'Larga',
                        'Sartenejas', 'Ingeniería Química', 3);
INSERT INTO carrera VALUES ('0600', 'Ingeniería Electrónica', 'Larga',
                        'Sartenejas', 'Tecnología e Ingeniería Electrónica', 4);
INSERT INTO carrera VALUES ('1500', 'Ingeniería de Materiales', 'Larga',
                        'Sartenejas', 'Ingeniería de Materiales', 5);
INSERT INTO carrera VALUES ('0800', 'Ingeniería de la Computación', 'Larga',
                        'Sartenejas', 'Ingeniería de Computación', 6);
INSERT INTO carrera VALUES ('1200', 'Ingeniería Geofísica', 'Larga',
                        'Sartenejas', 'Ingeniería Geofísica', 7);
INSERT INTO carrera VALUES ('1700', 'Ingeniería de Producción', 'Larga',
                        'Sartenejas', 'Organización Empresarial e Ingeniería de Producción', 8);
INSERT INTO carrera VALUES ('4000', 'Ingeniería de Mantenimiento', 'Litoral',
                        'Sartenejas', 'Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento', 9);
INSERT INTO carrera VALUES ('1800', 'Ingeniería de Telecomunicaciones', 'Larga',
                        'Sartenejas', 'Coordinación de Ing. en Telecomunicaciones', 10);
INSERT INTO carrera VALUES ('0400', 'Licenciatura en Química', 'Larga',
                        'Sartenejas', 'Coordinación de Química', 11);
INSERT INTO carrera VALUES ('0500', 'Licenciatura en Matemáticas', 'Larga',
                        'Sartenejas', 'Coordinación de Matemáticas', 12);
INSERT INTO carrera VALUES ('1000', 'Licenciatura en Física', 'Larga',
                        'Sartenejas', 'Coordinación de Física', 13);
INSERT INTO carrera VALUES ('1900', 'Licenciatura en Biología', 'Larga',
                        'Sartenejas', 'Coordinación de Biología', 14);
INSERT INTO carrera VALUES ('0700', 'Arquitectura', 'Larga',
                        'Sartenejas', 'Arquitectura', 15);
INSERT INTO carrera VALUES ('1100', 'Urbanismo', 'Larga',
                        'Sartenejas', 'Estudios Urbanos', 16);
INSERT INTO carrera VALUES ('3200', 'Licenciatura en Comercio Internacional', 'Larga',
                        'Sartenejas', 'Comercio Exterior y Licenciatura en  Comercio Internacional', 17);
INSERT INTO carrera VALUES ('3000', 'Licenciatura en Gestión de la Hospitalidad', 'Larga',
                        'Sartenejas', 'Turismo, Hotelería y Hospitalidad', 18);


INSERT INTO coordinacion VALUES (1
         , 'Tecnología e Ingeniería Eléctrica'
         , '00-11111'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (2
         , 'Ingeniería Mecánica'
         , '11-11112'
         , 'Sartenejas');


INSERT INTO coordinacion VALUES (3
         , 'Ingeniería Química'
         , '00-11113'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (4
         , 'Tecnología e Ingeniería Electrónica'
         , '00-11114'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (5
         , 'Ingeniería de Materiales'
         , '00-11115'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (6
         , 'Ingeniería Geofísica'
         , '00-11116'
         , 'Sartenejas');


INSERT INTO coordinacion VALUES (18
         , 'Organización Empresarial e Ingeniería de Producción'
         , '00-11108'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (7
         , 'Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'
         , '11-11117'
         , 'Sartenejas');


INSERT INTO coordinacion VALUES (8
         , 'Coordinación de Ing. en Telecomunicaciones'
         , '11-11118'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (17
         , 'Coordinación de Química'
         , '11-11107'
         , 'Sartenejas');


INSERT INTO coordinacion VALUES (9
         , 'Coordinación de Matemáticas'
         , '11-11119'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (10
         , 'Coordinación de Física'
         , '11-11100'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (11
         , 'Coordinación de Biología'
         , '11-11000'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (12
         , 'Arquitectura'
         , '11-10000'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (13
         , 'Estudios Urbanos'
         , '11-10003'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (14
         , 'Licenciatura en Comercio Internacional'
         , '11-10004'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (15
         , 'Ingeniería de Computación'
         , '11-10005'
         , 'Sartenejas');

INSERT INTO coordinacion VALUES (16
         , 'Turismo, Hotelería y Hospitalidad'
         , '11-10006'
         , 'Sartenejas');





-- INSERT INTO usuario
--    VALUES ('11-10053', 'Estudiante', 'Estudioso', NULL, NULL, NULL,NULL
--       );

INSERT INTO usuario
   VALUES ('12-11402', 'Georvic', 'Tur', NULL, NULL, NULL,NULL
      );

INSERT INTO usuario
   VALUES ('01-12345', 'Satouru', 'Fujinuma', NULL, NULL, NULL,NULL
      );

INSERT INTO usuario
   VALUES ('01-14746', 'Jack', 'London', NULL, NULL, NULL,NULL
      );

INSERT INTO usuario
   VALUES ('01-17746', 'Martin', 'Eden', NULL, NULL, NULL,NULL
      );

INSERT INTO usuario_estudiante VALUES ('12-11402', 
      '12-11402', '12','0800', 
      'Sartenejas', 'algo@gmail.com', 
      NULL, NULL, 'Ningun lado', 'M');

INSERT INTO empresa
   VALUES (97, 'log', 'password', 'quien?', 'yo', 'Empresas Polar', 1, NULL, NUll,
      '4ta. Transv., Centro Empresarial Polar, Nivel 1, Los Cortijos de Lourdes, Caracas',
      'http://empresaspolar.com', 
      'Productos Alimenticios, Productos de Alimentos, Distribuidora de Alimentos, Fábrica de Alimentos, Licores, Distribuidora de Licores, Productos de Limpieza '
      , '0800-372 82 42', NULL, 0, 1,
      CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
      );

-- INSERT INTO tutor_academico VALUES ('01-12345');
-- INSERT INTO universidad VALUES (77,'Universidad Simón Bolívar',1);
-- INSERT INTO tutor_industrial
--   VALUES (77, 'tutor_industrial@gmail.com', 'Gabriel', 'Logan', '13198799', 'password', 'soy?'
--   , 'Gabriel', 77,
--      'Consultor de Tecnología', 'chief technical officer'
--      ,77, 'Departamento de Computación y Tecnología de Información', 'La Florida', 1, NULL, '777-7777',
--      0, 1
--      );



-- INSERT INTO pasantia
--    VALUES ('PS1115', 77, 2016, '2016-03-10', 'seguridad',
--       'Probando', 'Pruebas', 'muy fino', 'si', 'varios', 0, 0, 0, NULL,
--       '2016-03-10', 2017, 0, 'no mencion', '2016-03-10', 'en curso',
--       '77@gmail.com', NULL, '77', '77', NULL, NULL, NULL, NULL, NULL
--       );

