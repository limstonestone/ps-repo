-- https://school.programmers.co.kr/learn/courses/30/lessons/273709

select sum(price) as total_price
from item_info
where rarity="LEGEND"
;