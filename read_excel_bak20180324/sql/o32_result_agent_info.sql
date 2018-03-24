select o32_result.基金名称,o32_result.组合编号,o32_result.组合名称,
       o32_result.证券代码,o32_result.证券名称,o32_result.交易市场,
       o32_result.持仓,o32_result.净价成本,o32_result.投资类型,
       o32_result.证券类别
  from o32_result
where o32_result.基金编号 in (100,101)
   and o32_result.组合编号 in ('005','010')
   and o32_result.证券类别 not in ('国债标准券','债券回购','协议质押式回购')