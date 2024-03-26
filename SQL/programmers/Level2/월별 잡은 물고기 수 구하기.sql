-- https://school.programmers.co.kr/learn/courses/30/lessons/293260

select count(*) as fish_count, month(time) as month
from fish_info
group by month
order by month
;

-- CAST 함수 -> 타입 변환 (SIGNED : 정수형, CHAR : 문자형)
select count(*) as fish_count, cast(date_format(time, "%m") as signed) as month
from fish_info
group by month
order by month
;

-- CONVERT 도 마찬가지
select count(*) as fish_count, convert(date_format(time, "%m"), signed) as month
from fish_info
group by month
order by month
;
