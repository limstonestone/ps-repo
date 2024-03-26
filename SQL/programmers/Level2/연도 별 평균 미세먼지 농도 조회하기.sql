-- https://school.programmers.co.kr/learn/courses/30/lessons/284530

select year(ym) as year, round(avg(pm_val1),2) as "pm10", 
    round(avg(pm_val2),2) as "pm2.5"
from air_pollution
where location2 = "수원"
group by year
order by year
;