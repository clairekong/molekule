#!/usr/bin/python
# -*- coding: UTF-8 -*-
#coding=utf-8 

import datetime
import json
import numpy as np
import os
import pandas as pd
import random
import requests
import time
import traceback

print("Fetching...")

csv_header = [u"country", u"province", u"confirmed", u"recovered", u"deaths", u"active", u"latitude", u"longitude", u"date"]
appkey = "3cc7e29631msh7cee92aae021fbfp15ff33jsn261ecaba7473"
url = "https://covid-19-data.p.rapidapi.com/report/country/all"
headers = {
    'x-rapidapi-key': appkey,
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }


begin_day = "2020-03-01"
begin_time = time.mktime(time.strptime(begin_day, "%Y-%m-%d"))
end_day = "2020-05-30"
end_time = time.mktime(time.strptime(end_day, "%Y-%m-%d"))
count_days = int((end_time - begin_time)/(24*60*60))
last_day = datetime.datetime.strptime(end_day, "%Y-%m-%d")
day_del = count_days


output_path = os.path.abspath('./molekule')
results = []

while day_del >= 0:
	sub_day = datetime.timedelta(days=day_del)
	target_date = last_day - sub_day
	target_date_str = target_date.strftime('%Y-%m-%d')
	querystring = {"date":target_date_str}

	response = requests.request("GET", url, headers=headers, params=querystring)
	response_data = json.loads(response.text)
	
	for _ditem in response_data:
		_country = _ditem['country']
		_latitude = str(_ditem['latitude'])
		_longitude = str(_ditem['longitude'])
		_date = _ditem['date']
		
		for _citem in _ditem['provinces']:
			row_data = [_country, _citem['province'], str(_citem['confirmed']), str(_citem['recovered']), str(_citem['deaths']), str(_citem['active']), _latitude, _longitude, _date]
			results.append(row_data)
		day_del -= 1

	df = pd.DataFrame(np.array(results), columns=csv_header)
	df.to_csv("covid_all_country.csv", encoding='utf-8')	
	print('All Request Complete.')
