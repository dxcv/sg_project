insert into sec_type_info
select c.日期,c.品种,c.品种成本,c.品种市值,c.品种浮动盈亏,c.品种资本利得,
       c.品种利息收入,c.品种总体盈亏,c.品种证券总面值,c.可交易品种浮动盈亏,
       d.持有到期品种浮动盈亏,c.品种全价总市值
  from     
(select a.日期,a.品种,a.品种成本,a.品种市值,a.品种浮动盈亏,a.品种资本利得,
       a.品种利息收入,a.品种总体盈亏,a.品种证券总面值,b.可交易品种浮动盈亏,
	   a.品种全价总市值
from 
(select gs_data.日期,o32_data_uniq.品种,
       sum(replace(gs_data.净价成本,',','')) "品种成本",
       sum(replace(gs_data.公允价值,',','')) "品种市值",
	   sum(replace(gs_data.浮动盈亏,',','')) "品种浮动盈亏",
	   sum(replace(gs_data.资本利得,',','')) "品种资本利得",
	   sum(replace(gs_data.利息收入,',','')) "品种利息收入",
	   sum(replace(gs_data.总体盈亏,',','')) "品种总体盈亏",
	   sum(replace(gs_data.证券总面值,',','')) "品种证券总面值",
	   sum(replace(gs_data.全价总市值,',','')) "品种全价总市值"
  from gs_data,o32_data_uniq
where o32_data_uniq.证券名称 = gs_data.证券名称
group by gs_data.日期,o32_data_uniq.品种) a
left join 
(select gs_data.日期,o32_data_uniq.品种,
	   sum(replace(gs_data.浮动盈亏,',','')) "可交易品种浮动盈亏"
  from gs_data,o32_data_uniq
where o32_data_uniq.证券名称 = gs_data.证券名称
  and o32_data_uniq.投资类型 = '可交易'
group by gs_data.日期,o32_data_uniq.品种) b
on( a.日期 = b.日期 and a.品种 = b.品种)) c
left join 
(select gs_data.日期,o32_data_uniq.品种,
	   sum(replace(gs_data.浮动盈亏,',','')) "持有到期品种浮动盈亏"
  from gs_data,o32_data_uniq
where o32_data_uniq.证券名称 = gs_data.证券名称
  and o32_data_uniq.投资类型 = '持有到期'
group by gs_data.日期,o32_data_uniq.品种)d
on (c.日期 = d.日期 and c.品种 = d.品种)