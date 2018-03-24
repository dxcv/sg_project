create table sec_type_info_lastday as
select b.品种,b.上日日期,c.品种总体盈亏 as 上日品种总体盈亏
from
(
--上一日期
select a.品种, max(a.日期) as 上日日期
  from sec_type_info a
where a.日期 <>--排除今天
 (
 --最大日期，即今天
 select max(t.日期) as 日期
from sec_type_info t
where a.品种 = t.品种
group by t.品种)
group by a.品种
)b,sec_type_info c
where b.品种 = c.品种
and b.上日日期 = c.日期