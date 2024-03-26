-- https://school.programmers.co.kr/learn/courses/30/lessons/293259

select round(avg(ifnull(length, 10)),2) as average_length
from fish_info
;