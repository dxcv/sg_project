insert into gs_agent_data
select a.交易对手,a.证券代码,a.证券名称,a.代持到期日,a.净价价格,a.持仓数量,
       a.净价成本,a.公允价值,a.公允价值变动,a.日期,a.code_windl1_type as 万得证券分类,
	   a.持仓数量 * case a.code_exch_city when '银行间债券' then a.code_dirty_cnbd else a.code_dirty_price end as 全价总市值
  from gs_agent_result a
where a.代持到期日 is not null