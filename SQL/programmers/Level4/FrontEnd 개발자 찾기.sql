-- https://school.programmers.co.kr/learn/courses/30/lessons/276035

-- 단순히 category 가 "Front End" 일 뿐만 아니라, 코드에 대한 합계를 해줘야 함
select id, email, first_name, last_name
from developers d inner join (select sum(code) as code 
                              from skillcodes
                            where category="Front End") s 
    on (d.skill_code & s.code)
order by id
;