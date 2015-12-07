项目最小可用单元1.0版本的描述：
功能清单

- [x] step 1 : filter the rowdata when close price cross the ma5

- [ ] step 2 : filted data fulfill that (1) the filted results exist in current day AND (2) the filted results have shown in the past 10 days.

	- minor progress: date data calculation. (code line 21-23)

	```
	days = datetime.timedelta(days=10) # no of days in between
	begin = date.isoformat(today-days) # start date of history data
	finish = date.isoformat(today) # end date of history data
	```

	- pandas.core.frame.DataFrame data structure, because you need to know the data structure and then make the judgement. 2015-12-07-16:48
