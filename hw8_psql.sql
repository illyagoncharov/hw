Create table actors(id serial, first_name varchar(30), 
				last_name varchar(30), date_of_birth date, 
				gender varchar(30));
					
Create table directors(id serial, first_name varchar(30), 
				last_name varchar(30), email varchar(50));
					   
Create table films(id serial, film_name varchar(30),
				 ganre varchar(30), country varchar(30), 
				 id_director integer, id_actor integer) ;

INSERT INTO actors (first_name, last_name, date_of_birth, gender) 
VALUES ('John', 'Travolta', 'Feb 18 1954', 'MALE');
INSERT INTO actors (first_name, last_name, date_of_birth, gender) 
VALUES ('Willard', 'Smith', 'Sep 25 1968', 'MALE');
INSERT INTO actors (first_name, last_name, date_of_birth, gender) 
VALUES ('Leonardo', 'DiCaprio', 'Nov 11 1974', 'MALE');

INSERT INTO directors (first_name, last_name, email) 
VALUES ('Quentin', 'Tarantino', 'tarantino@gmail.com');
INSERT INTO directors (first_name, last_name, email) 
VALUES ('Martin', 'Scorsese', 'scorsese@gmail.com');
INSERT INTO directors (first_name, last_name, email) 
VALUES ('Guy', 'Ritchie', 'guy@gmail.com');	

INSERT INTO films(film_name, ganre, country, id_director, id_actor)
VALUES ('Aladdin', 'Adventures', 'Australia, USA, UK', '3', '3');
INSERT INTO films(film_name, ganre, country, id_director, id_actor)
VALUES ('Pulp Fiction', 'Crime novels', 'USA', '1', '1');
INSERT INTO films(film_name, ganre, country, id_director, id_actor)
VALUES ('The Wolf of Wall Street', 'Biographical ', 'USA', '2', '2');

select pp.film_name, concat (p.first_name, ' ', p.last_name) as director, 
		concat (cp.first_name, ' ', cp.last_name) as actor 
		from films pp
	left join people p on pp.director = p.id 
	left join people cp on pp.main_actor = cp.id;

Select film_name, genre_name as genre, country_name as country, concat(pl.first_name, ' ', pl.last_name) as director,
concat(people.first_name, ' ', people.last_name) as actor

from films f
	left join genre on genre.id = f.id_genre
	left join country on country.id = f.id_country
	left join people pl on pl.id = f.director
	left join people on people.id = f.main_actor; 