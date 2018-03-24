insert into sec_type_info
select gs_data.日期,o32_data_uniq.品种,
       sum(replace(gs_data.净价成本,',','')) "品种成本",
       sum(replace(gs_data.公允价值,',','')) "品种市值",
	   sum(replace(gs_data.浮动盈亏,',','')) "品种浮动盈亏",
	   sum(replace(gs_data.资本利得,',','')) "品种资本利得",
	   sum(replace(gs_data.利息收入,',','')) "品种利息收入",
	   sum(replace(gs_data.总体盈亏,',','')) "品种总体盈亏"
  from gs_data,o32_data_uniq
where o32_data_uniq.证券名称 = gs_data.证券名称
group by gs_data.日期,o32_data_uniq.品种