with recursive rc as (
    select ID, PARENT_ID, 1 as GEN from ECOLI_DATA where PARENT_ID is null
    union all
    select e.ID, e.PARENT_ID, rc.GEN + 1 from ECOLI_DATA e JOIN rc on e.PARENT_ID=rc.ID
)

select count(*) as COUNT, GEN as GENERATION 
from rc 
where id not in (
    select distinct PARENT_ID from ECOLI_DATA where PARENT_ID is not null
)
group by GEN