create table o32_data_uniq as
select a.组合名称,a.证券代码,a.证券名称,a.交易市场,a.投资类型,a.证券类别,b.万得证券分类,
       case  when b.万得证券分类 = '短期融资券' and a.证券类别 = '企债' then '短期融资券'
             when b.万得证券分类 <> '短期融资券' and a.证券类别 = '企债' then '企业债/公司债/中期票据'
        else a.品种 end as 品种
 from o32_data_uniq_orig a left join
 (select gs_data.证券名称,gs_data.证券代码,gs_data.万得证券分类
   from gs_data where gs_data.日期 =