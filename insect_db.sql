-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 06-04-2024 a las 18:54:23
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `insect_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciclo_vida`
--

DROP TABLE IF EXISTS `ciclo_vida`;
CREATE TABLE IF NOT EXISTS `ciclo_vida` (
  `CICLO_VIDA_ID` int(10) NOT NULL AUTO_INCREMENT,
  `ETAPAS` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `DURACION` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `DESCRIPCION` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `FACTORES` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `COMPORTAMIENTOS` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`CICLO_VIDA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ciclo_vida`
--

INSERT INTO `ciclo_vida` (`CICLO_VIDA_ID`, `ETAPAS`, `DURACION`, `DESCRIPCION`, `FACTORES`, `COMPORTAMIENTOS`) VALUES
(1, 'Huevo, larva, pupa, adulto.', 'Varia según la especie y las condiciones ambientales.\r\n', 'Similar a otras especies de insectos.', 'Temperatura, humedad, disponibilidad de alimentos, depredadores, entre otros.', 'Cuidado de la crea, búsqueda de alimentos, defensa del nido, entre otros.'),
(2, 'Huevo, larva, pupa, adulto.', 'Varia según la especie y las condiciones ambientales.', 'Similar a otras especies de insectos.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Cuidado de la crea, recolección de néctar y polen, defensa del nido, entre otros.'),
(3, 'Huevo, larva (oruga), pupa (crisálida), adulto (imago).', 'Varia según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la larva (oruga), la pupa (crisÃ¡lida) y el adulto (imago).', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Búsqueda de alimento, reproducción, búsqueda de sitios de oviposición, migración (en algunas especies).'),
(4, 'Huevo, larva, pupa, adulto.', 'Varia según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la larva, la pupa y el adulto.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Alimentación, crecimiento, preparación para la metamorfosis.'),
(5, 'Huevo, larva, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la larva y el adulto.', 'La temperatura y la humedad son factores crÃ­ticos para el desarrollo de los huevos y las larvas, mientras que los adultos dependen de la disponibilidad de presas y refugios.', 'Alimentación, reproducción, busqueda de refugio.'),
(6, 'Huevo, ninfa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la ninfa (muda varias veces antes de convertirse en adulto) y el adulto.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Alimentación, reproducción, busqueda de refugio.'),
(7, 'Huevo, ninfa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la ninfa (etapas acuÃ¡ticas) y el adulto.', 'Temperatura, calidad del agua, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Caza de presas, reproducción, búsqueda de refugio.'),
(8, 'Huevo, larva (gusano), pupa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la larva, la pupa y el adulto.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Búsqueda de alimento, reproducción, búsqueda de refugio.'),
(9, 'Huevo, ninfa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la ninfa y el adulto.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Alimentación, reproducción, busqueda de refugio.'),
(10, 'Huevo, larva, pupa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la larva, la pupa y el adulto.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Alimentación, reproducción, busqueda de refugio.'),
(11, 'Huevo, ninfa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la ninfa y el adulto.', 'Temperatura, humedad, disponibilidad de presas, presencia de depredadores y parÃ¡sitos.', 'Caza de presas, reproducción, búsqueda de refugio.'),
(12, 'Huevo, larva, pupa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la larva, la pupa y el adulto.', 'Temperatura, humedad, disponibilidad de agua estancada, presencia de depredadores y parÃ¡sitos.', 'Alimentación, reproducción, busqueda de refugio.'),
(13, 'Huevo, araÃ±a joven (ninfas), araÃ±a adulta.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, las ninfas y el adulto.', 'Temperatura, humedad, disponibilidad de presas, presencia de depredadores y parÃ¡sitos.', 'Caza de presas, reproducción, construcción de telarañas.'),
(14, 'Huevo, larva, pupa, adulto.', 'Varía según la especie y las condiciones ambientales.', 'Las etapas incluyen el huevo, la larva, la pupa y el adulto.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.', 'Caza de presas, reproducción, busqueda de alimento.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clase`
--

DROP TABLE IF EXISTS `clase`;
CREATE TABLE IF NOT EXISTS `clase` (
  `CLASE_ID` int(10) NOT NULL AUTO_INCREMENT,
  `NOMBRE` varchar(200) NOT NULL,
  PRIMARY KEY (`CLASE_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clase`
--

INSERT INTO `clase` (`CLASE_ID`, `NOMBRE`) VALUES
(1, 'INSECTA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dieta`
--

DROP TABLE IF EXISTS `dieta`;
CREATE TABLE IF NOT EXISTS `dieta` (
  `DIETA_ID` int(10) NOT NULL AUTO_INCREMENT,
  `TIPO` longtext CHARACTER SET latin1 NOT NULL,
  `CONSUMIDO` longtext CHARACTER SET latin1 NOT NULL,
  `PREFERENCIAS_ALIMENTACION` longtext CHARACTER SET latin1 NOT NULL,
  `PATRONES_ALIMENTACION` longtext CHARACTER SET latin1 NOT NULL,
  PRIMARY KEY (`DIETA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Volcado de datos para la tabla `dieta`
--

INSERT INTO `dieta` (`DIETA_ID`, `TIPO`, `CONSUMIDO`, `PREFERENCIAS_ALIMENTACION`, `PATRONES_ALIMENTACION`) VALUES
(1, 'Las hormigas son generalmente omnívoras, aunque algunas especies pueden ser herbívoras, carnívoras o necrófagas.', 'Carbohidratos, proteínas, líquidos azucarados, insectos, hojas, semillas, entre otros.', 'Varían según la especie y la disponibilidad de alimentos en su entorno.', 'Depende de la especie, algunas son depredadoras, otras recolectoras, y algunas cultivan hongos para alimentarse.'),
(2, 'Mayormente se alimentan de néctar y polen, aunque algunas especies también pueden consumir otros líquidos y materiales vegetales.', 'Néctar, polen, líquidos azucarados, materiales vegetales.', 'Varían según la especie y la disponibilidad de alimentos en su entorno.', 'Depende de la especie, algunas abejas son especializadas en la recolecciÃ³n de polen, mientras que otras tambiÃ©n recolectan nÃ©ctar y resinas.'),
(3, 'Mayormente se alimentan de néctar de flores, aunque algunas especies también consumen otros líquidos azucarados y minerales disueltos.', 'Néctar de flores, líquidos azucarados, minerales disueltos.', 'Varían según la especie y la disponibilidad de flores en su entorno.', 'Depende de la especie, algunas mariposas son más activas durante el día, mientras que otras son nocturnas.'),
(4, 'Herbívoras', 'Hojas de plantas, brotes, frutos.', 'Varían según la especie y la disponibilidad de alimentos en su entorno.', 'Depende de la especie, algunas orugas son más activas durante el día, mientras que otras son nocturnas.'),
(5, 'Carnívoras', 'Insectos, arañas, pequeños vertebrados, otros invertebrados.', 'Varían según la especie y la disponibilidad de presas en su entorno.', 'Depende de la especie y el comportamiento individual, algunos son cazadores activos mientras que otros pueden ser carroÃ±eros o depredadores de emboscada.'),
(6, 'Mayormente omnívoras, se alimentan de una amplia variedad de alimentos orgánicos y en descomposición, asi­ como de materiales de desecho.', 'Desperdicios de alimentos, materiales en descomposiciÃ³n, papel, cartÃ³n, entre otros.', 'Varían según la especie y la disponibilidad de alimentos en su entorno.', 'Nocturnas, buscan comida principalmente durante la noche.'),
(7, 'Predadoras, se alimentan principalmente de insectos pequeÃ±os, como mosquitos, moscas y mariposas, que cazan en el aire.', 'Mosquitos, moscas, mariposas y otros insectos voladores pequeÃ±os.', 'Se alimentan de insectos que atrapan en vuelo, preferiblemente mientras estÃ¡n en movimiento.', 'Depende de la especie y del hábitat, algunas son cazadoras activas, mientras que otras pueden esperar pacientemente en una percha antes de lanzarse a capturar presas.'),
(8, 'Mayormente son insectos oportunistas y se alimentan de una amplia variedad de materia orgÃ¡nica en descomposiciÃ³n, asÃ­ como de secreciones y excrementos de animales.', 'Materia orgánica en descomposición, secreciones animales, excrementos.', 'Se adaptan a una amplia gama de alimentos disponibles en su entorno, pero prefieren materia orgÃ¡nica en descomposiciÃ³n.', 'Mayormente son activas durante el día y se alimentan de manera continua.'),
(9, 'Mayormente son herbívoros y se alimentan de una amplia variedad de plantas, incluyendo pastos, hierbas y cultivos.', 'Hierbas, pastos, cultivos y otras plantas de bajo crecimiento.', 'Se alimentan de una amplia variedad de plantas, pero algunas especies pueden tener preferencias alimenticias por ciertos tipos de plantas.', 'Mayormente son activos durante el día y se alimentan de manera continua.'),
(10, 'Son depredadoras y se alimentan principalmente de pulgones y otros pequeÃ±os insectos.', 'Pulgones, Ácaros, cochinillas y otros pequeños insectos.', 'Se alimentan principalmente de pulgones, pero tambiÃ©n pueden consumir otros pequeÃ±os insectos.', 'Mayormente son activas durante el día y se alimentan de manera continua.'),
(11, 'Son depredadores y se alimentan principalmente de otros insectos, como moscas, grillos y mariposas.', 'Moscas, grillos, mariposas y otros insectos pequeños.', 'Se alimentan principalmente de insectos, pero pueden consumir una variedad de presas disponibles en su entorno.', 'Mayormente son activos durante el día y cazan presas en movimiento.'),
(12, 'Las hembras se alimentan de sangre para obtener nutrientes para la producciÃ³n de huevos, mientras que los machos se alimentan de nÃ©ctar y otras sustancias azucaradas.', 'Sangre de mamíferos y aves para las hembras; néctar y otras sustancias azucaradas para los machos.', 'Las hembras prefieren alimentarse de sangre para la reproducciÃ³n, mientras que los machos se alimentan de nÃ©ctar.', 'Las hembras se alimentan de sangre principalmente durante el amanecer y el atardecer, mientras que los machos se alimentan de néctar durante el día.'),
(13, 'Son depredadoras y se alimentan principalmente de otros insectos, aunque algunas especies tambiÃ©n pueden consumir pequeÃ±os vertebrados.', 'Insectos, arañas más pequeñas, y en algunos casos, pequeños vertebrados como lagartijas y ratones.', 'Se alimentan principalmente de insectos, pero algunas especies pueden tener preferencias alimenticias por ciertos tipos de presas.', 'Mayormente son activas durante la noche y cazan presas mediante la emboscada o la construcción de telarañas.'),
(14, 'Son carnívoras y se alimentan principalmente de otros insectos, aunque algunas especies pueden consumir néctar y frutas maduras.', 'Otros insectos, larvas, néctar y en algunos casos, frutas maduras.', 'Se alimentan principalmente de otros insectos, pero algunas especies pueden consumir nÃ©ctar y frutas maduras.', 'Mayormente son activas durante el día y cazan presas para alimentar a sus larvas.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `geo_insect`
--

DROP TABLE IF EXISTS `geo_insect`;
CREATE TABLE IF NOT EXISTS `geo_insect` (
  `geo_inset_id` int(10) NOT NULL AUTO_INCREMENT,
  `user` varchar(100) NOT NULL,
  `descripcion` longtext NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `lat` varchar(100) NOT NULL,
  `log` varchar(100) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`geo_inset_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `geo_insect`
--

INSERT INTO `geo_insect` (`geo_inset_id`, `user`, `descripcion`, `titulo`, `lat`, `log`, `fecha`) VALUES
(1, 'Pruebas', 'Pruebas', 'pruebas', '0.0', '0.0', '2024-04-03'),
(4, 'Pruebas2', 'Pruebas de ubicación de insecto', 'Abeja', '10.4230', '-66.9946', '2024-04-04'),
(5, 'Pruebas3', 'Observe una Araña', 'Araña', '5.6324', '-76.6516', '2024-04-05'),
(6, 'alexander', 'Pruebas 3 ', 'Pruebas 3 ', '-17.056785', '-68.115234', '2024-04-06'),
(7, 'Juan', 'la observe las vacaciones ', 'Mosca', '-4.269724', '-56.04126', '2024-04-06'),
(8, 'Andres', 'Pruebas', 'Mariposa', '10.487812', '-71.586914', '2024-04-06'),
(9, 'alex', 'Preubas', 'Pruebas', '3.294082', '-65.67627', '2024-04-06');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habitat`
--

DROP TABLE IF EXISTS `habitat`;
CREATE TABLE IF NOT EXISTS `habitat` (
  `HABITAT_ID` int(10) NOT NULL AUTO_INCREMENT,
  `TIPO` longtext NOT NULL,
  `DESCRIPCION` longtext NOT NULL,
  `TEMPERATURA` longtext NOT NULL,
  `HUMEDAD` longtext NOT NULL,
  `ALTITUD` longtext NOT NULL,
  `PRECIPITACION` longtext NOT NULL,
  `OTROS_FACTORES` longtext NOT NULL,
  PRIMARY KEY (`HABITAT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `habitat`
--

INSERT INTO `habitat` (`HABITAT_ID`, `TIPO`, `DESCRIPCION`, `TEMPERATURA`, `HUMEDAD`, `ALTITUD`, `PRECIPITACION`, `OTROS_FACTORES`) VALUES
(1, 'Varían según la especie, pero pueden encontrarse en bosques, selvas, desiertos, pastizales, e incluso en áreas urbanas.', 'Depende de la especie, pero las hormigas pueden habitar en el suelo, en árboles, en nidos construidos bajo tierra o en la vegetación, entre otros lugares.\r\n', 'Varía según la especie, pero la mayoría prefiere climas cálidos o templados.\r\n', 'También varía según la especie, algunas prefieren ambientes más húmedos mientras que otras son más tolerantes a la sequía.\r\n', 'Pueden encontrarse desde el nivel del mar hasta altitudes elevadas en montañas.\r\n', 'Depende del hábitat y la especie, algunas especies pueden requerir niveles de precipitación más altos que otras.\r\n', '\r\n'),
(2, 'Varí­an según la especie, pero pueden encontrarse en diversos hábitats, desde bosques hasta Áreas urbanas.', 'Construyen sus nidos en cavidades naturales, como huecos de Ã¡rboles, y en estructuras hechas por el hombre, como colmenas.', 'Prefieren climas cÃ¡lidos y templados, aunque hay especies adaptadas a una variedad de climas.', 'Requieren ciertos niveles de humedad para el desarrollo de las larvas y la producciÃ³n de alimentos.', 'Pueden encontrarse desde el nivel del mar hasta altitudes elevadas en montaÃ±as.', 'Depende del hábitat y la especie, algunas abejas prefieren Áreas con una alta disponibilidad de flores.', 'Temperatura, humedad, disponibilidad de alimento, presencia de depredadores y parÃ¡sitos.'),
(3, 'Varían según la especie, pero pueden encontrarse en una amplia variedad de hábitats, desde selvas tropicales hasta praderas alpinas.', 'Depende de la especie, pero suelen habitar en Áreas con abundante vegetaciÃ³n y flores.', 'Varí­a según la especie y la regiÃ³n, pero generalmente se adaptan a una amplia gama de temperaturas, desde cálidas hasta frías.', 'Varí­a según la especie y la región, pero la mayoría prefiere niveles moderados de humedad.', 'Varía según la especie y la región, desde niveles del mar hasta altitudes elevadas en montañas.', 'Depende de la especie y la región, pero la mayoría prefiere Áreas con precipitación moderada.', 'La disponibilidad de alimento y la presencia de depredadores son factores clave para su supervivencia.'),
(4, 'Varí­an según la especie, pero pueden encontrarse en una amplia variedad de hábitats, desde selvas tropicales hasta praderas alpinas.', 'Depende de la especie, pero generalmente se encuentran en Ã¡reas con abundante vegetaciÃ³n.', 'Varía según la especie y la región, pero generalmente se adaptan a una amplia gama de temperaturas, desde cálidas hasta frÃ­as.', 'Varí­a según la especie y la region, pero la mayoría prefiere niveles moderados de humedad.', 'Varía según la especie y la región, desde niveles del mar hasta altitudes elevadas en montañas.', 'Depende de la especie y la región, pero la mayoría prefiere Áreas con precipitación moderada.', 'La disponibilidad de alimento y la presencia de depredadores son factores clave para su supervivencia.'),
(5, 'Varian dependiendo de la especie, pero pueden habitar en una variedad de hábitats, desde bosques húmedos hasta desiertos secos.', 'Los ciempiés prefieren Áreas con cobertura vegetal densa y suelen esconderse bajo rocas, hojarasca, troncos caídos y en el suelo.', 'Varían según la especie y el hábitat, pero muchos ciempiés prefieren temperaturas templadas.', 'Prefieren niveles moderados de humedad, pero algunas especies pueden adaptarse a condiciones mÃ¡s secas.', 'Se pueden encontrar desde el nivel del mar hasta altitudes elevadas, dependiendo de la especie.', 'Depende del hábitat, algunos ciempiés prefieren Áreas con altos niveles de precipitación, mientras que otros pueden sobrevivir en Áreas más secas.', 'La disponibilidad de presas, temperatura, humedad y la presencia de depredadores y parÃ¡sitos son factores importantes para la supervivencia de los ciempiÃ©s.'),
(6, 'Vai­an según la especie, pero suelen habitar en Áreas cálidas y húmedas.', 'Las cucarachas se encuentran comúnmente en ambientes urbanos y domésticos, así como en bosques tropicales y subtropicales.', 'Preferencia por temperaturas cálidas, generalmente entre 25Â°C y 35Â°C.', 'Prefieren niveles de humedad alta, entre el 75% y el 90%.', 'Pueden encontrarse a altitudes que van desde el nivel del mar hasta zonas montaÃ±osas.', 'Depende de la especie y del hábitat, algunas prefieren Áreas con alta humedad y otras pueden sobrevivir en condiciones más secas.', 'La disponibilidad de alimentos, refugio y la presencia de depredadores son factores clave para su supervivencia.'),
(7, 'Suelen habitar cerca de cuerpos de agua dulce, como estanques, lagos y rÃ­os, pero tambiÃ©n pueden encontrarse en Ã¡reas boscosas y de matorrales.', 'Las libélulas se encuentran comúnmente en hábitats acuáticos, como estanques, lagos, ríos y arroyos, pero también pueden habitar en Áreas adyacentes a cuerpos de agua, como praderas y bosques.', 'Preferencia por temperaturas cálidas, generalmente entre 20Â°C y 30Â°C.', 'Prefieren niveles de humedad moderados a altos, típicos de entornos acuáticos.', 'Pueden encontrarse a altitudes que van desde el nivel del mar hasta zonas montañosas.', 'Depende de la especie y del hábitat, algunas prefieren Áreas con alta humedad y otras pueden sobrevivir en condiciones más secas.', 'La disponibilidad de alimento y la calidad del agua son factores importantes para su supervivencia.'),
(8, 'Las moscas pueden encontrarse en una amplia gama de hÃ¡bitats, desde Ã¡reas urbanas hasta bosques y zonas agrÃ­colas.', 'Las moscas suelen habitar en Áreas con una alta disponibilidad de alimentos y refugios, como basureros, establos, Áreas de compostaje y hogares humanos.', 'Prefieren temperaturas cálidas, típicas de entornos urbanos y rurales.', 'Pueden tolerar una amplia gama de niveles de humedad, pero prefieren Ã¡reas con alta humedad relativa.', 'Se encuentran a altitudes que van desde el nivel del mar hasta zonas montaÃ±osas.', 'Depende del hábitat, algunas especies prefieren Áreas con alta precipitaciÃ³n, mientras que otras pueden encontrarse en Áreas más secas.', 'La disponibilidad de alimento, la temperatura y la humedad son factores clave para su supervivencia.'),
(9, 'Los saltamontes pueden habitar una variedad de hábitats, desde praderas y campos agrícolas hasta bosques y zonas urbanas.', 'Los saltamontes se encuentran comúnmente en Áreas abiertas con vegetaciÃ³n alta y dispersa, como praderas, campos agrícolas y pastizales.', 'Prefieren temperaturas cálidas, típicas de climas templados y tropicales.', 'Pueden tolerar una amplia gama de niveles de humedad, pero prefieren Ã¡reas con humedad moderada.', 'Se encuentran a altitudes que van desde el nivel del mar hasta zonas montaÃ±osas.', 'Depende del hábitat, algunos saltamontes prefieren Áreas con alta precipitación, mientras que otros pueden encontrarse en Áreas más secas.', 'La disponibilidad de alimento, la temperatura y la humedad son factores clave para su supervivencia.'),
(10, 'Las mariquitas pueden encontrarse en una variedad de hÃ¡bitats, desde Ã¡reas forestales hasta zonas urbanas y agrÃ­colas.', 'Las mariquitas suelen habitar en Áreas con una abundante oferta de alimentos, como jardines, campos agrícolas y bosques.', 'Prefieren temperaturas moderadas, típicas de climas templados.', 'Pueden encontrarse en una amplia gama de niveles de humedad, pero prefieren Áreas con humedad moderada.', 'Se encuentran a altitudes que van desde el nivel del mar hasta zonas montaÃ±osas.', 'Depende del hábitat, algunas especies prefieren Áreas con alta precipitaciÃ³n, mientras que otras pueden encontrarse en Áreas más secas.', 'La disponibilidad de alimento y la presencia de depredadores son factores clave para su supervivencia.'),
(11, 'Los mantis pueden encontrarse en una variedad de hÃ¡bitats, desde selvas tropicales hasta desiertos Ã¡ridos y zonas urbanas.', 'Los mantis suelen habitar en Áreas con una abundante oferta de presas, como jardines, campos agrÃ­colas y bosques.', 'Prefieren temperaturas cálidas a templadas, típicas de climas tropicales y templados.', 'Pueden encontrarse en una amplia gama de niveles de humedad, pero prefieren Ã¡reas con humedad moderada.', 'Se encuentran a altitudes que van desde el nivel del mar hasta zonas montañosas.', 'Depende del hábitat, algunas especies prefieren Áreas con alta precipitaciÃ³n, mientras que otras pueden encontrarse en Áreas más secas.', 'La disponibilidad de presas y la presencia de depredadores son factores clave para su supervivencia.'),
(12, 'Los zancudos pueden habitar una variedad de hábitats, desde Áreas urbanas hasta selvas tropicales y zonas húmedas.', 'Los zancudos se encuentran comúnmente cerca de cuerpos de agua estancada, como estanques, lagos y charcos, pero también pueden encontrarse en Áreas urbanas y rurales.', 'Prefieren temperaturas cálidas a templadas, típicas de climas tropicales y templados.', 'Prefieren niveles de humedad altos, tÃ­picos de entornos acuÃ¡ticos.', 'Se encuentran a altitudes que van desde el nivel del mar hasta zonas montaÃ±osas.', 'Depende del hábitat, algunas especies prefieren Áreas con alta precipitación, mientras que otras pueden encontrarse en Áreas más secas.', 'La disponibilidad de agua estancada para la reproducciÃ³n y la presencia de depredadores son factores clave para su supervivencia.'),
(13, 'Las arañas pueden habitar una variedad de hábitats, desde selvas tropicales hasta desiertos Áridos y zonas urbanas.', 'Las arañas se encuentran comúnmente en Áreas con una abundante oferta de presas y refugios, como bosques, praderas y Áreas urbanas.', 'Prefieren temperaturas cálidas a templadas, típicas de climas tropicales y templados.', 'Pueden encontrarse en una amplia gama de niveles de humedad, pero prefieren Ã¡reas con humedad moderada.', 'Se encuentran a altitudes que van desde el nivel del mar hasta zonas montaÃ±osas.', 'Depende del hábitat, algunas especies prefieren Áreas con alta precipitación, mientras que otras pueden encontrarse en Áreas más secas.', 'La disponibilidad de presas y la presencia de depredadores son factores clave para su supervivencia.'),
(14, 'Las avispas pueden habitar una variedad de hábitats, desde bosques y praderas hasta zonas urbanas y agrícolas.', 'Las avispas se encuentran comúnmente en Áreas con una abundante oferta de alimento y refugio, como bosques, jardines y Áreas urbanas.', 'Prefieren temperaturas cálidas a templadas, típicas de climas tropicales y templados.', 'Pueden encontrarse en una amplia gama de niveles de humedad, pero prefieren Ã¡reas con humedad moderada.', 'Se encuentran a altitudes que van desde el nivel del mar hasta zonas montañosas.', 'Depende del hábitat, algunas especies prefieren Áreas con alta precipitación, mientras que otras pueden encontrarse en Áreas más secas.', 'La disponibilidad de alimento, la presencia de depredadores y la competencia con otras especies son factores clave para su supervivencia.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `insecto`
--

DROP TABLE IF EXISTS `insecto`;
CREATE TABLE IF NOT EXISTS `insecto` (
  `INSECTO_ID` int(10) NOT NULL AUTO_INCREMENT,
  `NOMBRE_CIENTIFICO` varchar(100) NOT NULL,
  `NOMBRE` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `DESCRIPCION` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `DISTRIBUCION_GEO` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `ESTADO_CONSERVACION` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `LINK_IMAGEN` varchar(200) DEFAULT NULL,
  `CLASE_ID` int(10) NOT NULL,
  `HABITAT_ID` int(10) NOT NULL,
  `DIETA_ID` int(10) NOT NULL,
  `CLICLO_ID` int(10) NOT NULL,
  PRIMARY KEY (`INSECTO_ID`),
  KEY `CLASE_ID` (`CLASE_ID`),
  KEY `HABITAT_ID` (`HABITAT_ID`,`DIETA_ID`,`CLICLO_ID`),
  KEY `CLICLO_ID` (`CLICLO_ID`),
  KEY `DIETA_ID` (`DIETA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `insecto`
--

INSERT INTO `insecto` (`INSECTO_ID`, `NOMBRE_CIENTIFICO`, `NOMBRE`, `DESCRIPCION`, `DISTRIBUCION_GEO`, `ESTADO_CONSERVACION`, `LINK_IMAGEN`, `CLASE_ID`, `HABITAT_ID`, `DIETA_ID`, `CLICLO_ID`) VALUES
(1, 'Formicidae', 'Hormiga', 'Insectos sociales que viven en colonias organizadas con una división clara del trabajo.', 'Presentes en casi todos los hábitats terrestres del mundo, excepto en regiones polares y algunos desiertos extremos.', 'No se consideran en peligro de extinción en general, pero algunas especies pueden estar amenazadas por la destrucción de su hábitat y el cambio climático.', 'https://storage.cloud.google.com/bucket_insect/Insectos/ant.jpg', 1, 1, 1, 1),
(2, 'Apidae', 'Abejas\r\n', 'Insectos polinizadores pertenecientes a la familia Apidae.\r\n', 'Ampliamente distribuidas en todo el mundo, excepto en regiones polares y algunas islas remotas.\r\n', 'Algunas especies de abejas enfrentan amenazas debido a la pérdida de hábitat, el uso de pesticidas y el cambio climático.\r\n', 'https://storage.cloud.google.com/bucket_insect/Insectos/bee.jpg', 1, 2, 2, 2),
(3, 'Lepidoptera', 'Mariposas', 'Insectos con alas membranosas y escamas, conocidos por su belleza y diversidad', 'Presentes en todos los continentes, excepto en la Antártida', 'Algunas especies de mariposas enfrentan amenazas debido a la pérdida de hábitat, el uso de pesticidas y el cambio climático\r\n', 'https://storage.cloud.google.com/bucket_insect/Insectos/buttefly.jpg', 1, 3, 3, 3),
(4, 'Lepidoptera', 'Orugas', 'Fase larval de las mariposas, con cuerpo segmentado y varias patas falsas en la parte posterior', 'Presentes en todos los continentes, excepto en la Antártida', 'Algunas especies de orugas enfrentan amenazas debido a la pérdida de hábitat, el uso de pesticidas y el cambio climático', 'https://storage.cloud.google.com/bucket_insect/Insectos/caterpillar.jpg', 1, 4, 4, 4),
(5, 'Chilopoda', 'Ciempies', 'Los ciempiés son artrópodos alargados con numerosas patas segmentadas y mandíbulas venenosas. Pueden variar en tamaño desde unos pocos milímetros hasta más de 30 centímetros.\r\n', 'Se encuentran en todos los continentes, excepto en la Antártida.\r\n', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/centipede.jpg', 1, 5, 5, 5),
(6, 'Blattodea', 'Cucaracha', 'Insectos de cuerpo plano y marrón oscuro, con antenas largas y patas adaptadas para correr rápidamente.', 'Presentes en todos los continentes, excepto en la Antártida.', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/cockroach.jpg', 1, 6, 6, 6),
(7, 'Odonata', 'Libelula\r\n', 'Insectos voladores con cuerpos alargados y delgados, grandes ojos compuestos y dos pares de alas transparentes', 'Presentes en todos los continentes, excepto en la Antártida', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/dragonfly.jpg', 1, 7, 7, 7),
(8, 'Diptera', 'Mosca', 'Insectos voladores de tamaño pequeño a mediano, con un solo par de alas y un par de halterios', 'Presentes en todos los continentes, en una variedad de hábitats', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/Fly.jpg', 1, 8, 8, 8),
(9, 'Orthoptera', 'Saltamontes', 'Insectos con cuerpo alargado, patas traseras desarrolladas para el salto y antenas largas', 'Presentes en todos los continentes, excepto en la Antártida', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/grasshopper.jpg', 1, 9, 9, 9),
(10, 'Coccinellidae', 'Mariquita', 'Insectos pequeños y redondeados, generalmente de color rojo o naranja con manchas negras en el dorso', 'Presentes en todos los continentes, excepto en la Antártida', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/Ladybug.jpeg', 1, 10, 10, 10),
(11, 'Mantodea', 'Mantis', 'Insectos con cuerpo alargado, cabeza triangular y patas delanteras desarrolladas para atrapar presas', 'Presentes en todos los continentes, excepto en la Antártida', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/Mantis.jpg', 1, 11, 11, 11),
(12, 'Culicidae', 'Zancudo', 'Insectos pequeños con cuerpo delgado, patas largas y antenas largas. Las hembras tienen piezas bucales adaptadas para picar y alimentarse de sangre', 'Presentes en todos los continentes, excepto en la Antártida', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/mosquito.jpg', 1, 12, 12, 12),
(13, 'Araneae', 'Araña', 'Arácnidos con ocho patas, cuerpo dividido en dos segmentos (cefalotórax y abdomen) y capacidad de producir seda', 'Presentes en todos los continentes, excepto en la Antártida', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/Spider.jpg', 1, 13, 13, 13),
(14, 'Hymenoptera', 'Avispa', 'Insectos voladores con abdomen estrecho, antenas largas y a menudo con una coloración amarilla y negra. Algunas especies pueden tener aguijón', 'Presentes en todos los continentes, excepto en la Antártida', 'Especie sin riesgo de extinsion', 'https://storage.cloud.google.com/bucket_insect/Insectos/wasp.jpg', 1, 14, 14, 14);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interaccion_usuario`
--

DROP TABLE IF EXISTS `interaccion_usuario`;
CREATE TABLE IF NOT EXISTS `interaccion_usuario` (
  `interaccion_id` int(11) NOT NULL AUTO_INCREMENT,
  `Titulo` varchar(200) NOT NULL,
  `descricion` longtext NOT NULL,
  `user` varchar(200) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`interaccion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `interaccion_usuario`
--

INSERT INTO `interaccion_usuario` (`interaccion_id`, `Titulo`, `descricion`, `user`, `fecha`) VALUES
(1, 'Descubriendo al Escarabajo Dorado', 'Reciente mente me tope con el Escarabajo Dorado el cual investigando medí cuenta que:  El insecto, que ha sido denominado provisionalmente Escarabajo Auratus, se distingue por su coloración dorada brillante y sus marcados patrones en las alas.', 'Pruebas', '2024-03-04'),
(4, 'Pruebas', 'Pruebas', 'alex', '2024-04-06');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `insecto`
--
ALTER TABLE `insecto`
  ADD CONSTRAINT `insecto_ibfk_1` FOREIGN KEY (`CLASE_ID`) REFERENCES `clase` (`CLASE_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `insecto_ibfk_2` FOREIGN KEY (`CLICLO_ID`) REFERENCES `ciclo_vida` (`CICLO_VIDA_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `insecto_ibfk_3` FOREIGN KEY (`HABITAT_ID`) REFERENCES `habitat` (`HABITAT_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `insecto_ibfk_4` FOREIGN KEY (`DIETA_ID`) REFERENCES `dieta` (`DIETA_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
