
import Messari
#print(Messari.getAssets())
mets = Messari.getMetrics("eth")
#print(mets["blockchain_stats_last_24_hours"])
#print(Messari.getMetrics("ltc"))


'''
if __name__ == "__main__":
	xlsx = 'Messari.xlsx'
	writer = pd.ExcelWriter(xlsx, engine='xlsxwriter')

	df1 = getMarkets()
	df1.to_excel(writer, sheet_name='Markets', index=False, index_label=True, freeze_panes=(1,0))

	df2 = getAssets()
	df2.to_excel(writer, sheet_name='Assets', index=False, index_label=True, freeze_panes=(1,0))

	df3 = getProfile("eth")
	df4 = mess.getMetrics("eth")
	df5 = getNews()
	df6 = getNews("eth")

	writer.save()
'''

'''
{'all_time_high': {'days_since': 368,
                   'percent_down': 91.57490491033039,
                   'price': 1431.77},
 'blockchain_stats_last_24_hours': {'average_difficulty': 2633341356905588.5,
                                    'count_of_active_addresses': 271124,
                                    'count_of_blocks_added': 5629,
                                    'count_of_payments': 268880,
                                    'count_of_tx': 577239,
                                    'kilobytes_added': 103864.746,
                                    'median_tx_fee': 0.050663753265452284,
                                    'median_tx_value': 0.22974872000000002,
                                    'new_issuance': 2172378.054358718,
                                    'nvt': 36.309411350691555,
                                    'sum_of_fees': 61263.616379138286,
                                    'transaction_volume': 460766786.0618213},
 'developer_activity': {'commits_last_1_year': 1005,
                        'commits_last_3_months': 209,
                        'lines_added_last_1_year': 264824,
                        'lines_added_last_3_months': 25181,
                        'lines_deleted_last_1_year': 124236,
                        'lines_deleted_last_3_months': 15821,
                        'stars': 22357,
                        'watchers': 2036},
 'market_data': {'percent_change_btc_last_24_hours': 0.539091286708298,
                 'percent_change_usd_last_24_hours': 0.25878789383012923,
                 'price_btc': 0.033635389420815925,
                 'price_usd': 120.62798396536257,
                 'volume_last_24_hours': 2777828958.72},
 'misc_data': {'asset_age_days': 1266,
               'categories': ['Infrastructure'],
               'sectors': ['Smart Contract Platform'],
               'vladmir_cost_club': 1772940.0802878374},
 'roi_data': {'percent_change_last_1_month': 28.730294620893847,
              'percent_change_last_1_week': -10.704974796820146,
              'percent_change_last_1_year': -87.22997896089575,
              'percent_change_last_3_months': -39.595251062282784},
 'supply': {'circulating': 104415822, 'y_2050': 146975852.70072356},
 'symbol': 'eth'}
 '''
