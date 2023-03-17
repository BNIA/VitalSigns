# -*- coding: utf-8 -*-
"""
This notebook uses the Banks 2021 data to create a portion of BNIA's Vital Signs report

###Indicator from this csv
*   banks

###Tables used in this notebook
*   Banks_2021
*   CSA2010 to CSA2020 Crosswalk
*   2020 Population
"""

#export
#Import needed libraries
import pandas as pd

#Export
#Read data
banks = pd.read_excel("Banks_2021_CSA _City.xlsx")
crosswalk = pd.read_csv("https://raw.githubusercontent.com/BNIA/VitalSigns/main/CSA2010_2020.csv")
pop_2020 = pd.read_csv("CSA2020_CSA2010_&_2020pop.csv")

#Remove rows where Baltimore City is empty
banks = banks[banks['BaltCity'] != '']

"""###banks"""

#Export
#Banks Indicator
#Rate of Banks and Bank Branches per 1,000 Residents

#Only keep needed columns
banks = banks[['CSA']]

#Add counter
banks['count'] = 1

#Add Baltimore City row
banks.loc[len(banks.index)] = ['Baltimore City', banks['count'].sum()]

#Group by CSA
banks = banks.groupby("CSA").sum()

#Append 2010 CSAs
banks = crosswalk.merge(banks, left_on="CSA2020", right_on="CSA", how="outer")

#Append 2020 Population
banks = banks.merge(pop_2020, on=["CSA2010", "CSA2020"], how='outer')

#Get banks indicator
banks['banksXX'] = (banks['count'] / banks['tpop20']) * 1000

#Sort rows alphabetically 
banks = banks.sort_values('CSA2010')