-- https://school.programmers.co.kr/learn/courses/30/lessons/151141

-- convert 를 활용하여 정수변환
-- date type 의 경우 단순히 뺄셈으로 날짜 차를 구하는 것이 아닌 datediff 를 활용해야 함
select history_id,
    convert(duration * daily_fee * (100-ifnull(discount_rate, 0))/100, signed) as fee
from
(select history_id, daily_fee, datediff(end_date, start_date) + 1 as duration,
    case when datediff(end_date, start_date) + 1 >= 90 then "90일 이상"
        when datediff(end_date, start_date) + 1 >= 30 then "30일 이상"
        when datediff(end_date, start_date) + 1 >= 7 then "7일 이상"
        end as duration_type
from car_rental_company_rental_history ch
    left join (select car_id, car_type, daily_fee 
               from car_rental_company_car) c 
        on ch.car_id = c.car_id
where car_type = "트럭") a
    left join (select duration_type, discount_rate
               from car_rental_company_discount_plan
              where car_type="트럭") dp
        on dp.duration_type = a.duration_type
order by fee desc, history_id desc
;