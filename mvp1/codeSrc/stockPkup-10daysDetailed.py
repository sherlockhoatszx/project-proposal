# -*- coding: utf-8 -*-
#!/usr/bin/env python
#Done: filter the date when close price cross the ma5 line
#todo1:the defination of "the 'first time' cross ma5 line" 
#todo2:replace the end date with today automatically
#2AM Dec-7-2015,sherlock
#2PM Dec-7-2015,veratulips

import tushare as ts
import time
from datetime import date


##### initialize parametes #####
stockList = '601318' # stockList[0] = '601318' index sys starts from 0
k = '60' # k type: 60 minutes

today = date.today()

wd = date.isoweekday(today) # weekday starts from 1
step = datetime.timedelta(days=1)

while True: #(wd)
	if wd != 6 && wd != 7:
		wd_count += 1
		wd = date.isoweekday(today-step)
	else: 
		wend_count += 1

	if wd_count == 10:
		break



days = datetime.timedelta(days=wend_count+wd_count) # no of days in between
begin = date.isoformat(today-days) # start date of history data
finish = date.isoformat(today) # end date of history data

threshold_buy = 0.02 # judge rule of how to choose the buy point
# today =date.today() it seems that this date maynot be necessary


##### get hist data #####
histData = ts.get_hist_data(stockList, ktype= k ,start = begin, end = finish)  

##### rule: when close - ma5 > 0.02, choose #####
histData['increaseRate']=(histData['close']-histData['ma5'])/x['ma5']
screen1 = histData[histData.increaseRate>threshold_buy]

print x
print y
# print today
