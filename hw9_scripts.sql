/* Вивести ім’я та прізвище студентів разом із назвами їх груп */

select first_name, last_name, groups.name from students 
left join groups on students.group_id = groups.id;

/* Отримати список викладачів та назви кафедр, на яких вони працюють */

select first_name, last_name, departments.name from teachers 
left join departments on teachers.department_id = departments.id;

/* Вивести кількість студентів у кожній групі */

select groups.name, count(*) as students from students 
left join groups on students.group_id = groups.id
group by groups.name;

/*Вивести назву кафедри, імʼя та прізвище викладача, назву групи, імʼя та прізвище студента для викладачів із прізвищем Smith, Williams та Johnson, відсортувати за групою на прізвищем студента. Застосувати JOIN для з’єднання даних з усіх чотирьох таблиць на основі відповідних зовнішніх ключів. */

select t.first_name, t.last_name, departments.name as department, 
groups.name as group, students.last_name 
from teachers t
left join departments on t.department_id = departments.id
left join groups on groups.department_id = departments.id
left join students on students.group_id = groups.id
where students.last_name in ('Smith', 'Williams', 'Johnson')
order by groups.name, students.last_name;
