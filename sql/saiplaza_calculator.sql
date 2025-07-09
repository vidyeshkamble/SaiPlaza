-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: saiplaza
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `calculator`
--

DROP TABLE IF EXISTS `calculator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calculator` (
  `Month` varchar(10) NOT NULL,
  `FlatNo` int NOT NULL,
  `Name` varchar(45) NOT NULL,
  `CurrentPayable` int NOT NULL,
  `PaymentDone` int NOT NULL,
  `OSAmount` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calculator`
--

LOCK TABLES `calculator` WRITE;
/*!40000 ALTER TABLE `calculator` DISABLE KEYS */;
INSERT INTO `calculator` VALUES ('2025-06',101,'Mr. Patil Sir',1000,0,0),('2025-06',102,'Mr. Eknath K. B.',1000,0,0),('2025-06',103,'Mr. Nandan Nagesh Kumar',1000,0,0),('2025-06',201,'Mr. Ashok Bihari',1000,0,0),('2025-06',202,'Mr. Deepak Kumar',1000,0,0),('2025-06',203,'Mr. Bhusampure Tripathi',1000,0,0),('2025-06',301,'Mr. Harish D. Shakya',1000,0,0),('2025-06',302,'Mr. Govind Sawant',1000,0,0),('2025-06',303,'Mr. Yogesh Jadhav',1000,0,0),('2025-06',401,'Mr. Vishal Shinde',1000,0,0),('2025-06',402,'Mrs. Avani K. Kelapure',1000,0,0),('2025-06',403,'Mrs. Nandini R. Pawar',1000,0,0),('2025-06',501,'Mr. Ramesh R. Shinde',1000,0,0),('2025-06',502,'Mr. Jawaharlal Singh',1000,0,0),('2025-06',503,'Mrs. Pratibha A. Bagul',1000,0,0),('2025-06',601,'Mr. Ashish R. Vidyadhakar',1000,0,0),('2025-06',602,'Mr. Raju K. Shinde',1000,0,0),('2025-06',603,'Mr. Anil K. Kadam',1000,0,0),('2025-06',701,'Mr. Anant Kamble',1000,0,0),('2025-06',702,'Mr. Manoj Kumar',1000,0,0),('2025-06',703,'Mr. Prashant Bagul',1000,0,0);
/*!40000 ALTER TABLE `calculator` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-06 18:01:42
