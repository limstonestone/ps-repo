-- https://school.programmers.co.kr/learn/courses/30/lessons/298515

-- CONCAT 함수를 통해 문자열 결합 가능
select concat(max(length), "cm") as max_length
from fish_info
;