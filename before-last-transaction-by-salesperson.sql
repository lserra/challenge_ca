-- Exercise: 4
-- Before Last Transaction By Salesperson
select a.salesperson_id, max(a.date) as date
from 
	transactions a ,
(
	select salesperson_id, max(date) as date 
	from transactions 
	group by salesperson_id 
) as b 
where 
(
	a.salesperson_id = b.salesperson_id and
	a.date <> b.date
)
group by a.salesperson_id
order by a.salesperson_id;
