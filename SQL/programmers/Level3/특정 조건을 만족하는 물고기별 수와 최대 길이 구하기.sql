-- https://school.programmers.co.kr/learn/courses/30/lessons/298519

-- IFNULL 함수를 통해 NULL 값 처리 가능
select count(*) as fish_count, max(length) as max_length, fish_type
from fish_info
group by fish_type having avg(ifnull(length, 10)) >= 33
order by fish_type
;