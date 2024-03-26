-- https://school.programmers.co.kr/learn/courses/30/lessons/298516

select count(*) as fish_count
from fish_info
where year(time) = 2021
;