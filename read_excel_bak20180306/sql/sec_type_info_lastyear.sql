create table sec_type_info_lastyear as
select d.品种,d.日期 as 上年最大日期,e.品种总体盈亏 as 上年品种总体盈亏
from
(
--选出每年最大一天后，再选最大的日期，即上年最后一天
select c.品种,max(c.日期) as 日期
from
(
select b.品种,b.年份,b.日期
from
(
--每年最大日期
select a.品种, substr(a.日期,1,4) as 年份,max(a.日期) as 日期
  from sec_type_info a
group by a.品种,substr(a.日期,1,4)
) b
where b.日期 <>--排除今天
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