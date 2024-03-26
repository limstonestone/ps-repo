-- https://school.programmers.co.kr/learn/courses/30/lessons/273710

select it.item_id, ii.item_name
from (select item_id 
      from item_tree 
      where parent_item_id is null) it
      left join item_info ii
        on ii.item_id = it.item_id 
order by item_id
;