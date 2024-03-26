-- https://school.programmers.co.kr/learn/courses/30/lessons/298518

select count(*) as FISH_COUNT
from fish_info i, fish_name_info n
where n.fish_name in ("BASS", "SNAPPER") and i.fish_type = n.fish_type
;