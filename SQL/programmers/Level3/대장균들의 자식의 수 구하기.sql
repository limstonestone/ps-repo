-- https://school.programmers.co.kr/learn/courses/30/lessons/299305

select id, ifnull(child_count, 0) as child_count
from ecoli_data e
    left join (select parent_id, count(*) as child_count
              from ecoli_data
              group by parent_id) p
      on e.id = p.parent_id
order by id
;