#visualizar una base de datos
show databases;

# crear una base de datos
create database codigo;

create table alumnos(
id int,
nombre varchar(255),
apellido varchar(255)
);

SELECT * FROM codigo.alumnos;

insert into codigo.alumnos(
id,
nombre,
apellido)
values(
1,
'Cesar',
'Mayta');
#insertart datos en grupo
insert into codigo.alumnos(
id,
nombre,
apellido)
values
(2,'Miguel','Ramos'),
(3,'Eduardo','De Rivero'),
(4,'Jose','Rivas'),
(5,'Jorge','Garnica'),
(6,'Paolo','Guerrero'),
(7,'Jefferson','Farfan'),
(8,'Cristiano','Ronaldo'),
(9,'Lionel','Messi'),
(10,'Neimar','Jr');

# consultar algunas columnas
select id, nombre from codigo.alumnos;

#sentencia WHERE
select id, nombre from codigo.alumnos where id<6;

#operadores AND, OR, NOT
select * from codigo.alumnos where id<8 and id>3;

#order by
select * from codigo.alumnos order by id desc;
select * from codigo.alumnos order by apellido desc, nombre asc;

#update
set SQL_SAFE_UPDATES = 0;
update codigo.alumnos
set nombre='Alfred', apellido='Sanchez'
where id=4;
set SQL_SAFE_UPDATES = 1;

#delete
set SQL_SAFE_UPDATES = 0;
delete from codigo.alumnos
where id=10;
set SQL_SAFE_UPDATES = 1;

#like
select * from codigo.alumnos where nombre like 'A%';
select * from codigo.alumnos where id regexp '[0-5]'
