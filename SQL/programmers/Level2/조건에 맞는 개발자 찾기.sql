-- https://school.programmers.co.kr/learn/courses/30/lessons/276034

-- & 연산자를 사용하면 비트 AND 연산을 수행, 0이 아닌(스킬이 포함된 값 리턴)
select id, email, first_name, last_name
from developers d
where (d.skill_code & (select code from skillcodes where name="Python")) 
    or (d.skill_code & (select code from skillcodes where name="C#")) 
order by id
;

select distinct d.id, d.email, d.first_name, d.last_name
from developers d join skillcodes s on d.skill_code & s.code > 0
where s.name in ('Python', 'C#')
order by d.id
;