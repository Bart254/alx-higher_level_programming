-- creates user user_0d_1 and gives all privileges
-- Use Database
CREATE USER IF NOT EXISTS 'user_0d_1@localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- Gives user all privileges
GRANT ALL ON *.* TO 'user_0d_1@localhost';
