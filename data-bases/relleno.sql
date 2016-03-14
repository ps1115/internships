
INSERT INTO periodo VALUES (77, 'abril-septiembre');

INSERT INTO tipo_pasantia VALUES ('PS1115', 'Pasantia prueba');
INSERT INTO tipo_pasantia VALUES ('PS1110', 'Otra Pasantia prueba');

INSERT INTO usuario
   VALUES ('77', 'Estudiante', 'Estudioso', NULL, NULL
      );

INSERT INTO empresa
   VALUES (77, 'log', 'password', 'quien?', 'yo', 'Empresa', NULL, NULL,
      'Hogwarts', NULL, 'Hacemos cosas finas', NULL, NULL, 0, 1,
      CURRENT_TIMESTAMP, CURRENT_TIMESTAMP
      );

INSERT INTO tutor_academico VALUES ('77');

INSERT INTO tutor_industrial
   VALUES (77, '77@gmail.com', NULL, NULL, NULL, NULL, 'soy', 'jogs', 77,
      'vago', 'Senior vago', 'Vagancia', 'Narnia', NULL, NULL, '777-7777',
      0, 1
      );

INSERT INTO pasantia
   VALUES ('PS1115', 77, 2016, '2016-03-10', 'seguridad',
      'Probando', 'Pruebas', 'muy fino', 'si', 'varios', 0, 0, 0, NULL,
      '2016-03-10', 2017, 0, 'no mencion', '2016-03-10', 'en curso',
      '77@gmail.com', NULL, '77', '77', NULL, NULL, NULL, NULL, NULL
      );

INSERT INTO pasantia
   VALUES ('PS1110', 77, 2016, '2016-03-10', 'seguridad',
      'Probando', 'Pruebas', 'muy fino', 'si', 'varios', 0, 0, 0, NULL,
      '2016-03-10', 2017, 0, 'no mencion', '2016-03-10', 'en curso',
      '77@gmail.com', NULL, '77', '77', NULL, NULL, NULL, NULL, NULL
      );
