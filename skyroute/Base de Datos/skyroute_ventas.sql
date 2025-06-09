CREATE DATABASE  IF NOT EXISTS `skyroute` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `skyroute`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: skyroute
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cuit_cliente` varchar(13) NOT NULL,
  `id_destino` int NOT NULL,
  `fecha_viaje` date NOT NULL,
  `estado` enum('activa','anulada') DEFAULT 'activa',
  `fecha_registro` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `tipo_anulacion` enum('admin','arrepentimiento') DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cuit_cliente` (`cuit_cliente`),
  KEY `id_destino` (`id_destino`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`cuit_cliente`) REFERENCES `clientes` (`cuit`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`id_destino`) REFERENCES `destinos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,'20282705967',5,'2025-08-03','anulada','2025-06-08 05:53:26','arrepentimiento'),(2,'20282705967',2,'2025-09-03','activa','2025-06-08 05:53:26',NULL),(3,'20282705967',3,'2025-10-03','anulada','2025-06-08 05:53:26','admin'),(4,'27294634024',1,'2025-12-10','anulada','2025-06-08 05:53:26',NULL),(5,'20282705967',3,'2025-12-08','activa','2025-06-08 05:53:26',NULL),(6,'20282705967',3,'2025-12-20','activa','2025-06-08 05:53:26',NULL),(7,'20282705967',4,'2026-01-01','activa','2025-06-08 05:53:26',NULL),(8,'27294634024',3,'2026-01-02','activa','2025-06-08 05:53:26',NULL),(9,'27294634024',5,'2025-08-03','activa','2025-06-08 05:53:26',NULL),(12,'27119734342',4,'2025-12-24','anulada','2025-06-08 08:21:19','arrepentimiento'),(14,'27294634024',10,'2026-01-01','activa','2025-06-08 18:55:10',NULL),(15,'20282705967',1,'2025-07-03','activa','2025-06-08 18:58:10',NULL),(16,'27294634024',1,'2026-12-08','activa','2025-06-08 19:36:14',NULL),(17,'27119734342',10,'2025-10-03','anulada','2025-06-08 20:38:11','arrepentimiento'),(18,'27119734342',10,'2025-12-08','activa','2025-06-08 20:40:33',NULL),(19,'20282705967',10,'2025-12-25','activa','2025-06-08 20:59:49',NULL);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-08 20:57:58
