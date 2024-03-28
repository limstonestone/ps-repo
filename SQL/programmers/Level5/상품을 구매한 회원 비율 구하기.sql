-- https://school.programmers.co.kr/learn/courses/30/lessons/131534

-- distinct 를 활용하여 여러번 구매한 회원 수를 제외
with joined_users as (
    select count(distinct user_id) as joined
    from user_info
    where year(joined) = 2021
),
purchased_info as (
    select 
        year(sales_date) AS year,
        month(sales_date) AS month,
        count(distinct user_id) AS purchased_users
    from online_sale
    where user_id IN (select distinct user_id from user_info where YEAR(joined) = 2021)
    group by year, month
)
select 
    p.year,
    p.month,
    p.purchased_users,
    round(p.purchased_users / j.joined, 1) as purchased_ratio
from purchased_info p
inner join joined_users j;
