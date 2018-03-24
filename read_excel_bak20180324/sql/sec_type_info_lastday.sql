create table sec_type_info_lastday as
select b.品种,b.上日日期,c.品种总体盈亏 as 上日品种总体盈亏 
  from (select a.品种, max(a.日期) as 上日日期 
          from sec_type_info a 
         where a.日期 < 