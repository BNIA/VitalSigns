# -*- coding: utf-8 -*-
"""
This notebook uses the 311 Service Requests data to create a portion of BNIA's Vital Signs report

####**Indicators from this csv**

*   dirtyst
*   clogged
*   lights

**Note:** Due to the size of the original file for the 311 Service Requests data, the dataset was broken down into the three subsets that are needed for the indicators. After creating the three subsets, each subset was geocoded to include the CSA2010, CSA2020, and BaltCity columns. 
The subsets were created based on the SRType column, and the filters used for each indicator are as follows:

*   **dirtyst:** SRType = SW-Dirty Alley, SW-Dirty Street, SW-Dirty Alley Proactive, SW-Dirty Street Proactive
*   **clogged:** SRType = Everything that begins with 'WW-St' (used grep function)
*   **lights:** SRType = BGE-StLight(s) Out, BGE-StLight(s) Out Rear, TRM-Street Light Out
*   BaltCity != ' ' was used for all three subsets in addition to the above
"""

#export
#Import needed libraries
import pandas as pd

"""###dirtyst Indicator

"""

#export
#dirtyst Indicator
#Output - Rate of Dirty Streets and Alleys Reports per 1,000 Residents

#Read data
dirtyst = pd.read_csv('Clean_DirtyStreets_and_Alleys_2021.csv', encoding="cp850") #utf8 encoding kept giving an error.

#Only keep needed columns
dirtyst = dirtyst[['CSA2010', 'CSA2020']]

#Add dirtyst column
dirtyst['dirtystCount'] = 1

#Get CSAs frequency
dirtyst = dirtyst.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2020 column
dirtyst.reset_index(inplace=True)

#Add Baltimore City row
dirtyst.loc[len(dirtyst.index)] = ['Baltimore City', 'Baltimore City', dirtyst['dirtystCount'].sum()]

#read pop2020 data
pop2020 = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

#Append 2020pop
dirtyst = dirtyst.merge(pop2020, left_on=['CSA2010', 'CSA2020'], right_on=['CSA2010', 'CSA2020'], how='inner')

#Create indicator
dirtyst['dirtyst'] = (dirtyst['dirtystCount']/dirtyst['tpop20'])*1000

"""###clogged Indicator

"""

#export
#clogged Indicator
#Output - Rate of Clogged Storm Drain Reports per 1,000 Residents

#Read data
clogged = pd.read_csv('Clean_Clogged_Storm_Drains_2021.csv') #utf8 encoding kept giving an error.

#Only keep needed columns
clogged = clogged[['CSA2010', 'CSA2020']]

#Add clogged column
clogged['cloggedCount'] = 1

#Get CSAs frequency
clogged = clogged.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2020 column
clogged.reset_index(inplace=True)

#Add Baltimore City row
clogged.loc[len(clogged.index)] = ['Baltimore City', 'Baltimore City', clogged['cloggedCount'].sum()]

#read pop2020 data
pop2020 = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

#Append 2020pop
clogged = clogged.merge(pop2020, left_on=['CSA2010', 'CSA2020'], right_on=['CSA2010', 'CSA2020'], how='inner')

#Create indicator
clogged['clogged'] = (clogged['cloggedCount']/clogged['tpop20'])*1000

"""###lights Indicator

"""

#export
#lights Indicator
#Output - #Rate of Street Light Outages per 1,000 Residents

#Read data
lights = pd.read_csv('Clean_LightsOut_2021.csv') #utf8 encoding kept giving an error.

#Only keep needed columns
lights = lights[['CSA2010', 'CSA2020']]

#Add lights column
lights['lightsCount'] = 1

#Get CSAs frequency
lights = lights.groupby(['CSA2010', 'CSA2020']).sum(numeric_only=True) 

#make index the CSA2020 column
lights.reset_index(inplace=True)

#Add Baltimore City row
lights.loc[len(lights.index)] = ['Baltimore City', 'Baltimore City', lights['lightsCount'].sum()]

#read pop2020 data
pop2020 = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

#Append 2020pop
lights = lights.merge(pop2020, left_on=['CSA2010', 'CSA2020'], right_on=['CSA2010', 'CSA2020'], how='inner')

#Create indicator
lights['lights'] = (lights['lightsCount']/lights['tpop20'])*1000