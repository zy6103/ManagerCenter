-- MySQL dump 10.13  Distrib 5.6.13, for Linux (x86_64)
--
-- Host: localhost    Database: configcenter
-- ------------------------------------------------------
-- Server version	5.6.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add 账号表',6,'add_account'),(17,'Can change 账号表',6,'change_account'),(18,'Can delete 账号表',6,'delete_account'),(19,'配置中心一级索引页面',6,'menuLv1_index_get'),(20,'配置中心二级索引页面',6,'menuLv2_index_get'),(21,'配置中心角色索引页面',6,'role_index_get'),(22,'配置中心账号索引页面',6,'account_index_get'),(23,'配置中心一级菜单添加页面',6,'menuLv1_add_all'),(24,'配置中心一级菜单修改页面',6,'menuLv1_change_all'),(25,'配置中心二级菜单添加页面',6,'menuLv2_add_all'),(26,'配置中心二级菜单修改页面',6,'menuLv2_change_all'),(27,'配置中心角色添加页面',6,'role_add_all'),(28,'配置中心角色修改页面',6,'role_change_all'),(29,'配置中心账号添加页面',6,'account_add_all'),(30,'配置中心账号修改页面',6,'account_change_all'),(31,'配置中心删除提交页面',6,'delete_obj_post'),(32,'配置中心账号密码修改提交页面',6,'reset_password_post'),(33,'Can add 一级菜单表',7,'add_menulevel1'),(34,'Can change 一级菜单表',7,'change_menulevel1'),(35,'Can delete 一级菜单表',7,'delete_menulevel1'),(36,'Can add 二级菜单表',8,'add_menulevel2'),(37,'Can change 二级菜单表',8,'change_menulevel2'),(38,'Can delete 二级菜单表',8,'delete_menulevel2'),(39,'Can add 角色表',9,'add_role'),(40,'Can change 角色表',9,'change_role'),(41,'Can delete 角色表',9,'delete_role');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_account`
--

DROP TABLE IF EXISTS `configCenter_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(32) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_account`
--

