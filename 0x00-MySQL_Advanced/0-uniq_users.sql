-- SQL script that creates a table users
CREATE DATABASE IF NOT EXISTS users(PRIMARY KEY(
	id int NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL,
	name varchar(255),
	PRIMARY KEY (id),
	UNIQUE (email)
	);
