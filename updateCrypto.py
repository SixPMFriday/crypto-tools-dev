'''
Functions to return data that is regularly addded to the
crypto database. Both return a dictionary item. 
getDailyMetrics
'''

import json
import pandas as pd
from six.moves import urllib #for python urllib clarity
import pprint


# Daily data
# Pull daily
def getDailyMetrics(symbol):
	base_url = "https://data.messari.io/api/v1"
	endpoint = "/assets/{0}/metrics".format(symbol)
	url = base_url + endpoint
	d = json.loads(urllib.request.urlopen(url).read())
	dailyMetrics = d["data"]["blockchain_stats_last_24_hours"]
	return dailyMetrics

# Market data
# Pull hourly
def getMarketData(symbol):
	base_url = "https://data.messari.io/api/v1"
	endpoint = "/assets/{0}/metrics".format(symbol)
	url = base_url + endpoint
	d = json.loads(urllib.request.urlopen(url).read())
	marketData = d["data"]["market_data"]
	return marketData


if __name__ == "__main__":
	pp = pprint.PrettyPrinter()

	print("\nDaily Metrics:")
	pp.pprint(getDailyMetrics("eth"))

	print("\nMarket Data:")
	pp.pprint(getMarketData("eth"))

