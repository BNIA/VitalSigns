# -*- coding: utf-8 -*-
"""
This notebook uses the EnochPratt 2021 data to create a portion of BNIA's Vital Signs report

###Indicator from this csv
*   libcard

###Tables used in this notebook
*   Enochpratt_2021
*   CSA2010 to CSA2020 Crosswalk
*   2020 Population
"""

import pandas as pd

#export
#read data
libcard = pd.read_excel("EnochPratt_2021CSA_City.xlsx")
crosswalk = pd.read_csv("https://raw.githubusercontent.com/BNIA/VitalSigns/main/CSA2010_2020.csv")
pop_2020 = pd.read_csv("CSA2020_CSA2010_&_2020pop.csv")

#Remove rows where BaltCity is empty
libcard = libcard[libcard["BaltCity"] == "Baltimore City"]

"""###libcard"""

#Export
#libcard Indicator
#Rate of persons per 1,000 residents that possess a valid public library system card

#Keep needed columns
libcard = libcard[['CSA']]

#Add counter
libcard['count'] = 1

#Add Baltimore City row
libcard.loc[len(libcard.index)] = ['Baltimore City', libcard['count'].sum()]

#Group by CSA
libcard = libcard.groupby("CSA").sum()

#Append 2010 CSAs
libcard = crosswalk.merge(libcard, left_on="CSA2020", right_on="CSA", how="outer")

#Append 2020 Population
libcard = libcard.merge(pop_2020, on=["CSA2010", "CSA2020"], how='outer')

#Get libcard indicator
libcard['libcardsXX'] = (libcard['count'] / libcard['tpop20']) * 1000

#Sort rows alphabetically 
libcard = libcard.sort_values('CSA2010')