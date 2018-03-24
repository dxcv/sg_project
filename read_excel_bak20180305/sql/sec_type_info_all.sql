create table sec_type_info_all as
select e.品种,e.品种成本,e.品种市值,e.品种浮动盈亏,e.品种资本利得,
       e.品种利息收入,e.品种总体盈亏,e.日期,e.上日品种总体盈亏,
       e.上月品种总体盈亏,f.上年品种总体盈亏
  from
(select c.品种,c.品种成本,c.品种市值,c.品种浮动盈亏,c.品种资本利得,
       c.品种利息收入,c.品种总体盈亏,c.日期,c.上日品种总体盈亏,
       d.上月品种总体盈亏
  from
(select a.品种,
       a.品种成本,
       a.品种市值,
       a.品种浮动盈亏,
       a.品种资本利得,
       a.品种利息收入,
       a.品种总体盈亏,
       a.日期,
       b.上日品种总体盈亏
 from sec_type_info a left join
      sec_type_info_lastday b
on a.品种 = b.品种
  where a.日期 =
   (
 --最大日期，即今天
 select max(t.日期) as 日期
from sec_type_info t
where a.品种 = t.品种
group by t.品种)
)c left join sec_type_info_lastmon d
on c.品种 = d.品种
) e left join sec_type_info_lastyear f
on e.品种 = f.品种