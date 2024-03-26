-- https://school.programmers.co.kr/learn/courses/30/lessons/284529

select hre.dept_id, dept_name_en, round(avg(sal)) as avg_sal
from hr_department hrd 
    right join hr_employees hre
        on hrd.dept_id = hre.dept_id
group by dept_id
order by avg_sal desc
;