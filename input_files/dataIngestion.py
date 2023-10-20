import pandas as pd

#Read in annual dividends
appl_ann_div_df = pd.read_json('annual_dividends/apple_div.json')
# print(appl_ann_div_df)

msft_ann_div_df = pd.read_json('annual_dividends/microsoft_div.json')
# print(msft_ann_div_df)

wlmt_ann_div_df = pd.read_json('annual_dividends/walmart_div.json')
# print(wlmt_ann_div_df)

######################################################################
#Read in annual stock prices

appl_ann_price_df = pd.read_json('annual_prices/apple_price.json')
# print(appl_ann_price_df)

msft_ann_price_df = pd.read_json('annual_prices/microsoft_price.json')
# print(msft_ann_price_df)

wlmt_ann_price_df = pd.read_json('annual_prices/walmart_price.json')
# print(wlmt_ann_price_df)

#####################################################################
#Read in company profile

appl_comp_prof_df = pd.read_json('company_profile/apple_prof.json')
# print(appl_comp_prof_df)

msft_comp_prof_df = pd.read_json('company_profile/microsoft_prof.json')
# print(msft_comp_prof_df )

wlmt_comp_prof_df = pd.read_json('company_profile/walmart_prof.json')
# print(wlmt_comp_prof_df)


#### MERGE DATAFRAMES BY COMPANY ####
merge_appl = pd.merge(appl_ann_div_df, appl_ann_price_df, how='inner', left_on='symbol', right_on='symbol')
final_merge_appl = pd.merge(merge_appl, appl_comp_prof_df, how='inner', left_on='symbol', right_on='symbol')
# print(final_merge_appl)


merge_msft = pd.merge(msft_ann_div_df, msft_ann_price_df, how='inner', left_on='symbol', right_on='symbol')
final_merge_msft = pd.merge(merge_msft, msft_comp_prof_df, how='inner', left_on='symbol', right_on='symbol')
# print(final_merge_msft)

merge_wlmt = pd.merge(wlmt_ann_div_df, wlmt_ann_price_df, how='inner', left_on='symbol', right_on='symbol')
final_merge_wlmt = pd.merge(merge_wlmt, wlmt_comp_prof_df, how='inner', left_on='symbol', right_on='symbol')
# print(final_merge_wlmt)


#### Write Company Data to CSV files ####
# final_merge_wlmt.to_csv('walmart_data.csv')

# final_merge_msft.to_csv('microsoft_data.csv')

# final_merge_appl.to_csv('apple_data.csv')

