---sqlite 获取text格式调整为日期格式，并获取上一日，及上个月最后一天
select 
       date(
       strftime(substr(sec_type_info.日期,1,4 )||'-'||substr(sec_type_info.日期,5,2 )
       ||'-'||substr(sec_type_info.日期,7,2 )) 
       ,'-1 day','-1 month','+0 year')  up_day,
       strftime('%Y-%m-%d',
       strftime(substr(sec_type_info.日期,1,4 )||'-'||substr(sec_type_info.日期,5,2 )
       ||'-'||substr(sec_type_info.日期,7,2 ))   
       ,'start of month','-0 month','-1 day')  last_month_lastday
from sec_type_info;

--上个月最后一天的参考语句
select strftime('%Y-%m-%d','2018-02-22','start of month','-1 month','-1 day');

--上个月最后一天的参考语句，本地表获取
select substr(test.day1,1,6), max(test.day1) ,count() from test
group by substr(test.day1,1,6) order by substr(test.day1,1,6) desc limit  2
