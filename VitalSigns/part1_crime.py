# -*- coding: utf-8 -*-
"""
This notebook uses the Part1_Crime data to create a portion of BNIA's Vital Signs report

####**Indicators from this csv**

*   crime
*   prop
*   vio
*   gunhom
"""

#export
#Import needed libraries
import pandas as pd

#export
#Read data - This dataset has been geocoded and has a few extra columns; CSA2010, CSA2020 & BaltCity.
original = pd.read_csv('Part1_2021_CSACity.csv')

#Only keep needed crime descriptions
crime_descriptions = ['AGG. ASSAULT', 'AUTO THEFT', 'BURGLARY', 'HOMICIDE',
                      'LARCENY', 'LARCENY FROM AUTO', 'RAPE', 'ROBBERY - CARJACKING',
                      'ROBBERY - COMMERCIAL', 'ROBBERY - RESIDENCE', 'ROBBERY - STREET']

p1Crime_2021 = original[(original['Descriptio'].isin(crime_descriptions))]

#Remove rows where Baltimore City column is empty
p1Crime_2021 = p1Crime_2021[p1Crime_2021['BaltCity'] != '']

"""###crime Indicator"""

#export
#crime Indicator
#Output - Part 1 Crime Rate per 1,000 Residents

#Create new df with only needed columns
crime = p1Crime_2021[['CSA2010', 'CSA2020']]

#Add crime column
crime['crimeCount'] = 1

#Get CSAs frequency
crime = crime.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2020 column
crime.reset_index(inplace=True)

#Add Baltimore City row
crime.loc[len(crime.index)] = ['Baltimore City', 'Baltimore City', crime['crimeCount'].sum()]

#read pop2020 data
pop2020 = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

#Append 2020pop
crime = crime.merge(pop2020, left_on=['CSA2010', 'CSA2020'], right_on=['CSA2010', 'CSA2020'], how='inner')

#Create indicator
crime['crime'] = (crime['crimeCount']/crime['tpop20'])*1000

"""###prop Indicator"""

#export
#prop Indicator
#Output - Property Crime Rate per 1,000 Residents

#Create new df with only needed descriptions
descriptions = ['AUTO THEFT', 'BURGLARY', 'LARCENY', 'LARCENY FROM AUTO']

prop = p1Crime_2021[(p1Crime_2021['Descriptio'].isin(descriptions))]

#Remove all unnecessary columns
prop = prop[['CSA2010', 'CSA2020']]

#Add property crime column
prop['propCount'] = 1

#Get CSAs frequency
prop = prop.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2020 column
prop.reset_index(inplace=True)

#Add Baltimore City row
prop.loc[len(prop.index)] = ['Baltimore City', 'Baltimore City', prop['propCount'].sum()]

#read pop2020 data
pop2020 = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

#Append 2020pop
prop = prop.merge(pop2020, left_on=['CSA2010', 'CSA2020'], right_on=['CSA2010', 'CSA2020'], how='inner')

#Create indicator
prop['prop'] = (prop['propCount']/prop['tpop20'])*1000

"""###vio Indicator"""

#export
#vio Indicator
#Output - Violent Crime Rate per 1,000 Residents

#Create new df with only needed descriptions
descriptions = ['AGG. ASSAULT', 'HOMICIDE', 'RAPE', 'ROBBERY - CARJACKING', 
                'ROBBERY - COMMERCIAL', 'ROBBERY - RESIDENCE', 'ROBBERY - STREET']
                
vio = p1Crime_2021[(p1Crime_2021['Descriptio'].isin(descriptions))]

#Remove all unnecessary columns
vio = vio[['CSA2010', 'CSA2020']]

#Add property crime column
vio['vioCount'] = 1

#Get CSAs frequency
vio = vio.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2020 column
vio.reset_index(inplace=True)

#Add Baltimore City row
vio.loc[len(vio.index)] = ['Baltimore City', 'Baltimore City', vio['vioCount'].sum()]

#read pop2020 data
pop2020 = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

#Append 2020pop
vio = vio.merge(pop2020, left_on=['CSA2010', 'CSA2020'], right_on=['CSA2010', 'CSA2020'], how='inner')

#Create indicator
vio['vio'] = (vio['vioCount']/vio['tpop20'])*1000

"""###gunhom Indicator"""

#export
#gunhom Indicator
#Output - Number of Gun-Related Homicides per 1,000 Residents

#Create df where desription = homicide & weapon = firearm
gunhom = p1Crime_2021[(p1Crime_2021['Descriptio'] == 'HOMICIDE') & (p1Crime_2021['Weapon'] == 'FIREARM')]

#Remove all unnecessary columns
gunhom = gunhom[['CSA2010', 'CSA2020']]

#Add property crime column
gunhom['gunhomCount'] = 1

#Get CSAs frequency
gunhom = gunhom.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2020 column
gunhom.reset_index(inplace=True)

#Add Baltimore City row
gunhom.loc[len(gunhom.index)] = ['Baltimore City', 'Baltimore City', gunhom['gunhomCount'].sum()]

#read pop2020 data
pop2020 = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

#Append 2020pop. Using right-merge since some CSAs have zero gunhomCount.
gunhom = gunhom.merge(pop2020, left_on=['CSA2010', 'CSA2020'], right_on=['CSA2010', 'CSA2020'], how='right')

#Create indicator
gunhom['gunhom'] = (gunhom['gunhomCount']/gunhom['tpop20'])*1000