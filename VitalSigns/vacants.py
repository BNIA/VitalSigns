# -*- coding: utf-8 -*-
"""
This notebook uses the Vacants 2021 data to create a portion of BNIA's Vital Signs report

###Indicators from this csv
*   vacant
*   baltVac (uses vacant indicator)

###Tables used in this notebook
*   Vacants_2021
*   TotalRes_2021 (BNIA Indicator)
"""

#export
#Import needed libraries
import pandas as pd

#export
#Read data
vacants = pd.read_csv("Vacants_2021_CSACity.csv", encoding="cp850")
totalRes_2021 = pd.read_csv("totalRes_2021.csv")

#Remove rows where BaltCity is empty
vacants = vacants[vacants['BaltCity'] != '']

"""###vacant"""

#export
#vacant indicator
#Percentage of Residential Properties that are Vacant and Abandoned

#Only keep needed columns
vacant = vacants[['CSA2010','CSA2020']]

#Add indicator column
vacant['vacant_count'] = 1

#Group by CSAs
vacant = vacant.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2010 & CSA2020 column
vacant.reset_index(inplace=True)

#Add Baltimore City row
vacant.loc[len(vacant.index)] = ['Baltimore City', 'Baltimore City', vacant['vacant_count'].sum()]

#Merge table with TotalRes indicator
vacant = vacant.merge(totalRes_2021, on=['CSA2010','CSA2020'], how='outer')

#Create indicator
vacant['vacantXX'] = (vacant['vacant_count']/vacant['totalres'])*100

"""###baltvac"""

#export
#baltvac indicator
#Percentage of Vacant Properties Owned by Baltimore City

#Filter data
baltvac = vacants[(vacants['OWNER_ABBR'].str.contains('DHCD|HABC|HUD|MCC|USA', regex=True, na=False))]

#Only keep needed columns
baltvac = baltvac[['CSA2010','CSA2020']]

#Add indicator column
baltvac['batvac_count'] = 1

#Group by CSAs
baltvac = baltvac.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2010 & CSA2020 column
baltvac.reset_index(inplace=True)

#Add Baltimore City row
baltvac.loc[len(baltvac.index)] = ['Baltimore City', 'Baltimore City', baltvac['batvac_count'].sum()]

#Merge table with vacant indicator
baltvac = baltvac.merge(vacant, on=['CSA2010','CSA2020'], how='outer')

#Only keep needed columns
baltvac = baltvac[['CSA2010','CSA2020', 'batvac_count', 'vacant_count']]

#calcualte indicator
baltvac['baltvacXX'] = (baltvac['batvac_count']/baltvac['vacant_count'])*100

#Sort rows alphabetically 
baltvac = baltvac.sort_values('CSA2010')

from google.colab import files 
vacants.to_csv('vacants.csv')
files.download('vacants.csv')