create table o32_data_uniq as
select distinct o32_data.组合名称,o32_data.证券代码,o32_data.证券名称,o32_data.交易市场,
       o32_data.投资类型,o32_data.证券类别,o32_data.品种
from o32_data