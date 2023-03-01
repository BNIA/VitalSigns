# -*- coding: utf-8 -*-
"""
This notebook uses the Permits 2021 data to create a portion of BNIA's Vital Signs report

###Indicators from this csv
*   resrehab
*   crehab (calculate ComProp first)
*   demper
*   constper

###Tables used in this notebook
*   Permits_2021
*   TotalRes_2021 (BNIA Indicator)
*   MDPropertyView_2021
"""

#export
#Import needed libraries
import pandas as pd

#export
#Read data
permits = pd.read_excel("Permits_2021v2_CSACity.xlsx")
totalRes_2021 = pd.read_csv("totalRes_2021.csv")
mdProp = pd.read_csv("MDPropertyView_2021_CSACity.csv")
crosswalk = pd.read_csv('https://raw.githubusercontent.com/BNIA/VitalSigns/main/CSA_2010_and_2020.csv')



#Remove rows where BaltCity is empty
permits = permits[permits['BaltCity'] != '']
mdProp = mdProp[mdProp['BaltCity'] != '']

#Keep necessary columns from crosswalk table
crosswalk = crosswalk[['CSA2010', 'CSA2020']]
#Remove duplicate rows.
crosswalk = crosswalk.drop_duplicates()

"""###resrehab"""

#export
#resrehab Indicator
#Output - Percentage of properties with rehabilitation permits exceeding $5k

#Filter data
resrehab = permits[
    (permits['csm_cost'] > 5000) &
    (permits['csm_type_w'].str.contains('AA|ADD|ALT', regex=True)) &
    (permits['case_type'].str.contains('COM', regex=True)) &
    (permits['com_existi'].str.contains('SF|MF|DFAM|1-', regex=True)) &
    (permits['csm_use'].str.contains('SF|MF|DFAM|1-', regex=True))
]

#Only keep needed columns
resrehab = resrehab[['CSA2020']]

#Add indicator column
resrehab['permit_count'] = 1

#Group by CSAs
resrehab = resrehab.groupby('CSA2020').sum(numeric_only=True) 

#make index the CSA2020 column
resrehab.reset_index(inplace=True)

#Add Baltimore City row
resrehab.loc[len(resrehab.index)] = ['Baltimore City', resrehab['permit_count'].sum()]

#Merge table with TotalRes indicator
resrehab = resrehab.merge(totalRes_2021, on='CSA2020', how='outer')

#Create indicator
resrehab['resrehabXX'] = (resrehab['permit_count']/resrehab['totalres'])*100

#Change column order to clean things up.
resrehab = resrehab[['CSA2010', 'CSA2020', 'permit_count', 'totalres', 'resrehabXX']]

"""###crehab

####Comprop (from MDProperty View)
"""

#export
#comprop - denominator used for crehab indicator.

#Filter data
comprop = mdProp[mdProp['LU'].isin(['C','EC','I'])]

#Only keep needed columns
comprop = comprop[['CSA']]

#Add counter
comprop['comprop'] = 1

#Group by CSAs
comprop = comprop.groupby('CSA').sum(numeric_only=True) 

#make index the CSA2020 column
comprop.reset_index(inplace=True)

#Rename column
comprop = comprop.rename(columns={'CSA': 'CSA2010'})

#Add Baltimore City row
comprop.loc[len(comprop.index)] = ['Baltimore City', comprop['comprop'].sum()]

#Append 2020 CSA names
comprop = comprop.merge(crosswalk, on='CSA2010', how='inner')

comprop

#export
#crehab Indicator
#Output - Percentage of Commercial properties with rehabilitation permits exceeding $5k

#Filter data
crehab = permits[
    (permits['csm_cost'] > 5000) &
    (permits['csm_type_w'].str.contains('AA|ADD|ALT', regex=True)) &
    (permits['com_existi'].str.contains('2-|3-|4-|5-|6-|7-|COM|IND|BUS|AIR|ANIM|BAR|BEAU|DELI|FAC|ASM|ALV|DOTH|DWC|EDU|FOOD|HCF|HIH|HOS|MIXC|INS|MER|LIB|MNTL|MOB|PUB|STO|UT|VAC|VAL|DFAM', regex=True)) &
    (permits['csm_use'].str.contains('2-|3-|4-|5-|6-|7-|COM|IND|BUS|AIR|ANIM|BAR|BEAU|DELI|FAC|ASM|ALV|DOTH|DWC|EDU|FOOD|HCF|HIH|HOS|MIXC|INS|MER|LIB|MNTL|MOB|PUB|STO|UT|VAC|VAL|DFAM', regex=True))
]

#Only keep needed columns
crehab = crehab[['CSA2020']]

#Add indicator column
crehab['permit_count'] = 1

#Group by CSAs
crehab = crehab.groupby('CSA2020').sum(numeric_only=True) 

#make index the CSA2020 column
crehab.reset_index(inplace=True)

#Add Baltimore City row
crehab.loc[len(crehab.index)] = ['Baltimore City', crehab['permit_count'].sum()]

#Merge table with comprop table
crehab = crehab.merge(comprop, on='CSA2020', how='inner')

#calculate indicator
crehab['crehabXX'] = (crehab['permit_count']/ crehab['comprop']) *100

#Change column order to clean things up.
crehab = crehab[['CSA2010', 'CSA2020', 'permit_count', 'comprop', 'crehabXX']]

crehab

"""####demper"""

#export
#demper Indicator
#Output - Number of demolition permits per 1000 residential properties

#Filter data
demper = permits[
    (permits['csm_type_w'].str.contains('DEM', regex=True, na=False)) &
    (permits['PLANADDRES']  != '')         
]

#Only keep needed columns
demper = demper[['CSA2020']]

#Add indicator column
demper['permit_count'] = 1

#Group by CSAs
demper = demper.groupby('CSA2020').sum(numeric_only=True) 

#make index the CSA2020 column
demper.reset_index(inplace=True)

#Add Baltimore City row
demper.loc[len(demper.index)] = ['Baltimore City', demper['permit_count'].sum()]

#Merge table with TotalRes indicator
demper = demper.merge(totalRes_2021, on='CSA2020', how='outer')

#Create indicator
demper['demperXX'] = (demper['permit_count'] / demper['totalres']) *1000

#Sort rows alphabetically 
demper = demper.sort_values('CSA2010')

#Change column order to clean things up.
demper = demper[['CSA2010', 'CSA2020', 'permit_count', 'totalres', 'demperXX']]

"""###constper"""

#export
#demper Indicator
#Output - Number of of new construction permits per 1000 residential properties

#Filter data
constper = permits[
    (permits['csm_type_w'].str.contains('NEW', regex=True, na=False)) &
    (permits['PLANADDRES']  != '')         
]

#Only keep needed columns
constper = constper[['CSA2020']]

#Add indicator column
constper['permit_count'] = 1

#Group by CSAs
constper = constper.groupby('CSA2020').sum(numeric_only=True) 

#make index the CSA2020 column
constper.reset_index(inplace=True)

#Add Baltimore City row
constper.loc[len(constper.index)] = ['Baltimore City', constper['permit_count'].sum()]

#Merge table with TotalRes indicator
constper = constper.merge(totalRes_2021, on='CSA2020', how='outer')

#Create indicator
constper['constperXX'] = (constper['permit_count'] / constper['totalres']) *1000

#Sort rows alphabetically 
constper = constper.sort_values('CSA2010')

#Change column order to clean things up.
constper = constper[['CSA2010', 'CSA2020', 'permit_count', 'totalres', 'constperXX']]

from google.colab import files 
resrehab.to_csv('resrehab_2021.csv')
files.download('resrehab_2021.csv')