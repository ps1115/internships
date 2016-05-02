START TRANSACTION;

	-- Crea el usuario
	
	-- El % se cambiara por la direccion IP con la cual se accedera
	-- a la aplicacion
	
	-- El alist_development se cambiara por el nombre que tenga la
	-- base de datos con la cual corra la aplicacion
	
	CREATE USER 'spe'@'%' IDENTIFIED BY 'spe2016'; 
	
	-- Permiso para obtener filas de las tablas
	
	GRANT SELECT ON spe.* TO 'spe'@'%';
	
	-- Permiso para agregar filas a las tablas
	
	GRANT INSERT ON spe.* TO 'spe'@'%';
	
	-- Permiso para eliminar filas de las tablas
	
	GRANT UPDATE ON spe.* TO 'spe'@'%';
	
	-- Permiso para ejecutar funciones o procedimientos
	
	GRANT EXECUTE ON spe.* TO 'spe'@'%';

	-- Permiso para obtener los procedimientos

	GRANT SELECT ON `mysql`.`proc` TO 'alistweb'@'%';
	
	-- Para mostrar el usuario, en los privilegios sale la N como si el usuario no los
	-- tuviese pero esto es porque solo los tiene para una base de datos en especifico
	
	SELECT * FROM mysql.user;

COMMIT;
