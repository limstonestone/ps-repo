-- https://school.programmers.co.kr/learn/courses/30/lessons/299308

-- QUARTER : 분기를 구해주는 DATE 함수
select concat(quarter(differentiation_date), "Q") as quarter,
    count(*) as ecoli_count
from ecoli_data
group by concat(quarter(differentiation_date), "Q")
order by quarter
;