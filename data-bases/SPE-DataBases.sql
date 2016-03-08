-- phpMyAdmin SQL Dump
-- version 4.1.7
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 23-02-2016 a las 15:10:54
-- Versión del servidor: 5.1.73-1
-- Versión de PHP: 5.3.3-7+squeeze19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: 'pasantiasNuevo'
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'actividad'
--

CREATE TABLE IF NOT EXISTS 'actividad' (
    'id'                int(11)     NOT NULL AUTO_INCREMENT,
    'codigo_fase'       int(11)     DEFAULT NULL,
    'descripcion'       text        NOT NULL,
    'tiempo_estimado'   varchar(20) NOT NULL,
    PRIMARY KEY ('id'),
    KEY 'fk_actividad_codigo_fase_fase_codigo' ('codigo_fase')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=103942 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'calculo_pago'
--

CREATE TABLE IF NOT EXISTS 'calculo_pago' (
    'id_categoria'      int(11)     NOT NULL,
    'id_tipo_pasantia'  varchar(8)  NOT NULL,
    'id_zona'           int(11)     NOT NULL,
    'monto'             double      NOT NULL,
    PRIMARY KEY ('id_categoria','id_tipo_pasantia','id_zona'),
    KEY 'fk_calculo_pago_id_tipo_pasantia_tipo_pasantia_codigo' ('id_tipo_pasantia'),
    KEY 'fk_calculo_pago_id_zona_zona_id' ('id_zona')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'carrera'
--

CREATE TABLE IF NOT EXISTS 'carrera' (
    'codigo'        varchar(4)          NOT NULL,
    'nombre'        varchar(100)        NOT NULL,
    'duracion'      varchar(11)         NOT NULL DEFAULT 'Larga',
    'sede'          varchar(20)         NOT NULL DEFAULT 'Sartenejas',
    'coordinacion'  varchar(100)        NOT NULL,
    'id'            bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    PRIMARY KEY ('codigo','id'),
    UNIQUE KEY 'id' ('id')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=33 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'carrera_tipopasantia'
--

CREATE TABLE IF NOT EXISTS 'carrera_tipopasantia' (
    'codigo_carrera'        varchar(4) NOT NULL,
    'codigo_tipo_pasantia'  varchar(8) NOT NULL,
    KEY 'fk_codigo_carrera_carrera_codigo' ('codigo_carrera'),
    KEY 'fk_codigo_tipo_pasantia_tipo_pasantia_codigo' ('codigo_tipo_pasantia')
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COMMENT='tales carreras realizan tales periodos';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'categoria'
--

CREATE TABLE IF NOT EXISTS 'categoria' (
    'id'        int(11)     NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(20) NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'contenido_mensajes'
--

CREATE TABLE IF NOT EXISTS 'contenido_mensajes' (
    'id'        int(11)         NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(120)    NOT NULL,
    'mensaje'   varchar(500)    NOT NULL,
    'asunto'    varchar(80)     NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'coordinacion'
--

CREATE TABLE IF NOT EXISTS 'coordinacion' (
    'nombre'    varchar(100)    NOT NULL,
    'usbid'     varchar(30)     NOT NULL,
    'sede'      varchar(20)     NOT NULL,
    PRIMARY KEY ('nombre')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'dedicacion'
--

CREATE TABLE IF NOT EXISTS 'dedicacion' (
    'id'        int(11)     NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(20) NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'departamento'
--

CREATE TABLE IF NOT EXISTS 'departamento' (
    'id'            int(11)         NOT NULL AUTO_INCREMENT,
    'nombre'        varchar(50)     NOT NULL DEFAULT '',
    'id_division'   int(11)         NOT NULL DEFAULT '0',
    'email_dep'     varchar(254)    DEFAULT NULL,
    'sede'          varchar(20)     NOT NULL,
    PRIMARY KEY ('id'),
    KEY 'fk_departamento_id_division_id' ('id_division')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=30 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'division'
--

CREATE TABLE IF NOT EXISTS 'division' (
    'id'        int(11)     NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(50) NOT NULL DEFAULT '',
    PRIMARY KEY ('id')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'empresa'
--

CREATE TABLE IF NOT EXISTS 'empresa' (
    'login'                     varchar(254)    NOT NULL,
    'password'                  varchar(254)    NOT NULL,
    'pregunta_secreta'          varchar(254)    NOT NULL,
    'respuesta_pregunta_secreta'varchar(254)    NOT NULL,
    'nombre'                    varchar(254)    NOT NULL,
    'direccion'                 text,
    'pag_web'                   varchar(254)    DEFAULT NULL,
    'descripcion'               text,
    'telefono'                  varchar(20)     DEFAULT NULL,
    'contacto_RRHH'             varchar(20)     DEFAULT NULL,
    'intentos'                  int(4)          DEFAULT '0',
    'habilitado'                int(2)          DEFAULT '1',
    'fechaCreacion'             timestamp       NOT NULL DEFAULT '0000-00-00 00:00:00',
    'ultimaModificacion'        timestamp       NOT NULL DEFAULT '0000-00-00 00:00:00',
    PRIMARY KEY ('login')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Disparadores 'empresa'
--
DROP TRIGGER IF EXISTS 'empresainsert';
DELIMITER //
CREATE TRIGGER 'empresainsert' BEFORE INSERT ON 'empresa'
 FOR EACH ROW BEGIN SET NEW.fechaCreacion=IF(ISNULL(NEW.fechaCreacion) OR NEW.fechaCreacion='0000-00-00 00:00:00', CURRENT_TIMESTAMP, IF(NEW.fechaCreacion<CURRENT_TIMESTAMP, NEW.fechaCreacion, CURRENT_TIMESTAMP));SET NEW.ultimaModificacion=NEW.fechaCreacion; END
//
DELIMITER ;
DROP TRIGGER IF EXISTS 'empresaupdate';
DELIMITER //
CREATE TRIGGER 'empresaupdate' BEFORE UPDATE ON 'empresa'
 FOR EACH ROW SET NEW.ultimaModificacion=IF(NEW.ultimaModificacion<OLD.ultimaModificacion, OLD.ultimaModificacion, CURRENT_TIMESTAMP)
//
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'error'
--

CREATE TABLE IF NOT EXISTS 'error' (
    'id_error'  int(254)        NOT NULL AUTO_INCREMENT,
    'consulta'  varchar(254)    NOT NULL,
    'msj_error' varchar(254)    NOT NULL,
    'USBID'     varchar(254)    NOT NULL,
    'fecha'     timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ('id_error')
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2550 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'estado'
--

CREATE TABLE IF NOT EXISTS 'estado' (
    'id'        int(2)      NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(40) NOT NULL,
    'id_zona'   int(11)     NOT NULL,
    PRIMARY KEY ('id'),
    KEY 'fk_estado_id_zona_zona_id' ('id_zona')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=25 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'evento'
--

CREATE TABLE IF NOT EXISTS 'evento' (
    'codigo'                    int(11)         NOT NULL AUTO_INCREMENT,
    'nombre'                    varchar(254)    NOT NULL,
    'fecha_inicio'              date            NOT NULL,
    'fecha_fin'                 date            NOT NULL,
    'nombre_trimestre_actual'   varchar(50)     DEFAULT NULL,
    PRIMARY KEY ('codigo')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=10 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'extemp'
--

CREATE TABLE IF NOT EXISTS 'extemp' (
    'usbid'         varchar(9)  NOT NULL,
    'comunidad'     varchar(15) NOT NULL,
    PRIMARY KEY ('usbid')
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'fase'
--

CREATE TABLE IF NOT EXISTS 'fase' (
    'codigo'                int(11)         NOT NULL AUTO_INCREMENT,
    'id_periodo'            int(10)         NOT NULL,
    'anho'                  int(11)         NOT NULL,
    'id_estudiante'         varchar(254)    NOT NULL,
    'codigo_pasantia'       varchar(8)      NOT NULL,
    'nombre_fase'           varchar(100)    NOT NULL,
    'objetivos_especificos' text            NOT NULL,
    PRIMARY KEY ('codigo'),
    KEY 'fk_fase_id_estudiante_estudiante_usbid' ('id_estudiante'),
    KEY 'fk_fase_id_periodo_periodo_id' ('id_periodo'),
    KEY 'fk_fase_codigo_pasantia_tipo_pasantia_codigo' ('codigo_pasantia')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=52165 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'jurado'
--

CREATE TABLE IF NOT EXISTS 'jurado' (
    'usbid' varchar(254) NOT NULL DEFAULT '',
    PRIMARY KEY ('usbid')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'log'
--

CREATE TABLE IF NOT EXISTS 'log' (
    'id_log'        int(254)        NOT NULL AUTO_INCREMENT,
    'consulta'      varchar(2540)   NOT NULL,
    'ip'            varchar(50)     NOT NULL,
    'fecha'         timestamp       NOT NULL DEFAULT CURRENT_TIMESTAMP,
    'usbid_usuario' varchar(254)    NOT NULL,
    PRIMARY KEY ('id_log')
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=440647 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'pasantia'
--

CREATE TABLE IF NOT EXISTS 'pasantia' (
    'codigo'                        varchar(8)      NOT NULL DEFAULT '',
    'periodo'                       int(10)         NOT NULL,
    'anho'                          int(11)         NOT NULL,
    'fecha'                         date            NOT NULL,
    'cod_seguridad'                 varchar(10)     NOT NULL,
    'titulo'                        varchar(100)    NOT NULL,
    'area_proyecto'                 varchar(254)    NOT NULL,
    'resumen_proyecto'              text            NOT NULL,
    'confidencial'                  text,
    'objetivos'                     text            NOT NULL,
    'calificacion_total'            int(1)          DEFAULT '0',
    'calificacion_tutor_academico'  int(1)          DEFAULT '0',
    'calificacion_tutor_industrial' int(1)          DEFAULT '0',
    'fecha_acta_evaluacion'         date            DEFAULT NULL,
    'periodo_finaliza'              int(11)         NOT NULL,
    'anho_finaliza'                 int(11)         NOT NULL,
    'tiene_mencion'                 tinyint(1)      DEFAULT '0',
    'observacion_mencion'           text,
    'fecha_validacion'              date            DEFAULT NULL,
    'status'                        varchar(10)     NOT NULL,
    'id_tutor_industrial'           varchar(254)    NOT NULL,
    'id_jurado'                     varchar(254)    DEFAULT NULL,
    'id_estudiante'                 varchar(8)      NOT NULL,
    'id_tutor_academico'            varchar(254)    NOT NULL,
    'retirar'                       varchar(15)     DEFAULT NULL,
    'obtencion_pasantia'            tinyint(1)      DEFAULT NULL,
    PRIMARY KEY ('codigo','id_estudiante','anho','periodo'),
    KEY 'fk_pasantia_periodo_periodo_id' ('periodo'),
    KEY 'fk_pasantia_id_tutor_industrial_tutor_industrial_email' ('id_tutor_industrial'),
    KEY 'fk_pasantia_id_tutor_academico_usuario_usbid' ('id_tutor_academico'),
    KEY 'fk_pasantia_id_jurado_usuario_usbid' ('id_jurado'),
    KEY 'fk_pasantia_id_estudiante_estudiante_usbid' ('id_estudiante'),
    KEY 'periodo_finaliza' ('periodo_finaliza')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'periodo'
--

CREATE TABLE IF NOT EXISTS 'periodo' (
    'id'        int(10)         NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(255)    NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=9 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'permiso'
--

CREATE TABLE IF NOT EXISTS 'permiso' (
    'codigo'                int(11)     NOT NULL AUTO_INCREMENT,
    'fecha'                 date        NOT NULL,
    'codigo_seguridad'      varchar(10) NOT NULL,
    'tipo_permiso'          varchar(30) NOT NULL,
    'fecha_propuesta'       date        DEFAULT NULL,
    'justificacion'         text        NOT NULL,
    'observaciones_cctds'   text,
    'status'                varchar(10) DEFAULT 'Pendiente',
    PRIMARY KEY ('codigo')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2609 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'preinscripcion'
-- #####################################################################################################################################################3
CREATE TABLE IF NOT EXISTS 'preinscripcion' (
    'id'                int(10)         NOT NULL AUTO_INCREMENT,
    'id_periodo'        int(10)         NOT NULL,
    'anio'              int(4)          NOT NULL,
    'bloque'            varchar(1)      NOT NULL,
    'codigo'            varchar(7)      NOT NULL,
    'usbid'             varchar(254)    NOT NULL,
    'fecha_ingreso'     date            NOT NULL,
    'fecha_validacion'  date            DEFAULT NULL,
    'colocacion'        tinyint(1)      NOT NULL,
    'id_region'         int(10)         DEFAULT NULL,
    'id_estado'         int(10)         DEFAULT NULL,
    'validada'          tinyint(1)      DEFAULT '0',
    'cod_seguridad'     varchar(10)     NOT NULL,
    PRIMARY KEY ('id'),
    KEY 'fk_preinscripcion_usbid_usuario_usbid' ('usbid'),
    KEY 'fk_preinscripcion_id_periodo_periodo_id' ('id_periodo'),
    KEY 'fk_preinscripcion_id_region_region_id' ('id_region'),
    KEY 'fk_preinscripcion_id_estado_estado_id' ('id_estado'),
    KEY 'fk_preinscripcion_codigo_tipo_pasantia_codigo' ('codigo')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3065 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'region'
--

CREATE TABLE IF NOT EXISTS 'region' (
    'id'        int(10)         NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(255)    NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'rol_sistema'
--

CREATE TABLE IF NOT EXISTS 'rol_sistema' (
    'usbid'             varchar(254)    NOT NULL DEFAULT '',
    'nombre'            varchar(254)    NOT NULL,
    'apellido'          varchar(254)    NOT NULL,
    'rol'               varchar(254)    NOT NULL,
    'sede'              varchar(20)     NOT NULL,
    'longitudCarnet'    int(11)         NOT NULL,
    PRIMARY KEY ('usbid')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'solicita_permiso'
--

CREATE TABLE IF NOT EXISTS 'solicita_permiso' (
    'usbid_estudiante'  varchar(8)  NOT NULL,
    'codigo_permiso'    int(11)     NOT NULL,
    'codigo_pasantia'   varchar(8)  NOT NULL DEFAULT '',
    'id_periodo'        int(10)     NOT NULL DEFAULT '0',
    'anho'              int(11)     NOT NULL DEFAULT '0',
    PRIMARY KEY ('usbid_estudiante','codigo_permiso','codigo_pasantia','id_periodo','anho'),
    KEY 'fk_solicita_permiso_codigo_pasantia_tipo_pasantia_codigo' ('codigo_pasantia'),
    KEY 'fk_solicita_permiso_id_periodo_periodo_id' ('id_periodo'),
    KEY 'fk_solicita_permiso_codigo_permiso_permiso_codigo' ('codigo_permiso')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'solicitud_pasante'
--

CREATE TABLE IF NOT EXISTS 'solicitud_pasante' (
    'codigo'        int(11)         NOT NULL AUTO_INCREMENT,
    'id_empresa'    varchar(254)    NOT NULL,
    'cantidad'      int(11)         NOT NULL,
    'id_carrera'    varchar(4)      NOT NULL,
    'fecha'         date            NOT NULL,
    'status'        varchar(10)     DEFAULT 'Pendiente',
    PRIMARY KEY ('codigo'),
    KEY 'fk_solicitud_pasante_carrera_carrea_codigo' ('id_carrera'),
    KEY 'fk_solicitud_pasante_id_empresa_empresa_login' ('id_empresa')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1227 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'tipo_pasantia'
--

CREATE TABLE IF NOT EXISTS 'tipo_pasantia' (
    'codigo'    varchar(8)      NOT NULL DEFAULT '',
    'nombre'    varchar(200)    DEFAULT NULL,
    PRIMARY KEY ('codigo')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'trimestre'
--

CREATE TABLE IF NOT EXISTS 'trimestre' (
    'codigo' int(4)         NOT NULL AUTO_INCREMENT,
    'nombre' varchar(30)    NOT NULL,
    PRIMARY KEY ('codigo')
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'trimestre_periodo'
--

CREATE TABLE IF NOT EXISTS 'trimestre_periodo' (
    'codigo_trimestre'  int(4)  NOT NULL,
    'id_periodo'            int(10) NOT NULL,
    PRIMARY KEY ('codigo_trimestre','id_periodo'),
    KEY 'fk_codigo_trimestre_trimestre_codigo' ('codigo_trimestre'),
    KEY 'fk_id_periodo_periodo_id' ('id_periodo')
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'tutor_academico'
--

CREATE TABLE IF NOT EXISTS 'tutor_academico' (
    'usbid'         varchar(254) NOT NULL DEFAULT '',
    'motivo_retiro' text         NOT NULL,
    PRIMARY KEY ('usbid')

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'tutor_industrial'
--

CREATE TABLE IF NOT EXISTS 'tutor_industrial' (
    'email'                     varchar(254)    NOT NULL,
    'nombre'                    varchar(254)    DEFAULT NULL,
    'apellido'                  varchar(254)    DEFAULT NULL,
    'ci'                        varchar(8)      DEFAULT NULL,
    'password'                  varchar(254)    DEFAULT NULL,
    'pregunta_secreta'          varchar(254)    NOT NULL,
    'respuesta_pregunta_secreta'varchar(254)    NOT NULL,
    'empresa'                   varchar(254)    DEFAULT NULL,
    'pagWeb_empresa'            varchar(254)    DEFAULT NULL,
    'descripcion_empresa'       varchar(254)    DEFAULT NULL,
    'profesion'                 varchar(50)     NOT NULL,
    'cargo'                     varchar(50)     NOT NULL,
    'departamento'              varchar(50)     NOT NULL,
    'direccion'                 varchar(254)    NOT NULL,
    'id_estado'                 int(2)          DEFAULT NULL,
    'telefono'                  varchar(20)     NOT NULL,
    'contactoRRHH'              varchar(20)     DEFAULT NULL,
    'motivo_retiro'             text            NOT NULL,
    PRIMARY KEY ('email'),
    KEY 'fk_tutor_industrial_id_estado_estado_nombre' ('id_estado')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'tutor_industrial_temp'
--

CREATE TABLE IF NOT EXISTS 'tutor_industrial_temp' (
    'id'            int(11)         NOT NULL AUTO_INCREMENT,
    'email'         varchar(50)     NOT NULL,
    'nombre'        varchar(50)     NOT NULL,
    'apellido'      varchar(50)     NOT NULL,
    'profesion'     varchar(50)     NOT NULL,
    'empresa'       varchar(50)     NOT NULL,
    'cargo'         varchar(100)    NOT NULL,
    'departamento'  varchar(100)    NOT NULL,
    'telefono'      varchar(20)     NOT NULL,
    'estado'        varchar(20)     NOT NULL,
    'direccion'     varchar(200)    NOT NULL,
    'codSeg'        varchar(100)    NOT NULL,
    'motivo_retiro' text            NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1915 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'usuario'
--

CREATE TABLE IF NOT EXISTS 'usuario' (
    'usbid'     varchar(254)    NOT NULL,
    'nombre'    varchar(254)    NOT NULL,
    'apellido'  varchar(254)    NOT NULL,
    'ci'        varchar(8)      DEFAULT NULL,
    'tipo'      varchar(15)     DEFAULT NULL,
    PRIMARY KEY ('usbid')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'usuario_estudiante'
--

CREATE TABLE IF NOT EXISTS 'usuario_estudiante' (
    'usbid_usuario'     varchar(254)    NOT NULL,
    'carnet'            varchar(8)      NOT NULL,
    'cohorte'           varchar(2)      DEFAULT NULL,
    'carrera'           varchar(4)      DEFAULT NULL,
    'estudiante_sede'   varchar(11)     DEFAULT NULL,
    'email_sec'         varchar(254)    NOT NULL,
    'telf_hab'          varchar(20)     DEFAULT NULL,
    'telf_cel'          varchar(20)     DEFAULT NULL,
    'direccion'         text,
    'sexo'              varchar(1)      DEFAULT NULL,
    'motivo_retiro'     text            NOT NULL,
    PRIMARY KEY ('usbid_usuario'),
    KEY 'fk_usuario_estudiante_carrera_carrera_codigo' ('carrera')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'usuario_profesor'
--

CREATE TABLE IF NOT EXISTS 'usuario_profesor' (
    'usbid_usuario' varchar(254)    NOT NULL,
    'dependencia'   int(11)         DEFAULT NULL,
    'dedicacion'    int(11)         DEFAULT NULL,
    'categoria'     int(11)         DEFAULT NULL,
    'email_sec'     varchar(254)    DEFAULT NULL,
    'telf'          varchar(20)     DEFAULT NULL,
    'celular'       varchar(20)     DEFAULT NULL,
    'activo'        tinyint(11)     DEFAULT '1',
    PRIMARY KEY ('usbid_usuario'),
    KEY 'fk_usuario_profesor_dependencia_categoria_id' ('dependencia'),
    KEY 'fk_usuario_profesor_categoria_categoria_id' ('categoria'),
    KEY 'fk_usuario_profesor_dedicacion_dedicacion_id' ('dedicacion')
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'zona'
--

CREATE TABLE IF NOT EXISTS 'zona' (
    'id'        int(11)     NOT NULL AUTO_INCREMENT,
    'nombre'    varchar(10) NOT NULL,
    PRIMARY KEY ('id')
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'curriculum'
--

CREATE TABLE IF NOT EXISTS 'curriculum' (
    'usbid'         varchar(254)    NOT NULL,
    'nombre'        varchar(254)    NOT NULL,
    'apellido'      varchar(254)    NOT NULL,
    'ci'            varchar(8)      DEFAULT NULL,
    'carrera'       varchar(4)      DEFAULT NULL,
    'anio_ingreso'  varchar(2)      DEFAULT NULL,
    'telf_cel'      varchar(20)     DEFAULT NULL,
    'telf_hab'      varchar(20)     DEFAULT NULL,
    'email'         varchar(254)    NOT NULL,
    'direccion'     text,
    'electiva'      text,
    'cursos'        text,
    'conocimientos' text,
    'idiomas'       text,
    'aficiones'     text,
    -- 'foto'
    PRIMARY KEY ('usbid'),
    KEY 'fk_curriculum_usbid_usuario_estudiante_usbid' ('usbid'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_nombre' ('nombre'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_apellido' ('apellido'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_ci' ('ci'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_cohorte' ('anio_ingreso'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_telf_cel' ('telf_cel'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_telf_hab' ('telf_hab'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_email' ('email'),
    KEY 'fk_curriculum_nombre_usuario_estudiante_direccion' ('direccion'),
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla 'actividad'
--
ALTER TABLE 'actividad'
    ADD CONSTRAINT 'fk_actividad_codigo_fase_fase_codigo' FOREIGN KEY ('codigo_fase') REFERENCES 'fase' ('codigo') ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla 'calculo_pago'
--
ALTER TABLE 'calculo_pago'
    ADD CONSTRAINT 'fk_calculo_pago_id_categoria_categoria_id' FOREIGN KEY ('id_categoria') REFERENCES 'categoria' ('id') ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_calculo_pago_id_tipo_pasantia_tipo_pasantia_codigo' FOREIGN KEY ('id_tipo_pasantia') REFERENCES 'tipo_pasantia' ('codigo') ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_calculo_pago_id_zona_zona_id' FOREIGN KEY ('id_zona') REFERENCES 'zona' ('id') ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla 'departamento'
--
ALTER TABLE 'departamento'
    ADD CONSTRAINT 'fk_departamento_id_division_id' FOREIGN KEY ('id_division') REFERENCES 'division' ('id') ON UPDATE CASCADE;

--
-- Filtros para la tabla 'estado'
--
ALTER TABLE 'estado'
    ADD CONSTRAINT 'fk_estado_id_zona_zona_id' FOREIGN KEY ('id_zona') REFERENCES 'zona' ('id') ON UPDATE CASCADE;

--
-- Filtros para la tabla 'fase'
--
ALTER TABLE 'fase'
    ADD CONSTRAINT 'fk_fase_codigo_pasantia_tipo_pasantia_codigo' FOREIGN KEY ('codigo_pasantia') REFERENCES 'tipo_pasantia' ('codigo') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_fase_id_estudiante_estudiante_usbid' FOREIGN KEY ('id_estudiante') REFERENCES 'usuario' ('usbid'),
    ADD CONSTRAINT 'fk_fase_id_periodo_periodo_id' FOREIGN KEY ('id_periodo') REFERENCES 'periodo' ('id') ON UPDATE CASCADE;

--
-- Filtros para la tabla 'jurado'
--
ALTER TABLE 'jurado'
    ADD CONSTRAINT 'fk_jurado_usbid_usuario_usbid' FOREIGN KEY ('usbid') REFERENCES 'usuario' ('usbid');

--
-- Filtros para la tabla 'pasantia'
--
ALTER TABLE 'pasantia'
    ADD CONSTRAINT 'fk_pasantia_codigo_tipo_pasantia_codigo' FOREIGN KEY ('codigo') REFERENCES 'tipo_pasantia' ('codigo') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_pasantia_id_estudiante_estudiante_usbid' FOREIGN KEY ('id_estudiante') REFERENCES 'usuario' ('usbid'),
    ADD CONSTRAINT 'fk_pasantia_id_jurado_usuario_usbid' FOREIGN KEY ('id_jurado') REFERENCES 'usuario' ('usbid'),
    ADD CONSTRAINT 'fk_pasantia_id_tutor_academico_usuario_usbid' FOREIGN KEY ('id_tutor_academico') REFERENCES 'usuario' ('usbid'),
    ADD CONSTRAINT 'fk_pasantia_id_tutor_industrial_tutor_industrial_email' FOREIGN KEY ('id_tutor_industrial') REFERENCES 'tutor_industrial' ('email'),
    ADD CONSTRAINT 'fk_pasantia_periodo_periodo_id' FOREIGN KEY ('periodo') REFERENCES 'periodo' ('id') ON UPDATE CASCADE;

--
-- Filtros para la tabla 'preinscripcion'
--
ALTER TABLE 'preinscripcion'
    ADD CONSTRAINT 'fk_preinscripcion_codigo_tipo_pasantia_codigo' FOREIGN KEY ('codigo') REFERENCES 'tipo_pasantia' ('codigo') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_preinscripcion_id_estado_estado_id' FOREIGN KEY ('id_estado') REFERENCES 'estado' ('id') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_preinscripcion_id_periodo_periodo_id' FOREIGN KEY ('id_periodo') REFERENCES 'periodo' ('id') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_preinscripcion_id_region_region_id' FOREIGN KEY ('id_region') REFERENCES 'region' ('id') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_preinscripcion_usbid_usuario_usbid' FOREIGN KEY ('usbid') REFERENCES 'usuario' ('usbid');

--
-- Filtros para la tabla 'solicita_permiso'
--
ALTER TABLE 'solicita_permiso'
    ADD CONSTRAINT 'fk_solicita_permiso_codigo_pasantia_tipo_pasantia_codigo' FOREIGN KEY ('codigo_pasantia') REFERENCES 'tipo_pasantia' ('codigo'),
    ADD CONSTRAINT 'fk_solicita_permiso_codigo_permiso_permiso_codigo' FOREIGN KEY ('codigo_permiso') REFERENCES 'permiso' ('codigo') ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_solicita_permiso_id_periodo_periodo_id' FOREIGN KEY ('id_periodo') REFERENCES 'periodo' ('id') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_solicita_permiso_usbid_estudiante_usuario_usbid' FOREIGN KEY ('usbid_estudiante') REFERENCES 'usuario' ('usbid');

--
-- Filtros para la tabla 'solicitud_pasante'
--
ALTER TABLE 'solicitud_pasante'
    ADD CONSTRAINT 'fk_solicitud_pasante_carrera_carrea_codigo' FOREIGN KEY ('id_carrera') REFERENCES 'carrera' ('codigo') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_solicitud_pasante_id_empresa_empresa_login' FOREIGN KEY ('id_empresa') REFERENCES 'empresa' ('login') ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla 'tutor_academico'
--
ALTER TABLE 'tutor_academico'
    ADD CONSTRAINT 'fk_tutor_academico_usbid_usuario_usbid' FOREIGN KEY ('usbid') REFERENCES 'usuario' ('usbid');

--
-- Filtros para la tabla 'tutor_industrial'
--
ALTER TABLE 'tutor_industrial'
    ADD CONSTRAINT 'fk_tutor_industrial_id_estado_estado_nombre' FOREIGN KEY ('id_estado') REFERENCES 'estado' ('id') ON UPDATE CASCADE;

--
-- Filtros para la tabla 'usuario_estudiante'
--
ALTER TABLE 'usuario_estudiante'
    ADD CONSTRAINT 'fk_usuario_estudiante_carrera_carrera_codigo' FOREIGN KEY ('carrera') REFERENCES 'carrera' ('codigo') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_usuario_estudiante_usbid_usuario_usuario_usbid' FOREIGN KEY ('usbid_usuario') REFERENCES 'usuario' ('usbid');

--
-- Filtros para la tabla 'usuario_profesor'
--
ALTER TABLE 'usuario_profesor'
    ADD CONSTRAINT 'fk_usuario_profesor_categoria_categoria_id' FOREIGN KEY ('categoria') REFERENCES 'categoria' ('id') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_usuario_profesor_dedicacion_dedicacion_id' FOREIGN KEY ('dedicacion') REFERENCES 'dedicacion' ('id') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_usuario_profesor_dependencia_categoria_id' FOREIGN KEY ('dependencia') REFERENCES 'departamento' ('id') ON UPDATE CASCADE,
    ADD CONSTRAINT 'fk_usuario_profesor_usbid_usuario_usuario_usbid' FOREIGN KEY ('usbid_usuario') REFERENCES 'usuario' ('usbid');

--
-- Filtros para la tabla 'curriculum'
--
ALTER TABLE 'curriculum'
    ADD CONSTRAINT 'fk_curriculum_usbid_usuario_estudiante_usbid' FOREIGN KEY ('usbid') REFERENCES 'usuario' ('usbid'); 
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_nombre' FOREIGN KEY ('nombre') REFERENCES 'usuario' ('nombre');
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_apellido' FOREIGN KEY ('apellido') REFERENCES 'usuario' ('apellido');
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_ci' FOREIGN KEY ('ci') REFERENCES 'usuario' ('ci');
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_cohorte' FOREIGN KEY ('anio_ingreso') REFERENCES 'usuario_estudiante' ('cohorte');
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_telf_cel' FOREIGN KEY ('telf_cel') REFERENCES 'usuario_estudiante' ('telf_cel') ON UPDATE CASCADE;
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_telf_hab' FOREIGN KEY ('telf_hab') REFERENCES 'usuario_estudiante' ('telf_hab') ON UPDATE CASCADE;
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_email' FOREIGN KEY ('email') REFERENCES 'usuario_estudiante' ('email_sec') ON UPDATE CASCADE;
    ADD CONSTRAINT 'fk_curriculum_nombre_usuario_estudiante_direccion' FOREIGN KEY ('direccion') REFERENCES 'usuario_estudiante' ('direccion') ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
