create table departments( id serial primary key, name varchar(50));

create table teachers( id serial primary key, first_name varchar(50), 
					last_name varchar (50), 
					department_id integer references departments(id));
					
create table groups( id serial primary key, name varchar(50), 
					department_id integer references departments(id));
					
create table students( id serial primary key, first_name varchar(50), 
					last_name varchar (50), 
					group_id integer references groups(id));

INSERT INTO departments (name) VALUES
('Computer Science'),
('Mathematics'),
('Physics');

INSERT INTO teachers (first_name, last_name, department_id) VALUES
('John', 'Doe', 1),
('Jane', 'Smith', 2),
('Robert', 'Johnson', 3),
('Emily', 'Williams', 1),
('Michael', 'Brown', 2);

INSERT INTO groups (name, department_id) VALUES
('CS50', 1),
('Math101', 2),
('Phys101', 3),
('CS101', 1);

INSERT INTO students (first_name, last_name, group_id) VALUES
('Alice', 'Johnson', 1),
('Bob', 'Smith', 2),
('Charlie', 'Williams', 3),
('David', 'Brown', 1),
('Eva', 'Davis', 2),
('Frank', 'Miller', 3),
('Grace', 'Jones', 4),
('Henry', 'Anderson', 1),
('Ivy', 'Moore', 2),
('Jack', 'Taylor', 3),
('Kate', 'White', 4),
('Leo', 'Martin', 1),
('Mia', 'Young', 2),
('Noah', 'Lee', 3),
('Olivia', 'Harris', 4),
('Paul', 'Clark', 1),
('Quinn', 'Evans', 2),
('Ryan', 'Wright', 3),
('Sophia', 'Walker', 4),
('Tyler', 'Hill', 1);

