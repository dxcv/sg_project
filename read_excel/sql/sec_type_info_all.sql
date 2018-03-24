create table sec_type_info_all as
select e.品种,e.品种成本,e.品种市值,e.品种浮动盈亏,e.品种资本利得,
       e.品种利息收入,e.品种总体盈亏,e.日期,e.品种证券总面值,
	   e.可交易品种浮动盈亏,
	   e.持有到期品种浮动盈亏,
	   e.品种全价总市值,
	   e.上日品种总体盈亏,
       e.上月品种总体盈亏,f.上年品种总体盈亏
  from
(select c.品种,c.品种成本,c.品种市值,c.品种浮动盈亏,c.品种资本利得,
       c.品种利息收入,c.品种总体盈亏,c.日期,c.品种证券总面值,
	   c.可交易品种浮动盈亏,
	   c.持有到期品种浮动盈亏,
	   c.品种全价总市值,
	   c.上日品种总体盈亏,
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
	   a.品种证券总面值,
	   a.可交易品种浮动盈亏,
	   a.持有到期品种浮动盈亏,
	   a.品种全价总市值,
       b.上日品种总体盈亏
 from sec_type_info a left join
      sec_type_info_lastday b
on a.品种 = b.品种
  where a.日期 =  