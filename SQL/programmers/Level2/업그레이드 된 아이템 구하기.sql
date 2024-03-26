-- https://school.programmers.co.kr/learn/courses/30/lessons/273711

select i.item_id as item_id, i.item_name, i.rarity
from item_info i inner join item_tree t on i.item_id = t.item_id
where t.parent_item_id in 
    (select item_id from item_info where rarity="RARE")
order by item_id desc
;
