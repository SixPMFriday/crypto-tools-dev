# Messari API Testing
# (!) indicates real-time data

import json
import pandas as pd
from six.moves import urllib #for python urllib clarity
import pprint


# Function to call api based on input argument
class Messari():
	def __init__(self):
		self.base_url = "https://data.messari.io/api/v1"

	def _callAPI(self, endpoint):
		url = self.base_url + endpoint
		d = json.loads(urllib.request.urlopen(url).read())
		return d

	#API functions
	#source: https://messari.io/api/docs

	def _getAllMarkets(self):
	# (!) Get the list of all exchanges and pairs that our 
	# WebSocket-based market real-time market data API supports.
		endpoint = "/markets"
		return self._callAPI(endpoint)

	def _getAllAssets(self):
	# Get the list of all crypto assets that our non-real-time 
	# data REST API supports.
	# Json response["data"] is a list of dict with keys name, symbol
		endpoint = "/assets"
		return self._callAPI(endpoint)

	def _getProfileBySymbol(self, symbol):
	# Get fundamental information by asset symbol.
		endpoint = "/assets/{0}/profile".format(symbol)
		return self._callAPI(endpoint)

	def _getMetricsBySymbol(self, symbol):
	# Get fundamental information by asset symbol.
		endpoint = "/assets/{0}/metrics".format(symbol)
		return self._callAPI(endpoint)

	def _getNews(self):
	# Get fundamental information by asset symbol.
		endpoint = "/news"
		return self._callAPI(endpoint)

	def _getNewsBySymbol(self, symbol):
	# Get fundamental information by asset symbol.
		endpoint = "/news/{0}".format(symbol)
		return self._callAPI(endpoint)

# Returns df with all Messari tokens
# (name, symbol)
# def getMessariExchanges():
def getMarkets():
	messari = Messari()
	res = messari._getAllMarkets()
	#print(tokenlist["status"])
	df = pd.DataFrame(res["data"]).sort_values(by=["exchange", "pair"])#, "quote", "base"])
	return df

# Returns df with all Messari tokens
# (name, symbol)
# def getMessariTokens():
def getAssets():
	messari = Messari()
	res = messari._getAllAssets()
	#print(tokenlist["status"])
	df = pd.DataFrame(res["data"]).sort_values(by=["name"])
	return df

def getProfile(symbol):
	messari = Messari()
	res = messari._getProfileBySymbol(symbol)
	pp = pprint.PrettyPrinter()
	pp.pprint(res["data"])

def getMetrics(symbol):
	messari = Messari()
	res = messari._getMetricsBySymbol(symbol)
	pp = pprint.PrettyPrinter()
	pp.pprint(res["data"])
	print(type(res))

def getDailyMetrics(symbol):
	messari = Messari()
	res = messari._getMetricsBySymbol(symbol)
	df = pd.DataFrame(res["data"])

	pp.pprint(res["data"])
	print(type(res))

def getNews(symbol=None):
	messari = Messari()
	if symbol == None:
		res = messari._getNews()
		pp = pprint.PrettyPrinter()
		pp.pprint(res["data"])
	else:
		res = messari._getNewsBySymbol(symbol)
		pp = pprint.PrettyPrinter()
		pp.pprint(res["data"])


#df = getMarkets() #getMessariExchanges()
#print(df)

# _getProfileBySymbol
# Get fundamental information by asset symbol.
