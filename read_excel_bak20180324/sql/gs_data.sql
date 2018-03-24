insert into gs_data
select gs_result.日期,gs_result.证券名称,gs_result.证券代码,gs_result.证券类别,
       gs_result.市场,gs_result.净价成本,gs_result.公允价值,gs_result.浮动盈亏,
	   gs_result.资本利得,gs_result.利息收入,gs_result.总体盈亏,gs_result.证券总面值,
	   gs_result.万得证券分类,gs_result.全价总市值
  from gs_result
where gs_result.证券代码 <> '(空白)' and gs_result.证券名称 <> '基金名称'
and gs_result.证券名称 <> '申港固收自营1号'
union
select replace(o32_result.日期,'-',''),o32_result.证券名称,o32_result.证券代码,o32_result.证券类别,
       o32_result.交易市场,o32_result.净价成本,o32_result.市值,o32_result.当日浮动盈亏,
	   '','',o32_result.总体盈亏,1*o32_result.持仓 as 证券总面值,
	   o32_result.证券类别,o32_result.市值 as 全价总市值
from o32_result where o32_result.证券名称 = '上投摩根岁岁金定期开放债券A'