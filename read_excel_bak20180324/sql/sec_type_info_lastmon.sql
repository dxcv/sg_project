create table sec_type_info_lastmon as
select d.品种,d.日期 as 上月最大日期,e.品种总体盈亏 as 上月品种总体盈亏
from
(
--选出每月最大一天后，再选最大的日期，即上月最后一天
select c.品种,max(c.日期) as 日期
from
(
select b.品种,b.月份,b.日期
from
(
--每月最大日期
select a.品种, substr(a.日期,1,6) as 月份,max(a.日期) as 日期
  from sec_type_info a
group by a.品种,substr(a.日期,1,6)
) b
where b.日期 <--小于表格最大日期
 (
 --最大日期，即今天
 select max(t.日期) as 日期
from sec_type_info t
where b.品种 = t.品种
group by t.品种)
)c
group by c.品种
)d,sec_type_info e
where d.品种 = e.品种
  and d.日期 = e.日期