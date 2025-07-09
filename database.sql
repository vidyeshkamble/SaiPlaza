-- mysql -u myVidyesh -p -h myVidyesh.mysql.pythonanywhere-services.com

USE myVidyesh$default;

DROP TABLE IF EXISTS `bill`;

CREATE TABLE `bill` (
  `BillNo` varchar(50) NOT NULL,
  `user_id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `email_id` varchar(45) NOT NULL,
  `PhoneNo` int NOT NULL,
  `Amount` int NOT NULL,
  `OSAmount` int NOT NULL,
  `month` varchar(45) DEFAULT NULL,
  `paymentDatetime` varchar(45) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`BillNo`)
);


DROP TABLE IF EXISTS `calculator`;

CREATE TABLE `calculator` (
  `Month` varchar(10) NOT NULL,
  `FlatNo` int NOT NULL,
  `Name` varchar(45) NOT NULL,
  `CurrentPayable` int NOT NULL,
  `PaymentDone` int NOT NULL,
  `OSAmount` int NOT NULL
);


DROP TABLE IF EXISTS `chatbox`;

CREATE TABLE `chatbox` (
  `flatno` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `message` varchar(5000) NOT NULL,
  `datetime` datetime NOT NULL
);

DROP TABLE IF EXISTS `customer`;

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
);

INSERT INTO `customer` VALUES (101,'Sai@123',101,0,'xxx@gmail.com','Mr. Patil Sir',1000,'1'),(102,'Sai@123',102,0,'xxx@gmail.com','Mr. Eknath K. B.',1000,'2'),(103,'Sai@123',103,0,'xxx@gmail.com','Mr. Nandan Nagesh Kumar',1000,'3'),(201,'Sai@123',201,0,'xxx@gmail.com','Mr. Ashok Bihari',1000,'4'),(202,'Sai@123',202,0,'xxx@gmail.com','Mr. Deepak Kumar',1000,'5'),(203,'Sai@123',203,0,'xxx@gmail.com','Mr. Bhusampure Tripathi',1000,'6'),(301,'Sai@123',301,0,'xxx@gmail.com','Mr. Harish D. Shakya',1000,'7'),(302,'Sai@123',302,0,'xxx@gmail.com','Mr. Govind Sawant',1000,'8'),(303,'Sai@123',303,0,'xxx@gmail.com','Mr. Yogesh Jadhav',1000,'9'),(401,'Sai@123',401,0,'xxx@gmail.com','Mr. Vishal Shinde',1000,'10'),(402,'Sai@123',402,0,'xxx@gmail.com','Mrs. Avani K. Kelapure',1000,'11'),(403,'Sai@123',403,0,'xxx@gmail.com','Mrs. Nandini R. Pawar',1000,'12'),(501,'Sai@123',501,0,'xxx@gmail.com','Mr. Ramesh R. Shinde',1000,'13'),(502,'Sai@123',502,0,'xxx@gmail.com','Mr. Jawaharlal Singh',1000,'14'),(503,'Sai@123',503,0,'xxx@gmail.com','Mrs. Pratibha A. Bagul',1000,'15'),(601,'Sai@123',601,0,'xxx@gmail.com','Mr. Ashish R. Vidyadhakar',1000,'16'),(602,'Sai@123',602,0,'xxx@gmail.com','Mr. Raju K. Shinde',1000,'17'),(603,'Sai@123',603,0,'xxx@gmail.com','Mr. Anil K. Kadam',1000,'18'),(701,'Sai@123',701,0,'xxx@gmail.com','Mr. Anant Kamble',1000,'19'),(702,'Sai@123',702,0,'xxx@gmail.com','Mr. Manoj Kumar',1000,'20'),(703,'Sai@123',703,0,'xxx@gmail.com','Mr. Prashant Bagul',1000,'21');


DROP TABLE IF EXISTS `images`;

CREATE TABLE `images` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `image_data` longblob,
  `flatno` varchar(3) DEFAULT NULL
);

DROP TABLE IF EXISTS `payementmode`;

CREATE TABLE `payementmode` (
  `upi_id` varchar(45) NOT NULL,
  `flatno` varchar(10) NOT NULL
);