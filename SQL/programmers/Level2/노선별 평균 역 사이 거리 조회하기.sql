-- https://school.programmers.co.kr/learn/courses/30/lessons/284531

-- total_distance 가 반올림하여 문자열인 상태이므로 ORDER BY 에서 따로 지정해줘야함을 주의
select route, concat(round(sum(d_between_dist),1), "km") as total_distance, 
    concat(round(avg(d_between_dist),2), "km") as average_distance
from subway_distance
group by route
order by round(total_distance, 1) desc
;