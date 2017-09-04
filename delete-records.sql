-- Exercise: 3
-- Two parts
-- Part one: delete records where email_type equals 'private'
-- Part two: delete records duplicated, the valid record is the latest record

-- This block code isn't working fine.
/*
with no_private_rows as 
(
	delete from emails where email_type = 'private';
	returning *
), 
	no_duplicate as 
(
	delete from no_private_rows a using 
	(
		select distinct b.id from emails b, emails c where b.contact_id = c.contact_id and b.id < c.id 
	) d 
	where a.id = d.id;
)	
select * from no_duplicate;
*/

delete from emails where email_type = 'private';
delete from emails a using (
	select distinct b.id 
	from emails b, emails c 
	where b.contact_id = c.contact_id and b.id < c.id 
) d 
where a.id = d.id;

select * from emails;