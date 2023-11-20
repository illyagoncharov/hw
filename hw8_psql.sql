CREATE DATABASE homework8_db;

\c homework8_db

CREATE TABLE actors(id serial, first_name varchar(30), 
				last_name varchar(30), date_of_birth date, 
				gender varchar(30));
					
CREATE TABLE directors(id serial, first_name varchar(30), 
				last_name varchar(30), email varchar(50));
					   
CREATE TABLE films(id serial, film_name varchar(30),
				 ganre varchar(30), country varchar(30), 
				 id_director integer, id_actor integer) ;

INSERT INTO actors (first_name, last_name, date_of_birth, gender) 
VALUES ('John', 'Travolta', 'Feb 18 1954', 'MALE'), 
('Willard', 'Smith', 'Sep 25 1968', 'MALE'), 
('Leonardo', 'DiCaprio', 'Nov 11 1974', 'MALE');

INSERT INTO directors (first_name, last_name, email) 
VALUES ('Quentin', 'Tarantino', 'tarantino@gmail.com'), 
('Martin', 'Scorsese', 'scorsese@gmail.com'), 
('Guy', 'Ritchie', 'guy@gmail.com');

INSERT INTO films(film_name, ganre, country, id_director, id_actor)
VALUES ('Aladdin', 'Adventures', 'Australia, USA, UK', '3', '3'), 
('Pulp Fiction', 'Crime novels', 'USA', '1', '1'), 
('The Wolf of Wall Street', 'Biographical ', 'USA', '2', '2');
