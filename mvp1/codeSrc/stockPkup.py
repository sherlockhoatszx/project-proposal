# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Done: filter the date when close price cross the ma5 line
#todo1:the defination of "the 'first time' cross ma5 line" 
#todo2:replace the end date with today automatically
#2AM Dec-7-2015,sherlock
#5PM Dec-7-2015,veratulips

import tushare as ts
import time
from datetime import date, timedelta

##### initialize parametes #####
stockList = '601318' # stockList[0] = '601318' index sys starts from 0
k = '60' # k type: 60 minutes

today = date.today()
# wd = date.isoweekday(today) # weekday starts from 1
days = timedelta(days=10) # no of days in between
begin = date.isoformat(today-days) # start date of history data
finish = date.isoformat(today) # end date of history data

threshold_buy = 0.02 # judge rule of how to choose the buy point
# today =date.today() it seems that this date maynot be necessary

##### get hist data #####
histData = ts.get_hist_data(stockList, ktype= k ,start = begin, end = finish)  

##### rule 1: when close - ma5 > 0.02, choose #####
histData['increaseRate']=(histData['close']-histData['ma5'])/histData['ma5']
screen1 = histData[histData.increaseRate>threshold_buy]

##### rule 2.1: filted data exits in current day #####
##### rule 2.2: filted data haven't shown this in past 10 days
