-- https://school.programmers.co.kr/learn/courses/30/parts/17043

select e.year, max_ - size_of_colony as year_dev, id
from (select year(DIFFERENTIATION_DATE) as year, size_of_colony, id
        from ecoli_data e) e
    left join (select year(differentiation_date) as year, max(size_of_colony) as max_
                from ecoli_data
                group by year(differentiation_date)) m
    on e.year = m.year
order by year, year_dev
;