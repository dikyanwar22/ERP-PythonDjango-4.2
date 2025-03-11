-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for db_django
CREATE DATABASE IF NOT EXISTS `db_django` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_django`;

-- Dumping structure for table db_django.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.auth_group: ~0 rows (approximately)
INSERT INTO `auth_group` (`id`, `name`) VALUES
	(1, 'Administrator'),
	(2, 'Finance');

-- Dumping structure for table db_django.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.auth_group_permissions: ~0 rows (approximately)

-- Dumping structure for table db_django.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.auth_permission: ~36 rows (approximately)
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add mahasiswa', 7, 'add_mahasiswa'),
	(26, 'Can change mahasiswa', 7, 'change_mahasiswa'),
	(27, 'Can delete mahasiswa', 7, 'delete_mahasiswa'),
	(28, 'Can view mahasiswa', 7, 'view_mahasiswa'),
	(29, 'Can add item', 8, 'add_item'),
	(30, 'Can change item', 8, 'change_item'),
	(31, 'Can delete item', 8, 'delete_item'),
	(32, 'Can view item', 8, 'view_item'),
	(33, 'Can add mahasiswa', 9, 'add_mahasiswa'),
	(34, 'Can change mahasiswa', 9, 'change_mahasiswa'),
	(35, 'Can delete mahasiswa', 9, 'delete_mahasiswa'),
	(36, 'Can view mahasiswa', 9, 'view_mahasiswa');

-- Dumping structure for table db_django.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `group_id` int DEFAULT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.auth_user: ~0 rows (approximately)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `group_id`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$870000$4jbfbtojHsvzNe6fF61TMT$FXPs7/K0IFJcuZR5Ha0zj+ulbuIQkqGLW2JEoX2ES2I=', NULL, 0, 'dicky', 'diky', 'anwar', 'dikyanwar22@gmail.com', 1, 0, 1, '2025-03-10 07:31:33.000000'),
	(2, 'pbkdf2_sha256$870000$4jbfbtojHsvzNe6fF61TMT$FXPs7/K0IFJcuZR5Ha0zj+ulbuIQkqGLW2JEoX2ES2I=', NULL, 0, 'budi', 'budi', 'soleh', 'budi@gmail.com', 2, 0, 1, '2025-03-10 07:31:33.000000'),
	(3, 'pbkdf2_sha256$870000$4jbfbtojHsvzNe6fF61TMT$FXPs7/K0IFJcuZR5Ha0zj+ulbuIQkqGLW2JEoX2ES2I=', NULL, 0, 'ridwan', 'ridwan', 'khadir', 'ridwan@gmail.com', 2, 0, 1, '2025-03-10 07:31:33.000000');

-- Dumping structure for table db_django.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.auth_user_groups: ~0 rows (approximately)

-- Dumping structure for table db_django.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.auth_user_user_permissions: ~0 rows (approximately)

-- Dumping structure for table db_django.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.django_admin_log: ~0 rows (approximately)

-- Dumping structure for table db_django.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.django_content_type: ~8 rows (approximately)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(8, 'crudapp', 'item'),
	(7, 'crudapp', 'mahasiswa'),
	(9, 'erp', 'mahasiswa'),
	(6, 'sessions', 'session');

-- Dumping structure for table db_django.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.django_migrations: ~18 rows (approximately)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2025-03-07 00:21:21.716484'),
	(2, 'auth', '0001_initial', '2025-03-07 00:21:22.249870'),
	(3, 'admin', '0001_initial', '2025-03-07 00:21:22.344005'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2025-03-07 00:21:22.359626'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-03-07 00:21:22.359626'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2025-03-07 00:21:22.423072'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2025-03-07 00:21:22.473914'),
	(8, 'auth', '0003_alter_user_email_max_length', '2025-03-07 00:21:22.487018'),
	(9, 'auth', '0004_alter_user_username_opts', '2025-03-07 00:21:22.502100'),
	(10, 'auth', '0005_alter_user_last_login_null', '2025-03-07 00:21:22.549152'),
	(11, 'auth', '0006_require_contenttypes_0002', '2025-03-07 00:21:22.549152'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2025-03-07 00:21:22.549152'),
	(13, 'auth', '0008_alter_user_username_max_length', '2025-03-07 00:21:22.596951'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2025-03-07 00:21:22.643741'),
	(15, 'auth', '0010_alter_group_name_max_length', '2025-03-07 00:21:22.659477'),
	(16, 'auth', '0011_update_proxy_permissions', '2025-03-07 00:21:22.659477'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2025-03-07 00:21:22.706894'),
	(18, 'sessions', '0001_initial', '2025-03-07 00:21:22.738123'),
	(19, 'crudapp', '0001_initial', '2025-03-07 00:23:58.065643'),
	(20, 'crudapp', '0002_item', '2025-03-07 00:30:06.198174'),
	(21, 'erp', '0001_initial', '2025-03-07 01:52:48.422935');

-- Dumping structure for table db_django.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.django_session: ~1 rows (approximately)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('b5tlkayqlhh5n1bb4xafoe0h44z191ly', '.eJyrViotTi2Kz0xRsjLUAbPzEnNTlayUUjKTsyuVdJTSMouKS-LhgmCxnESEUGJeeWIRUCw1NzEzB6oELGZk5JAOEtNLzs8FyqcX5ZcWQOypBQAb8SeG:1trok2:HQSbLmmy3rA5EM7UszG_TMr82hgb8VBEKWsR0G4ahg8', '2025-03-25 01:49:10.141459');

-- Dumping structure for table db_django.erp_mahasiswa
CREATE TABLE IF NOT EXISTS `erp_mahasiswa` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nama` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `nim` varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `jurusan` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nim` (`nim`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.erp_mahasiswa: ~4 rows (approximately)
INSERT INTO `erp_mahasiswa` (`id`, `nama`, `nim`, `email`, `jurusan`) VALUES
	(19, 'Warung ibu perjuangan', '3637239', 'it.naikbhinneka@gmail.com', 'Pendingin dan tata angin'),
	(22, 'Bengkel iqbal', '5555', 'otong@gmail.com', 'Kehutanan'),
	(23, 'Amat', '65656', 'amat@gmail.com', 'it-sage'),
	(24, 'Diky Anwar', '4739483', 'diky@gmail.com', 'informatika');

-- Dumping structure for table db_django.helpdesk_categories
CREATE TABLE IF NOT EXISTS `helpdesk_categories` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `deleted` int DEFAULT NULL,
  `created_by` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table db_django.helpdesk_categories: ~6 rows (approximately)
INSERT INTO `helpdesk_categories` (`id`, `name`, `deleted`, `created_by`, `created_at`, `updated_at`) VALUES
	(1, 'error ij', 0, 1, '2025-02-04 02:06:56', '2025-02-05 01:25:48'),
	(2, 'test', 0, 1, '2025-02-05 08:26:12', NULL),
	(3, 'coba lagi', 0, 1, '2025-02-04 23:13:33', NULL),
	(4, 'membantu siapa ok', 0, 1, '2025-02-04 23:26:16', '2025-02-05 01:24:46'),
	(5, 'Error system', 0, 1, '2025-02-04 23:27:05', '2025-02-05 01:25:21'),
	(6, 'Kesalahan data', 0, 1, '2025-02-05 00:08:49', '2025-02-05 01:25:33'),
	(19, 'upload satu', 0, 1, '2025-02-05 20:31:33', NULL),
	(20, 'upload dua', 0, 1, '2025-02-05 20:31:33', NULL),
	(21, 'upload tiga', 0, 1, '2025-02-05 20:31:33', NULL),
	(22, 'upload empat', 0, 1, '2025-02-05 20:31:33', NULL);

-- Dumping structure for table db_django.helpdesk_inbox
CREATE TABLE IF NOT EXISTS `helpdesk_inbox` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `group_id` bigint unsigned DEFAULT NULL,
  `cat_id` bigint unsigned DEFAULT NULL,
  `url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id_sender` bigint unsigned DEFAULT NULL,
  `file_upload` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `user_id_receiver` bigint unsigned DEFAULT NULL,
  `reply_message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `status` enum('0','1','2') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '0',
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `reply_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Dumping data for table db_django.helpdesk_inbox: ~3 rows (approximately)
INSERT INTO `helpdesk_inbox` (`id`, `group_id`, `cat_id`, `url`, `user_id_sender`, `file_upload`, `message`, `user_id_receiver`, `reply_message`, `status`, `created_at`, `updated_at`, `reply_at`) VALUES
	(1, 1, 1, 'http://127.0.0.1:8000/Helpdesk/detail_inbox/1', 3, '1738718421_upload_file.png', 'tolong perbaiki', 1, 'saya sudah perbaiki silahkan dicek kembali', '0', '2025-02-04 02:06:29', NULL, NULL),
	(2, 1, 1, 'http://127.0.0.1:8000/Helpdesk/detail_inbox/1', 2, '1738718421_upload_file.png', 'Puji syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa, karena dengan rahmat-Nya, kita semua masih diberi kesempatan untuk berkumpul di sini dalam keadaan sehat wal afiat. Pada kesempatan yang berbahagia ini, saya ingin menyampaikan beberapa patah kata mengenai kebangsaan kita, mengenai apa yang telah kita raih, dan apa yang harus kita perjuangkan bersama untuk masa depan bangsa.\n\nSaudara-saudara sekalian,\nBangsa Indonesia, yang terdiri dari beragam suku, agama, dan budaya, adalah contoh nyata dari kekuatan dalam keberagaman. Sejarah panjang perjuangan kemerdekaan kita telah membuktikan bahwa perbedaan tidaklah menjadi penghalang, melainkan kekuatan yang menyatukan kita. Dari Sabang sampai Merauke, dari Miangas sampai Pulau Rote, kita adalah satu, dalam semangat yang sama: Indonesia maju.', 1, 'saya sudah membalas chat ini', '0', '2025-02-05 03:53:00', NULL, NULL),
	(3, 1, 1, 'http://127.0.0.1:8000/Helpdesk/detail_inbox/1', 1, '1738718421_upload_file.png', 'apakah data ini masuk?', 1, NULL, '0', '2025-02-04 18:20:21', NULL, NULL);

-- Dumping structure for table db_django.menu
CREATE TABLE IF NOT EXISTS `menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `modul_id` int DEFAULT NULL,
  `sequence` int DEFAULT NULL,
  `nama` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `icon` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `uri` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `tipe` enum('dropdown','menu') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'dropdown',
  `group_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `deleted` int NOT NULL DEFAULT '0',
  `created_by` int DEFAULT NULL,
  `created_username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `updated_username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.menu: ~6 rows (approximately)
INSERT INTO `menu` (`id`, `modul_id`, `sequence`, `nama`, `icon`, `uri`, `tipe`, `group_id`, `deleted`, `created_by`, `created_username`, `created_at`, `updated_by`, `updated_username`, `updated_at`) VALUES
	(14, 6, 1, 'Pertanyaan', 'fa fa-list', 'Pertanyaan', 'menu', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:10:12', NULL, NULL, NULL),
	(15, 6, 3, 'Pengaturan', 'fa fa-gears', 'Pengaturan', 'dropdown', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:11:47', NULL, NULL, NULL),
	(16, 6, 2, 'Informasi', 'fa fa-belt', 'Informasi', 'dropdown', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:12:51', NULL, NULL, NULL),
	(17, 6, NULL, 'Berita', 'fa fa-list', 'Berita', 'menu', '1,2', 1, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:13:22', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:42:32'),
	(18, 6, NULL, 'Dashboard', 'fa fa-dashboard', 'Dashboard', 'menu', '1,2', 1, 1, 'dikyanwar22@gmail.com', '2024-02-11 01:23:06', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:42:40'),
	(19, 23, NULL, 'Category', 'fa fa-pencil', 'Category', 'menu', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2025-02-05 05:46:10', NULL, NULL, NULL);

-- Dumping structure for table db_django.modul
CREATE TABLE IF NOT EXISTS `modul` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nama` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `icon` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `uri` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `group_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sequence` int DEFAULT NULL,
  `deleted` int DEFAULT '0',
  `created_by` int DEFAULT NULL,
  `created_username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `updated_username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uri` (`uri`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.modul: ~12 rows (approximately)
INSERT INTO `modul` (`id`, `nama`, `icon`, `uri`, `group_id`, `sequence`, `deleted`, `created_by`, `created_username`, `created_at`, `updated_by`, `updated_username`, `updated_at`) VALUES
	(6, 'Admin', 'fa fa-car', 'Admin', '1,2', 3, 0, NULL, NULL, NULL, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:06:24'),
	(13, 'akunting', 'fa fa-money', 'akunting', '1,2', 7, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:42:12', 1, 'dikyanwar22@gmail.com', '2024-10-05 06:10:46'),
	(14, 'Marketing', 'fa fa-money', 'Marketing', '1,2', 2, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:42:33', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:43:24'),
	(15, 'Sales', 'fa fa-money', 'Sales', '1,2', 1, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:44:00', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:44:34'),
	(16, 'Operasional', 'fa fa-money', 'Operasional', '1,2', 8, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:44:15', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:43:17'),
	(17, 'Manufaktur', 'fa fa-money', 'Manufaktur', '1,2', 5, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:44:37', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:43:35'),
	(18, 'Gudang', 'fas fa-user', 'Gudang', '1,2', 10, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:47:51', 1, 'dikyanwar22@gmail.com', '2024-10-05 06:10:54'),
	(19, 'Purchase', 'fas fa-user', 'Purchase', '1,2', 9, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:48:35', NULL, NULL, NULL),
	(20, 'HRM', 'fas fa-box', 'HRM', '1,2', 4, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:49:49', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:43:59'),
	(21, 'PPC', 'fas fa-box', 'PPC', '1,2', 13, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:51:21', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:43:10'),
	(22, 'Logistic', 'fa fa-list', 'Logistic', '1,2', 14, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:51:40', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:44:15'),
	(23, 'Helpdesk', 'fa fa-globe', 'Helpdesk', '1,2', 12, 0, 1, 'dikyanwar22@gmail.com', '2024-09-26 14:53:28', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:44:07');

-- Dumping structure for table db_django.sub_menu
CREATE TABLE IF NOT EXISTS `sub_menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `menu_id` int DEFAULT NULL,
  `sequence` int DEFAULT NULL,
  `nama` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `icon` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `uri` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `group_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `deleted` int NOT NULL DEFAULT '0',
  `created_by` int DEFAULT NULL,
  `created_username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_by` int DEFAULT NULL,
  `updated_username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dumping data for table db_django.sub_menu: ~4 rows (approximately)
INSERT INTO `sub_menu` (`id`, `menu_id`, `sequence`, `nama`, `icon`, `uri`, `group_id`, `deleted`, `created_by`, `created_username`, `created_at`, `updated_by`, `updated_username`, `updated_at`) VALUES
	(12, 15, NULL, 'Fasilitas', 'fa fa-list', 'Fasilitas', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:14:50', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:37:04'),
	(13, 15, NULL, 'Promo', 'fa fa-list', 'Promo', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:15:08', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:38:14'),
	(14, 16, 2, 'Info', 'fa fa-list', 'Info', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:15:38', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:38:05'),
	(15, 16, 1, 'Carousel', 'fa fa-list', 'Carousel', '1,2', 0, 1, 'dikyanwar22@gmail.com', '2024-02-10 23:16:08', 1, 'dikyanwar22@gmail.com', '2024-10-05 05:36:55');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
