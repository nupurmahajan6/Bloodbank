/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - bloodbank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`bloodbank` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `bloodbank`;

/*Table structure for table `addata` */

DROP TABLE IF EXISTS `addata`;

CREATE TABLE `addata` (
  `id` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `UID` varchar(255) default NULL,
  `address1` varchar(255) default NULL,
  `gender1` varchar(255) default NULL,
  `contact1` varchar(255) default NULL,
  `bloodgroup1` varchar(255) default NULL,
  `Division1` varchar(255) default NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `addata` */

insert  into `addata`(`id`,`username`,`email`,`UID`,`address1`,`gender1`,`contact1`,`bloodgroup1`,`Division1`) values (1,'a','rmundekar2000@gmail.com','9465579945466','vashi','Male','9561161391','AB-','mumbai');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(255) NOT NULL auto_increment,
  `usename` varchar(255) default NULL,
  `bloodgroup` varchar(255) default NULL,
  `emailid` varchar(255) default NULL,
  `status` varchar(255) default '"BOOKING REJECTED BY NGO"',
  `feedback` longtext,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`usename`,`bloodgroup`,`emailid`,`status`,`feedback`) values (1,'b','O+','rmundekar2000@gmail.com','\"BOOKING REJECTED BY NGO\"','sorry your age not yet ');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `username` varchar(255) default NULL,
  `latitude` double default NULL,
  `longitude` double default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`username`,`latitude`,`longitude`) values ('a',19.17178081,73.00754999);

/*Table structure for table `ngo_register` */

DROP TABLE IF EXISTS `ngo_register`;

CREATE TABLE `ngo_register` (
  `ngo_username` varchar(255) default NULL,
  `ngo_email` varchar(255) default NULL,
  `ngo_password` varchar(255) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ngo_register` */

insert  into `ngo_register`(`ngo_username`,`ngo_email`,`ngo_password`) values ('ngo','ngo@gmail.com','ngo');

/*Table structure for table `notificationdonors` */

DROP TABLE IF EXISTS `notificationdonors`;

CREATE TABLE `notificationdonors` (
  `hospital` varchar(255) default NULL,
  `bloodgroup` varchar(255) default NULL,
  `address` varchar(255) default NULL,
  `location` varchar(255) default NULL,
  `input_details` varchar(255) default NULL,
  `input_time_confirm` varchar(22) default NULL,
  `email` varchar(255) default NULL,
  `status` varchar(255) default 'Unsuccesful_donation',
  `rewards` varchar(255) default '0',
  `username` varchar(255) default NULL,
  `rate` varchar(255) default '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notificationdonors` */

insert  into `notificationdonors`(`hospital`,`bloodgroup`,`address`,`location`,`input_details`,`input_time_confirm`,`email`,`status`,`rewards`,`username`,`rate`) values ('Ghatkopar ','AB-','sangarsh nagar','mumbai','you are eligible for this ','6:09','rmundekar2000@gmail.com','succesful_donaton','25','a','4.0');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `username` varchar(50) default NULL,
  `email` varchar(50) default NULL,
  `mobile` varchar(50) default NULL,
  `password` varchar(50) default NULL,
  `img` varchar(255) default NULL,
  `status` varchar(255) default 'Not_Verified'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`username`,`email`,`mobile`,`password`,`img`,`status`) values ('a','rmundekar2000@gmail.com','2134678979','a','a-20230114-104446.jpg','Verify'),('b','b@gmail.com','9756486325','b','a-20230114-104610.jpg','Verify');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
