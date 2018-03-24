insert into sec_agent_type_info
select gs_agent_data.日期,o32_agent_data_uniq.品种,
       sum(replace(gs_agent_data.净价成本,',','')) "品种成本",
       sum(replace(gs_agent_data.公允价值,',','')) "品种市值",
	   sum(replace(gs_agent_data.全价总市值,',','')) "全价总市值"
  from gs_agent_data,o32_agent_data_uniq
where o32_agent_data_uniq.证券名称 = gs_agent_data.证券名称 
and gs_agent_data.日期 = 