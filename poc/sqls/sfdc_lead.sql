select 1 as id, EXTRACT(year from c.created_date_est) year_created,
MONTHNAME(c.created_date_est) as Month_of_Year
, d.super_region,d.sub_region,d.region,
case when lead_stage_to in ('Marketing Rejected','Sales Rejected','Marketing Disqualified','Sales Disqualified') and rejection_reason='Small Purchase' then 'Rejected Leads - Small Purchase'
when lead_stage_to in ('Marketing Disqualified','Sales Disqualified')  then 'Disqualified Leads'
when lead_stage_to in ('Marketing Rejected','Sales Rejected','Marketing Disqualified','Sales Disqualified') then 'Rejected Leads'
when lead_stage_to in ('Marketing Accepted','Sales Accepted') then 'Accepted Leads' END as Lead_Type,
c.lead_id
from  APL_VDB_SFDC_SALES.sfdc_lead_mngmnt_hist c
full outer join APL_VDB_SFDC_SALES.sfdc_lead d on c.lead_id=d.lead_id
WHERE  c.lead_id is not null
AND  EXTRACT(year from c.created_date_est) >= '2020'
order by c.lead_id

limit 100000


--select MONTHNAME(NOW())
