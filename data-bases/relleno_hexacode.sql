INSERT INTO periodo VALUES (77, 'Abril-Septiembre, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);
INSERT INTO periodo VALUES (78, 'Octubre-Marzo, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);
INSERT INTO periodo VALUES (79, 'Julio-Septiembre, 2016', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,0);


INSERT INTO tipo_pasantia VALUES ('EP-3420', 'Pasantia larga');
INSERT INTO tipo_pasantia VALUES ('EP-1420', 'Pasantia intermedia');
INSERT INTO tipo_pasantia VALUES ('ET-2420', 'Pasantia intermedia');


INSERT INTO usuario
   VALUES ('77', 'Juan Carlos', 'Medina Perez', NULL, NULL, NULL,NULL);

INSERT INTO empresa
   VALUES (77, 'pmendoza@empresaspolar.com', 'password', 'Nombre mascota', 'Balto', 'Empresas Polar', NULL, NULL,
      NULL, 'Los Cortijos', NULL, 'Alimentos y bebidas', NULL, NULL, 0, 1,
      CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
      );


INSERT INTO tutor_academico VALUES ('77');


INSERT INTO pais VALUES (25,'Venezuela');


INSERT INTO universidad VALUES (12,'Universidad Simon Bolivar',25);


INSERT INTO tutor_industrial
   VALUES (77, 'plopez@gmail.com', NULL, NULL, NULL, NULL, 'Nombre suegra', 'Marisa', 77,
      'Ingeniero', 'Jefe de departamento', 12, 'Desarrollo', 'Los Cortijos', NULL, NULL, '0424-1518824',
      0, 1
      );


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
INSERT INTO pasantia
   VALUES ('EP-3420', 77, 2016, '2016-03-10', '325698kjsa',
      'Análisis de pruebas mediante el uso de redes neurales', 'Sistemas de informacion',
      'Principios de pruebas', 'si', 'Pruebas optimas', 0, 0, 0,
      '2016-03-10', 78,  2017, 0, 'no mencion', '2016-03-10', 'en curso',
      'plopez@gmail.com', NULL, '11-10576', '77', NULL, NULL, NULL, NULL, NULL
      );
