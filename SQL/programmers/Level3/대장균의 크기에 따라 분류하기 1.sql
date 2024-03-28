-- https://school.programmers.co.kr/learn/courses/30/lessons/299307

select id,
    case when size_of_colony <= 100 then "LOW"
        when size_of_colony <= 1000 then "MEDIUM"
        else "HIGH" end as size
from ecoli_data
order by id
;