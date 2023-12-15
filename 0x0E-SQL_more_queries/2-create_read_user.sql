-- creates a database and user
-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create the user name with passw
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
-- Grant select privilege
GRANT SELECT 
ON hbtn_0d_2.* 
TO user_0d_2@localhost;
