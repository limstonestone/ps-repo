-- https://school.programmers.co.kr/learn/courses/30/lessons/276036

-- with as 를 사용하여 임시 테이블 생성
-- group_concat 으로 name 과 category 결합하여 그룹핑
-- & : 비트 AND 연산자
-- having 을 사용하여 case when 을 통해 grade 컬럼을 삽입한 뒤 조건 활용(where X)
with group_developers as (
    select id, email, group_concat(distinct name, category) as grouped
    from skillcodes s
    join developers d on d.skill_code & s.code
    group by 1,2)
    
select case 
    when grouped like "%Front%" and grouped like "%Python%" then "A"
    when grouped like "%C#%" then "B"
    when grouped like "%Front%" then "C" end as grade,
    id, email
from group_developers
having grade is not null
order by grade, id
;