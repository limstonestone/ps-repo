-- https://school.programmers.co.kr/learn/courses/30/lessons/293257

-- Left 조인을 해주어야 실제 잡은 것들에 대해서만 조인됨
select fish_count, fish_name
from (select fish_type, count(*) as fish_count
      from fish_info
      group by fish_type) fi 
      left join fish_name_info fni
        on fi.fish_type = fni.fish_type
order by fish_count desc
;