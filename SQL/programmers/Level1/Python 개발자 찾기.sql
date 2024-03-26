-- https://school.programmers.co.kr/learn/courses/30/lessons/276013

select id, email, first_name, last_name
from developer_infos
where "Python" in (skill_1, skill_2, skill_3)
order by id
;