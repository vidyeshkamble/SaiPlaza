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
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `UserId` int NOT NULL,
  `Password` varchar(50) NOT NULL,
  `FlatNo` int NOT NULL,
  `PhoneNo` int NOT NULL,
  `EmailId` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `OSAmount` int NOT NULL DEFAULT '0',
  `Srno` varchar(45) NOT NULL,
  PRIMARY KEY (`UserId`,`Srno`),
  KEY `Os_idx` (`OSAmount`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (101,'Sai@123',101,0,'xxx@gmail.com','Mr. Patil Sir',1000,'1'),(102,'Sai@123',102,0,'xxx@gmail.com','Mr. Eknath K. B.',1000,'2'),(103,'Sai@123',103,0,'xxx@gmail.com','Mr. Nandan Nagesh Kumar',1000,'3'),(201,'Sai@123',201,0,'xxx@gmail.com','Mr. Ashok Bihari',1000,'4'),(202,'Sai@123',202,0,'xxx@gmail.com','Mr. Deepak Kumar',1000,'5'),(203,'Sai@123',203,0,'xxx@gmail.com','Mr. Bhusampure Tripathi',1000,'6'),(301,'Sai@123',301,0,'xxx@gmail.com','Mr. Harish D. Shakya',1000,'7'),(302,'Sai@123',302,0,'xxx@gmail.com','Mr. Govind Sawant',1000,'8'),(303,'Sai@123',303,0,'xxx@gmail.com','Mr. Yogesh Jadhav',1000,'9'),(401,'Sai@123',401,0,'xxx@gmail.com','Mr. Vishal Shinde',1000,'10'),(402,'Sai@123',402,0,'xxx@gmail.com','Mrs. Avani K. Kelapure',1000,'11'),(403,'Sai@123',403,0,'xxx@gmail.com','Mrs. Nandini R. Pawar',1000,'12'),(501,'Sai@123',501,0,'xxx@gmail.com','Mr. Ramesh R. Shinde',1000,'13'),(502,'Sai@123',502,0,'xxx@gmail.com','Mr. Jawaharlal Singh',1000,'14'),(503,'Sai@123',503,0,'xxx@gmail.com','Mrs. Pratibha A. Bagul',1000,'15'),(601,'Sai@123',601,0,'xxx@gmail.com','Mr. Ashish R. Vidyadhakar',1000,'16'),(602,'Sai@123',602,0,'xxx@gmail.com','Mr. Raju K. Shinde',1000,'17'),(603,'Sai@123',603,0,'xxx@gmail.com','Mr. Anil K. Kadam',1000,'18'),(701,'Sai@123',701,0,'xxx@gmail.com','Mr. Anant Kamble',1000,'19'),(702,'Sai@123',702,0,'xxx@gmail.com','Mr. Manoj Kumar',1000,'20'),(703,'Sai@123',703,0,'xxx@gmail.com','Mr. Prashant Bagul',1000,'21');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-06 18:01:41
