insert into o32_agent_data
select o32_result.日期,o32_result.组合名称,o32_result.证券代码,o32_result.证券名称,o32_result.交易市场,
       o32_result.投资类型,o32_result.证券类别,o32_result.净价成本,o32_result.市值,
	   o32_result.当日浮动盈亏,o32_result.总体盈亏,accounting_subject.report_subject "品种"
  from o32_result,accounting_subject
 where o32_result.证券类别 = accounting_subject.o32_subject
   and o32_result.基金编号 in (100,101)
   and o32_result.组合编号  in ('005','010')
   and o32_result.持仓多空标志 = '多仓'
 union
 select o32_result.日期,o32_result.组合名称,o32_result.证券代码,o32_result.证券名称,o32_result.交易市场,
       o32_result.投资类型,o32_result.证券类别,o32_result.净价成本 ,o32_result.市值,
	   o32_result.当日浮动盈亏,o32_result.总体盈亏,'其他' "品种"
   from o32_result
  where o32_result.证券类别 not in ('国债标准券','买断式回购','债券回购','协议质押式回购')
     and o32_result.基金编号 in (100,101)
   and o32_result.组合编号  in ('005','010')
   and o32_result.持仓多空标志 = '多仓'
  and o32_result.证券类别 not in
  (select  distinct o32_result.证券类别
    from  o32_result,accounting_subject
 where o32_result.证券类别 = accounting_subject.o32_subject
   and o32_result.基金编号 in (100,101)
   and o32_result.组合编号  in ('005','010'))