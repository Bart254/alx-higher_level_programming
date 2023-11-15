-- Creates database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Use the database
USE `hbtn_0d_usa`;
-- creates a table in database
CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY,
	`state_id` INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES state(id),
	`name` VARCHAR(256) NOT NULL );
