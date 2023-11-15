-- Creates database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use the database
USE `hbtn_0d_usa`;
-- creates a table in database
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY,
	`name` VARCHAR(256) NOT NULL );
