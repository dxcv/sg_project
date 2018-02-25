select gs_result.*,o32_result.*
from (select * from  gs_result where gs_result.证券代码 <> '(空白)'
  and gs_result.证券名称 <> '基金名称'
  and gs_result.证券名称 <> '申港固收自营1号' )  gs_result
left outer join
   (select * from  o32_result where o32_result.证券代码 is not null)
   o32_result
on gs_result.证券名称 = o32_result.证券名称
union
select gs_result.*,o32_result.*
from
   (select * from  o32_result where o32_result.证券代码 is not null)
   o32_result
   left outer join
   (select * from  gs_result where gs_result.证券代码 <> '(空白)'
  and gs_result.证券名称 <> '基金名称'
  and gs_result.证券名称 <> '申港固收自营1号' )  gs_result
on gs_result.证券名称 = o32_result.证券名称