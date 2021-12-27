
CREATE TABLE IF NOT EXISTS books (

	book_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	author_id INTEGER UNSIGNED, 
	title VARCHAR(100) NOT NULL,
	year INTEGER UNSIGNED NOT NULL DEFAULT 1900,
	language VARCHAR(2) NOT NULL DEFAULT 'es' COMMENT 'Use ISO 639-1 language',
	cover_url VARCHAR(500),
	price DOUBLE(6, 2) NOT NULL DEFAULT 10.0,
	sellable TINYINT(1) DEFAULT 1, 
	copies INTEGER NOT NULL DEFAULT 1, 
	description TEXT

);


CREATE TABLE IF NOT EXISTS authors (

	author_id INTEGRER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL, 
	nationality VARCHAR(3)

);

 
CREATE TABLE IF NOT EXISTS `clients`(

	client_id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	`name`  VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE, 
	birthdate DATETIME,
	gender ENUM('M','F','ND') NOT NULL,
	active TINYINT(1) NOT NULL DEFAULT 1,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP 
	ON UPDATE CURRENT_TIMESTAMP

);


CREATE TABLE IF NOT EXISTS operations(

	operations_id INTEGER UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	book_id INTEGER UNSIGNED NOT NULL ,
	client_id INTEGER UNSIGNED NOT NULL ,
	operations_type ENUM('S','R','B') COMMENT 'S-> Sold, R->Returned, B->Borrowed',
	create_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	finshed TINYINT(1) NOT NULL
	
);