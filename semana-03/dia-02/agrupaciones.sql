select * from notas;

select count(*) from notas;

select max(nota) from notas;

select avg(nota),min(nota), max(nota) from notas;

select pais,count(*)
from notas
group by pais
order by count(*) asc;

select pais,count(*) as total
from notas
where nota > 10
group by pais
order by count(*) asc;

select pais,avg(nota)as promedio
from notas
group by pais
having promedio>10;

select *
from notas n
where pais='Peru' and nota > (select avg(nota) from notas where pais='Peru');

select pais,count(*) as total
from notas n
where nota > (select avg(nota) from notas where pais=n.pais)
GROUP BY pais;

select n.pais,count(*) as nalumnos
from notas n inner join (select pais,avg(nota) as prom from notas group by pais) p on n.pais=p.pais
where n.nota > p.prom
GROUP BY n.pais
