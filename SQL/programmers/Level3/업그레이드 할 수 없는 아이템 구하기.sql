-- https://school.programmers.co.kr/learn/courses/30/lessons/273712

select item_id, item_name, rarity
from item_info
where item_id not in (select distinct parent_item_id 
                      from item_tree 
                      where parent_item_id is not null)
order by item_id desc
;