LOCK TABLES `configCenter_account` WRITE;
/*!40000 ALTER TABLE `configCenter_account` DISABLE KEYS */;
INSERT INTO `configCenter_account` VALUES (1,'pbkdf2_sha256$36000$WdmnuUtX0dEz$/cw6nJBTYaI/dosvqzwU9h6+5F09JRqxfSkSrlctMxk=','2018-11-26 01:28:38.610000',0,'admin@mc.com','超级管理员',1,1);
/*!40000 ALTER TABLE `configCenter_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_account_groups`
--

DROP TABLE IF EXISTS `configCenter_account_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_account_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `configCenter_account_groups_account_id_group_id_37e961f8_uniq` (`account_id`,`group_id`),
  KEY `configCenter_account_groups_group_id_4671ef0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `configCenter_account_groups_group_id_4671ef0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `configCenter_account_account_id_6dfc5e5c_fk_configCen` FOREIGN KEY (`account_id`) REFERENCES `configCenter_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_account_groups`
--

LOCK TABLES `configCenter_account_groups` WRITE;
/*!40000 ALTER TABLE `configCenter_account_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `configCenter_account_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_account_roles`
--

DROP TABLE IF EXISTS `configCenter_account_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_account_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `configCenter_account_roles_account_id_role_id_a5c29da8_uniq` (`account_id`,`role_id`),
  KEY `configCenter_account_role_id_49c95dfa_fk_configCen` (`role_id`),
  CONSTRAINT `configCenter_account_role_id_49c95dfa_fk_configCen` FOREIGN KEY (`role_id`) REFERENCES `configCenter_role` (`id`),
  CONSTRAINT `configCenter_account_account_id_17434383_fk_configCen` FOREIGN KEY (`account_id`) REFERENCES `configCenter_account` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_account_roles`
--

LOCK TABLES `configCenter_account_roles` WRITE;
/*!40000 ALTER TABLE `configCenter_account_roles` DISABLE KEYS */;
INSERT INTO `configCenter_account_roles` VALUES (1,1,1);
/*!40000 ALTER TABLE `configCenter_account_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_account_user_permissions`
--

DROP TABLE IF EXISTS `configCenter_account_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_account_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `configCenter_account_use_account_id_permission_id_6e05a3d0_uniq` (`account_id`,`permission_id`),
  KEY `configCenter_account_permission_id_d62b4b07_fk_auth_perm` (`permission_id`),
  CONSTRAINT `configCenter_account_permission_id_d62b4b07_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `configCenter_account_account_id_044831da_fk_configCen` FOREIGN KEY (`account_id`) REFERENCES `configCenter_account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_account_user_permissions`
--

LOCK TABLES `configCenter_account_user_permissions` WRITE;
/*!40000 ALTER TABLE `configCenter_account_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `configCenter_account_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_menulevel1`
--

DROP TABLE IF EXISTS `configCenter_menulevel1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_menulevel1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `url_type` smallint(6) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_menulevel1`
--

LOCK TABLES `configCenter_menulevel1` WRITE;
/*!40000 ALTER TABLE `configCenter_menulevel1` DISABLE KEYS */;
INSERT INTO `configCenter_menulevel1` VALUES (1,'配置中心',1,'#');
/*!40000 ALTER TABLE `configCenter_menulevel1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_menulevel2`
--

DROP TABLE IF EXISTS `configCenter_menulevel2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_menulevel2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `level2_to_level1_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url_name` (`url_name`),
  KEY `configCenter_menulev_level2_to_level1_id_ab13a843_fk_configCen` (`level2_to_level1_id`),
  CONSTRAINT `configCenter_menulev_level2_to_level1_id_ab13a843_fk_configCen` FOREIGN KEY (`level2_to_level1_id`) REFERENCES `configCenter_menulevel1` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_menulevel2`
--

LOCK TABLES `configCenter_menulevel2` WRITE;
/*!40000 ALTER TABLE `configCenter_menulevel2` DISABLE KEYS */;
INSERT INTO `configCenter_menulevel2` VALUES (1,'一级菜单','menuLv1_index',1),(2,'二级菜单','menuLv2_index',1),(3,'角色','role_index',1),(4,'账号','account_index',1);
/*!40000 ALTER TABLE `configCenter_menulevel2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_role`
--

DROP TABLE IF EXISTS `configCenter_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_role`
--

LOCK TABLES `configCenter_role` WRITE;
/*!40000 ALTER TABLE `configCenter_role` DISABLE KEYS */;
INSERT INTO `configCenter_role` VALUES (1,'config');
/*!40000 ALTER TABLE `configCenter_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `configCenter_role_menu_level1`
--

DROP TABLE IF EXISTS `configCenter_role_menu_level1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `configCenter_role_menu_level1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `menulevel1_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `configCenter_role_menu_l_role_id_menulevel1_id_84eaf3fd_uniq` (`role_id`,`menulevel1_id`),
  KEY `configCenter_role_me_menulevel1_id_c9f762d5_fk_configCen` (`menulevel1_id`),
  CONSTRAINT `configCenter_role_me_menulevel1_id_c9f762d5_fk_configCen` FOREIGN KEY (`menulevel1_id`) REFERENCES `configCenter_menulevel1` (`id`),
  CONSTRAINT `configCenter_role_me_role_id_a9ca13ef_fk_configCen` FOREIGN KEY (`role_id`) REFERENCES `configCenter_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `configCenter_role_menu_level1`
--

LOCK TABLES `configCenter_role_menu_level1` WRITE;
/*!40000 ALTER TABLE `configCenter_role_menu_level1` DISABLE KEYS */;
INSERT INTO `configCenter_role_menu_level1` VALUES (1,1,1);
/*!40000 ALTER TABLE `configCenter_role_menu_level1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_configCenter_account_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_configCenter_account_id` FOREIGN KEY (`user_id`) REFERENCES `configCenter_account` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-11-26 01:29:00.707000','1','配置中心',1,'[{\"added\": {}}]',7,1),(2,'2018-11-26 01:29:31.648000','1','一级菜单',1,'[{\"added\": {}}]',8,1),(3,'2018-11-26 01:29:44.014000','2','二级菜单',1,'[{\"added\": {}}]',8,1),(4,'2018-11-26 01:30:00.245000','3','角色',1,'[{\"added\": {}}]',8,1),(5,'2018-11-26 01:30:13.687000','4','账号',1,'[{\"added\": {}}]',8,1),(6,'2018-11-26 01:33:21.003000','1','config',1,'[{\"added\": {}}]',9,1),(7,'2018-11-26 01:37:24.884000','1','admin@mc.com',2,'[]',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(6,'configCenter','account'),(7,'configCenter','menulevel1'),(8,'configCenter','menulevel2'),(9,'configCenter','role'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-11-26 01:23:42.424000'),(2,'contenttypes','0002_remove_content_type_name','2018-11-26 01:23:42.461000'),(3,'auth','0001_initial','2018-11-26 01:23:42.545000'),(4,'auth','0002_alter_permission_name_max_length','2018-11-26 01:23:42.567000'),(5,'auth','0003_alter_user_email_max_length','2018-11-26 01:23:42.587000'),(6,'auth','0004_alter_user_username_opts','2018-11-26 01:23:42.604000'),(7,'auth','0005_alter_user_last_login_null','2018-11-26 01:23:42.616000'),(8,'auth','0006_require_contenttypes_0002','2018-11-26 01:23:42.621000'),(9,'auth','0007_alter_validators_add_error_messages','2018-11-26 01:23:42.633000'),(10,'auth','0008_alter_user_username_max_length','2018-11-26 01:23:42.644000'),(11,'configCenter','0001_initial','2018-11-26 01:23:42.895000'),(12,'admin','0001_initial','2018-11-26 01:23:42.964000'),(13,'admin','0002_logentry_remove_auto_add','2018-11-26 01:23:42.982000'),(14,'admin','0003_auto_20180626_1553','2018-11-26 01:23:43.009000'),(15,'admin','0004_auto_20180626_1557','2018-11-26 01:23:43.039000'),(16,'sessions','0001_initial','2018-11-26 01:23:43.060000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-26  9:38:28
