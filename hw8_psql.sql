Create table country(id serial primary key, name varchar(50));

Insert into country (name) 
values ('Argentina'),('UK'), ('France'),('China'),('USA'),('Italia'),('Japan'),('Australia'),('Ukraine');

CREATE TABLE gender ( id serial primary key, name varchar(50));

Insert into gender(name)
Values ('male'), ('female');

create table profession ( id serial primary key, name varchar(20));

Insert into profession ( name)
Values ('actor'), ('director');

Create table genre ( id serial primary key, name varchar(50));

Insert into genre (name)
Values ('Adventure'), ('Comedy'), ('Drama'), ('Fantasy'), ('Historical'), 
('Horror'), ('Thriller'), ('Western'), ('Biographical');

Create table people( id serial primary key, first_name varchar(50), 
					last_name varchar(50), email varchar(50), 
					id_gender integer references gender(id), 
					id_profession integer references profession(id));

Insert into people ( first_name, last_name, email, id_gender, id_profession)

Values ('John', 'Travolta', 'travolta@gmail.com', 1, 1 ), 
('Willn', 'Smith', 'ws@gmail.com', 1, 1 ),
('Leonardo', 'DiCaprio', 'ld@gmail.com', 1, 1 ),
('Quentin', 'Tarantino', 'tarantino@gmail.com', 1, 2 ),
('Martin', 'Scorsese', 'ms@gmail.com', 1, 2 ),
('Guy', 'Ritchie', 'guy@gmail.com', 1, 2 );

Create table films(id serial primary key, name varchar(50),
				   id_genre integer references genre(id),id_country integer references country(id), 
				   id_director integer references people(id), id_main_actor integer references people(id) );

Insert into films(name, id_genre, id_country, 
				   id_director, id_main_actor)

Values ('Aladdin', 1, 8, 6, 2), ('Pulp Fiction', 7, 5, 4, 1), ('The Wolf of Wall Street', 9, 5, 5, 3);


Select f.name, genre.name as genre, country.name as country, concat(pl.first_name, ' ', pl.last_name) as director,
concat(people.first_name, ' ', people.last_name) as actor
from films f
	left join genre on genre.id = f.id_genre
	left join country on country.id = f.id_country
	left join people pl on pl.id = f.id_director
	left join people on people.id = f.id_main_actor; 
