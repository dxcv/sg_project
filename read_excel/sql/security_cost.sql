select a.品种,a.品种成本,a.品种市值,a.品种浮动盈亏,a.品种资本利得,
       a.品种利息收入,a.品种总体盈亏,a.日期,
       a.品种总体盈亏 - a.上日品种总体盈亏 as 日盈亏变动,
       a.品种总体盈亏 - a.上月品种总体盈亏 as 月盈亏变动,
       a.品种总体盈亏 - a.上年品种总体盈亏 as 年盈亏变动,
	   a.品种证券总面值,
	   a.可交易品种浮动盈亏,
	   a.持有到期品种浮动盈亏,
	   a.品种全价总市值
  from sec_type_info_all a