-- Script creates a table and inserts values into it
-- creates second_table with id, name and score attributes
CREATE TABLE IF NOT EXISTS `second_table` (
	`id` INT,
	`name` VARCHAR(256),
	`score` INT);
-- Inserts values into table created
INSERT INTO second_table
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);
