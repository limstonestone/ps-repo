-- https://school.programmers.co.kr/learn/courses/30/lessons/293261

select id, fish_name, length
from fish_info fi 
    inner join fish_name_info fni 
        on fi.fish_type = fni.fish_type
where (fi.fish_type, length) in (select fish_type, max(length)
                                 from fish_info
                                 group by fish_type)
order by id
;