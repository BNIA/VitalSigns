# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/HUD.ipynb (unless otherwise specified).

__all__ = ['df', 'cdf', 'cdf', 'cdf', 'cdf2', 'cdf2']

# Cell
import pandas as pd

df = pd.read_csv("hcv_2019_BCityonly.csv");

# Cell
import numpy as np
df['tract'] = df['Code'].astype(str).str[4:].astype(np.int64)
df['tract']

# Cell
from dataplay.acsDownload import retrieve_acs_data
cdf = retrieve_acs_data(state, county, tract, tableId, year, saveAcs).reset_index()[['B25003_003E_Total:_Renter_occupied', 'tract']]

# Cell
df['B25003_003E_Total:_Renter_occupied'] = df.merge(cdf, left_on='tract', right_on='tract')['B25003_003E_Total:_Renter_occupied']
df.head()

# Cell
# Match Tract to CSA
df['CSA'] = df.merge(crosswalk, left_on='Code', right_on='GEOID10')['CSA2010']

# Cell
from math import floor
cdf = df.merge(crosswalk, left_on='Code', right_on='GEOID2010', how='left')
cdf["TRACT2010"] = cdf["TRACT2010"].fillna(0.0).astype(int)

# TRACTCE10 GEOID10 NAME10 CSA
cdf['TRACTCE10'] = cdf['TRACT2010']
cdf['GEOID10'] = cdf['Code']
cdf['CSA'] = cdf['CSA2010']

cdf = cdf.drop(columns=['TRACT2010', 'GEOID2010', 'Code', 'CSA2010', 'TRACT2010' ], axis=1)

# Cell
cdf2 = cdf.merge(cw2, left_on='TRACTCE10', right_on='TRACT', how='left')
cdf2['NAME10'] = cdf2['NEIGHBORHOOD']
cdf2 = cdf2.drop(columns=['TRACT', 'NEIGHBORHOOD'], axis=1)
cdf2.head(1)

# Cell
 cd3 = cdf2[[
           'NAME10',
           'TRACTCE10', 'CSA', 'GEOID10',
           'Summary level', 'Program label', 'Program', 'Sub-program', 'Name',
       'Subsidized units available', '% Occupied', '# Reported',
       '% Reported', 'Average months since report', '% moved in past year',
       'Number of people per unit', 'Number of people: total',
       'Average Family Expenditure per month ($$)',
       'Average HUD Expenditure per month ($$)', 'Household income per year',
       'Household income per year per person', '% $1 - $4,999',
       '% $5,000 - $9,999', '% $10,000 - $14,999', '% $15,000 - $19,999',
       '% $20,000 or more',
       '% Households where wages are major source of income',
       '% Households where welfare is major source of income',
       '% Households with other major sources of income',
       '% of local median (Household income)', '% very low income',
       '% extremely low income', '% 2+ adults with children',
       '% 1 adult with children', '% female head',
       '% female head with children',
       '% with disability, among Head, Spouse, Co-head, aged 61 years or less',
       '% with disability, among Head, Spouse, Co-head, aged 62 years or older',
       '% with disability, among all persons in households',
       '% 24 years or less (Head or spouse)',
       '% 25 to 49 years (Head or spouse)', '% 51 to 60 (Head or spouse)',
       '% 62 or more (Head or spouse)', '% 85 or more (Head or spouse)',
       '% Minority', '%Black Non-Hispanic', ' %Black Hispanic',
       '%Native American Non-Hispanic',
       '%Asian or Pacific Islander Non-Hispanic', '% Hispanic',
       'Average months on waiting list', 'Average months since moved in',
       '% with utility allowance', 'Average utility allowance $$',
       '% 0 - 1 bedrooms:', '% 2 bedrooms', '% 3+ bedrooms', '% Overhoused',
       '% in poverty (Census tract)', '% minority (Census tract)',
       '% single family owners (Census tract)', 'Congressional District',
       'CBSA', 'PLACE', 'Latitude', 'Longitude', 'State', 'PHA Total Units',
       'HA category']]