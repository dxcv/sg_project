delete from o32_agent_data where (o32_agent_data.日期,o32_agent_data.证券代码,o32_agent_data.证券名称,o32_agent_data.交易市场) in
(select o32_agent_data.日期,o32_agent_data.证券代码,o32_agent_data.证券名称,o32_agent_data.交易市场
   from o32_agent_data
group by o32_agent_data.日期,o32_agent_data.证券代码,o32_agent_data.证券名称,o32_agent_data.交易市场 having count(*) > 1)
and rowid not in (select min(rowid) from o32_agent_data group by o32_agent_data.日期,o32_agent_data.证券代码,o32_agent_data.证券名称,o32_agent_data.交易市场
having count(*) > 1)