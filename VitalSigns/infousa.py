# -*- coding: utf-8 -*-
"""
This notebook uses the InfoUSA data to create a portion of BNIA's Vital Signs report

####**Indicators from this csv**

*   artbusXX - Arts and Culture
*   artempXX - Arts and Culture
*   cebusXX - Arts and Culture
*   ceempXX - Arts and Culture
*   numbusXX - Workforce and Economic Development
*   totempXX - Workforce and Economic Development
*   smlbusXX - Workforce and Economic Development
*   biz1_XX - Workforce and Economic Development
*   biz2_XX - Workforce and Economic Development
*   biz4_XX - Workforce and Economic Development
*   neiindXX - Workforce and Economic Development
*   neibusXX - Workforce and Economic Development
*   neiempXX - Workforce and Economic Development
"""

#export
#Import needed libraries
import pandas as pd
import numpy as np

#export
#Read data
original = pd.read_csv('InfoUSA_2021_CSACity.csv')

"""#Arts and Culture

Arts-related businesses are defined as belonging to industries that allow for the consumption and enjoyment of arts and culture.

The following industries are identified by their primary NAICS code: music, literary, and visual arts-related retail/supplies (451140, 451211, 451220); art dealers (453920, 453920); libraries (519120); motion picture and film (521310, 532230); art schools (611610); performing arts (711110, 711120, 711130, 711190); independent artists, writers, and performers (711510); museums (712110); historical sites (712120); and zoos, gardens and nature parks (712130, 712190).

The following industries are identified by their primary SIC codes: designers (152106); art publishers (274101), music, literary, and visual arts-related retail/supplies (393101, 519202, 573608, 573609, 593201, 594201, 594205, 594501, 594520, 594601, 599965, 769969); art galleries, dealers, and consultants (599969, 599988, 599989); photography (722121); calligraphers (733607); embroidery (738942); theatres (783201, 792207); theatrical support (792211, 792212); musical and live entertainment (792903, 792905, 792906, 792908, 792917, 792918, 792927); parks (799951); art and music instruction (804958, 829915, 829919); libraries (823111); museums (841201); arts organizations (841202); zoos (842201); writers (899903); visual artists (899907, 899912); art restoring (899908); and music arrangers and composers (899921).

####Artbus Indicator
"""

#export
#Artbus Indicator
#Output - Number of Businesses that are Arts-Related per 1,000 Residents

#Define NAICS ans SIC codes
naicCodes =  [451140, 451211, 451220, 453920, 519120, 521310, 532230, 611610, 711110, 711120, 
              711130, 711190, 711510, 712110, 712120, 712130, 712190]

sicCodes = [152106, 274101, 393101, 519202, 573608, 573609, 593201, 594201, 594205, 594501, 
            594520, 594601, 599965, 769969, 599969, 599988, 599989, 722121, 733607, 738942, 
            783201, 792207, 792211, 792212, 792903, 792905, 792906, 792908, 792917, 792918, 
            792927, 799951, 804958, 829915, 829919, 823111, 841201, 841202, 842201, 899903, 
            899907, 899912, 899908, 899921]

#Subset data to only include the codes above from the prim_naics & prim_sic columns
artbus = original[(original['prim_naics'].isin(naicCodes)) | (original['prim_sic'].isin(sicCodes))]

#Fix typos in CSA names.
artbus['CSA'] = artbus['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
artbus['CSA'] = artbus['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
artbus['CSA'] = artbus['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
artbus = pd.crosstab(index=artbus['CSA'], columns='artbusCount')

#make index the CSA2020 column
artbus.reset_index(inplace=True)

#Rename CSA column to CSA2020
artbus = artbus.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
artbus.loc[len(artbus.index)] = ['Baltimore City', artbus['artbusCount'].sum()]

#Append CSA population and CSA2020 names - This csv includes CSA2010/2020 names & 2020 pop.
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

artbus = pop2020_and_2020CSA.merge(artbus, left_on='CSA2020', right_on='CSA2020', how='outer')

#Create indicator
artbus['artbus'] = (artbus['artbusCount']/artbus['tpop20'])*1000

"""####Artemp Indicator """

#export
#Artemp Indicator
#Output - Total Employment in Arts-Related Businesses

#Define NAICS ans SIC codes
naicCodes =  [451140, 451211, 451220, 453920, 519120, 521310, 532230, 611610, 711110, 711120, 
              711130, 711190, 711510, 712110, 712120, 712130, 712190]

sicCodes = [152106, 274101, 393101, 519202, 573608, 573609, 593201, 594201, 594205, 594501, 
            594520, 594601, 599965, 769969, 599969, 599988, 599989, 722121, 733607, 738942, 
            783201, 792207, 792211, 792212, 792903, 792905, 792906, 792908, 792917, 792918, 
            792927, 799951, 804958, 829915, 829919, 823111, 841201, 841202, 842201, 899903, 
            899907, 899912, 899908, 899921]

#Subset data to only include the codes above from the prim_naics & prim_sic columns
artemp = original[ (original['prim_naics'].isin(naicCodes)) | (original['prim_sic'].isin(sicCodes))]

#Fix typos in CSA names. - These are the 2020 CSA names.
artemp['CSA'] = artemp['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
artemp['CSA'] = artemp['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
artemp['CSA'] = artemp['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
artemp = artemp[['CSA', 'empl_size']]
artemp = artemp.groupby('CSA').sum(numeric_only=True) 

#make index the CSA2020 column
artemp.reset_index(inplace=True)

#Rename CSA column to CSA2020, and empl_size to artemp
artemp = artemp.rename({'CSA': 'CSA2020', 'empl_size': 'artemp'}, axis=1)

#Add Baltimore City Row
artemp.loc[len(artemp.index)] = ['Baltimore City', artemp['artemp'].sum()]

#Append CSA population and CSA2010 names
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

artemp = pop2020_and_2020CSA.merge(artemp, left_on='CSA2020', right_on='CSA2020', how='outer')

"""####cebus Indicator

The creative economy is defined as industries that use and support artistic and cultural skillsets to attract and generate capital, knowledge, and information.

Arts-based businesses are included in the creative economy. In addition to the industries included in the rate of arts-based businesses indictor, the following industries are identified by their primary NAICS code: Textiles (313220); Commercial Printing (323111, 323113); Book Printers and Publishers (323117, 511130); Print Media (451212, 511110, 511120, 511199, 519110); Motion Picture & Video Production (512110); Music Publishers (512230); Sound Recording (512240); Radio (515112); Architecture (541310, 541320); Interior Design (541410); Graphic Design (541430); Advertising (541810, 541890); and Photography (541921, 541922).

In addition to the industries included in the rate of arts-based businesses indictor, the following industries are identified by their primary SIC code: Print Media (271101, 271102, 271198, 272101, 272102, 272104, 273101, 273198, 596302, 599401);Publishers (273298, 274104, 274105, 874205); Printers (275202, 275202, 275902, 275998); Bookbinders (278902); Radio (483201); Television (483301, 484101, 792205, 824911); Textiles (513122, 594904); Advertising (519917, 731101, 731115, 731305, 731999); Fashion Designers (569901, 594408); Photography (722101, 722113, 722120, 733501, 738401); Graphic Design (733603); Commercial Artists (733604); Website Design (737311); General Media (738301); Interior Design (738902); Restoration (764112); Landscape Design (781030); Motion Picture and Video Support (781205, 781211, 781901); Architecture (871202, 871207, 871209, 874892); and Business Writers (899902).
"""

#export
#cebus Indicator
#Output - Rate of Businesses in the Creative Economy per 1,000 Residents

#Define NAICS ans SIC codes
naicCodes = [323111, 323113, 451140, 451211, 451212, 453920, 511110, 511120, 511130, 511199, 
              512110, 519110, 519120, 541310, 541320, 541410, 541430, 541810, 541890, 541921, 
              541922, 611610, 711110, 711130, 711190, 711510, 712110, 712120, 712130, 712190, 
              313220, 323117, 511130, 512230, 512240, 515112 ]

sicCodes = [271101, 271102, 271198, 272101, 272102, 272104, 273101, 273198, 596302, 599401,
            273298, 274104, 274105, 874205, 275202, 275902, 275998, 278902, 483201, 
            483301, 484101, 792205, 824911, 513122, 594904, 519917, 731101, 731115, 731305, 
            731999, 569901, 594408, 722101, 722113, 722120, 733501, 738401, 733603, 733604, 
            737311, 738301, 738902, 764112, 781030, 781205, 781211, 781901, 871202, 871207, 
            871209, 874892, 899902]

#Subset data to only include the codes above from the prim_naics & prim_sic columns
cebus = original[ (original['prim_naics'].isin(naicCodes)) | (original['prim_sic'].isin(sicCodes))]

#Fix typos in CSA names.
cebus['CSA'] = cebus['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
cebus['CSA'] = cebus['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
cebus['CSA'] = cebus['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
cebus = pd.crosstab(index=cebus['CSA'], columns='cebusCount')

#make index the CSA2020 column
cebus.reset_index(inplace=True)

#Rename CSA column to CSA2020
cebus = cebus.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
cebus.loc[len(cebus.index)] = ['Baltimore City', cebus['cebusCount'].sum()]

#Append CSA population and CSA2020 names - This csv includes CSA2010/2020 names & 2020 pop.
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

cebus = pop2020_and_2020CSA.merge(cebus, left_on='CSA2020', right_on='CSA2020', how='outer')

#Create indicator
cebus['cebus'] = (cebus['cebusCount']/cebus['tpop20'])*1000

"""####ceemp Indicator """

#export
#ceemp Indicator
#Output - Number of Employees in the Creative Economy

#Define NAICS ans SIC codes
naicCodes = [323111, 323113, 451140, 451211, 451212, 453920, 511110, 511120, 511130, 511199, 
              512110, 519110, 519120, 541310, 541320, 541410, 541430, 541810, 541890, 541921, 
              541922, 611610, 711110, 711130, 711190, 711510, 712110, 712120, 712130, 712190, 
              313220, 323117, 511130, 512230, 512240, 515112 ]

sicCodes = [271101, 271102, 271198, 272101, 272102, 272104, 273101, 273198, 596302, 599401,
            273298, 274104, 274105, 874205, 275202, 275902, 275998, 278902, 483201, 
            483301, 484101, 792205, 824911, 513122, 594904, 519917, 731101, 731115, 731305, 
            731999, 569901, 594408, 722101, 722113, 722120, 733501, 738401, 733603, 733604, 
            737311, 738301, 738902, 764112, 781030, 781205, 781211, 781901, 871202, 871207, 
            871209, 874892, 899902, 451220, 521310, 532230, 711120]

#Subset data to only include the codes above from the prim_naics & prim_sic columns
ceemp = original[ (original['prim_naics'].isin(naicCodes)) | (original['prim_sic'].isin(sicCodes))]

#Fix typos in CSA names.
ceemp['CSA'] = ceemp['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
ceemp['CSA'] = ceemp['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
ceemp['CSA'] = ceemp['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
ceemp = ceemp[['CSA', 'empl_size']]
ceemp = ceemp.groupby('CSA').sum(numeric_only=True) 

#make index the CSA2020 column
ceemp.reset_index(inplace=True)

#Rename CSA column to CSA2020, and empl_size to ceemp
ceemp = ceemp.rename({'CSA': 'CSA2020', 'empl_size': 'ceemp'}, axis=1)

#Add Baltimore City Row
ceemp.loc[len(ceemp.index)] = ['Baltimore City', ceemp['ceemp'].sum()]

#Append CSA population and CSA2010 names
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

ceemp = pop2020_and_2020CSA.merge(ceemp, left_on='CSA2020', right_on='CSA2020', how='outer')

"""#Workforce and Economic Development

###numbus Indicator
"""

#export
#numbus Indicator
#Output - Total Number of Businesses

#Create new df with only the CSA column
numbus = original[['CSA']]
numbus['numbus'] = 1

#Fix typos in CSA names.
numbus['CSA'] = numbus['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
numbus['CSA'] = numbus['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
numbus['CSA'] = numbus['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
numbus = numbus.groupby('CSA').sum(numeric_only=True) 

#make index the CSA2020 column
numbus.reset_index(inplace=True)

#Rename CSA column to CSA2020, and empl_size to ceemp
numbus = numbus.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
numbus.loc[len(numbus.index)] = ['Baltimore City', numbus['numbus'].sum()]

#Append CSA population and CSA2010 names
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

numbus = pop2020_and_2020CSA.merge(numbus, left_on='CSA2020', right_on='CSA2020', how='outer')

"""###totemp Indicator"""

#export
#totemp Indicator
#Output - Total Number of Employees

#Create new df with CSA and empl_size columns 
totemp = original[['CSA', 'empl_size']]

#Fix typos in CSA names.
totemp['CSA'] = totemp['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
totemp['CSA'] = totemp['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
totemp['CSA'] = totemp['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
totemp = totemp[['CSA', 'empl_size']]
totemp = totemp.groupby('CSA').sum(numeric_only=True) 

#make index the CSA2020 column
totemp.reset_index(inplace=True)

#Rename CSA column to CSA2020, and empl_size to totemp
totemp = totemp.rename({'CSA': 'CSA2020', 'empl_size': 'totemp'}, axis=1)

#Add Baltimore City Row
totemp.loc[len(totemp.index)] = ['Baltimore City', totemp['totemp'].sum()]

#Append CSA population and CSA2010 names
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

totemp = pop2020_and_2020CSA.merge(totemp, left_on='CSA2020', right_on='CSA2020', how='outer')

"""###smlbus  Indicator"""

#export
#smlbus Indicator
#Output - Number of Businesses with Under 50 Employees

#Create new df with only business that have less than 50 employess
smlbus = original[original['empl_rng'].isin(['1 to 4', '5 to 9', '10 to 19', '20 to 49'])]

#Fix typos in CSA names.
smlbus['CSA'] = smlbus['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
smlbus['CSA'] = smlbus['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
smlbus['CSA'] = smlbus['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
smlbus = pd.crosstab(index=smlbus['CSA'], columns='smlbus')

#make index the CSA2020 column
smlbus.reset_index(inplace=True)

#Rename CSA column to CSA2020
smlbus = smlbus.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
smlbus.loc[len(smlbus.index)] = ['Baltimore City', smlbus['smlbus'].sum()]

#Append CSA population and CSA2020 names - This csv includes CSA2010, CSA2020 names & 2020 pop.
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

smlbus = pop2020_and_2020CSA.merge(smlbus, left_on='CSA2020', right_on='CSA2020', how='outer')

"""###biz_1  Indicator"""

#export
#biz_1 Indicator (for 2021)
#Output - Percent of Businesses that are 1 Year old or Less
#This indicator requires the numbus indicator as denominator

#Create new df with only business that started in 2020
biz1 = original[original['first_year'].isin([2020])]

#Fix typos in CSA names.
biz1['CSA'] = biz1['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
biz1['CSA'] = biz1['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
biz1['CSA'] = biz1['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
biz1 = pd.crosstab(index=biz1['CSA'], columns='biz1_count')

#make index the CSA2020 column
biz1.reset_index(inplace=True)

#Rename CSA column to CSA2020
biz1 = biz1.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
biz1.loc[len(biz1.index)] = ['Baltimore City', biz1['biz1_count'].sum()]

#Get numbus indicator data
numbus = pd.read_csv('numbus2021.csv')

#Append numbus data to biz1
biz1 = numbus.merge(biz1, left_on='CSA2020', right_on='CSA2020', how='outer')

#Create indicator
biz1['biz1'] = (biz1['biz1_count']/ biz1['numbus'])*100

"""###biz_2  Indicator"""

#export
#biz_2 Indicator (for 2021)
#Output - Percent of Businesses that are 2 Years old or Less
#This indicator requires the numbus indicator as denominator

#Create new df with only business that started in 2020
biz2 = original[original['first_year'].isin([2020, 2019])]

#Fix typos in CSA names.
biz2['CSA'] = biz2['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
biz2['CSA'] = biz2['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
biz2['CSA'] = biz2['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
biz2 = pd.crosstab(index=biz2['CSA'], columns='biz2_count')

#make index the CSA2020 column
biz2.reset_index(inplace=True)

#Rename CSA column to CSA2020
biz2 = biz2.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
biz2.loc[len(biz2.index)] = ['Baltimore City', biz2['biz2_count'].sum()]

#Get numbus indicator data
numbus = pd.read_csv('numbus2021.csv')

#Append numbus data to biz2
biz2 = numbus.merge(biz2, left_on='CSA2020', right_on='CSA2020', how='outer')

#Create indicator
biz2['biz2'] = (biz2['biz2_count']/ biz2['numbus'])*100

"""###biz_4  Indicator"""

#export
#biz_4 Indicator (for 2021)
#Output - Percent of Businesses that are 4 Years old or Less
#This indicator requires the numbus indicator as denominator

#Create new df with only business that started in 2020
biz4 = original[original['first_year'].isin([2020, 2019, 2018, 2017])]

#Fix typos in CSA names.
biz4['CSA'] = biz4['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
biz4['CSA'] = biz4['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
biz4['CSA'] = biz4['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
biz4 = pd.crosstab(index=biz4['CSA'], columns='biz4_count')

#make index the CSA2020 column
biz4.reset_index(inplace=True)

#Rename CSA column to CSA2020
biz4 = biz4.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
biz4.loc[len(biz4.index)] = ['Baltimore City', biz4['biz4_count'].sum()]

#Get numbus indicator data
numbus = pd.read_csv('numbus2021.csv')

#Append numbus data to biz4
biz4 = numbus.merge(biz4, left_on='CSA2020', right_on='CSA2020', how='outer')

#Create indicator
biz4['biz4'] = (biz4['biz4_count']/ biz4['numbus'])*100

"""###neiind  Indicator"""

#export
#neiind Indicator
#Output - Number of Businesses by Selected Neighborhood Industry (NAICS Sectors)

#Make copy of original df for neiind indicator
neiind = original.copy()

#Create new column where the 'prim_naics' column is trasformed to a string. 
#Then remove the last 6 characters from the string, and transform the column back to int
neiind['naics_extra_short'] = neiind.prim_naics.astype(str).str[:-6].astype(np.int64)

#Create df with only the short naic values needed
neiind = original[ (neiind['naics_extra_short'].isin( [44, 45, 52, 54, 62, 71, 72, 81]))]

#Fix typos in CSA names.
neiind['CSA'] = neiind['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
neiind['CSA'] = neiind['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
neiind['CSA'] = neiind['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
neiind = pd.crosstab(index=neiind['CSA'], columns='neiind')

#make index the CSA2020 column
neiind.reset_index(inplace=True)

#Rename CSA column to CSA2020
neiind = neiind.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
neiind.loc[len(neiind.index)] = ['Baltimore City', neiind['neiind'].sum()]

#Append CSA population and CSA2020 names - This csv includes CSA2010, CSA2020 names & 2020 pop.
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

neiind = pop2020_and_2020CSA.merge(neiind, left_on='CSA2020', right_on='CSA2020', how='outer')

"""###neibus Indicator"""

#export
#neibus Indicator
#Output - Neighborhood Businesses per 1,000 Residents (NAICS Sectors)

#Make copy of original df for neibus indicator
neibus = original.copy()

#Create new column where the 'prim_naics' column is trasformed to a string. 
#Then remove the last 6 characters from the string, and transform the column back to int
neibus['naics_extra_short'] = neibus.prim_naics.astype(str).str[:-6].astype(np.int64)

#Create df with only the short naic values needed
neibus = original[(neibus['naics_extra_short'].isin( [44, 45, 52, 54, 62, 71, 72, 81]))]

#Fix typos in CSA names.
neibus['CSA'] = neibus['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
neibus['CSA'] = neibus['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
neibus['CSA'] = neibus['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
neibus = pd.crosstab(index=neibus['CSA'], columns='neibus_count')

#make index the CSA2020 column
neibus.reset_index(inplace=True)

#Rename CSA column to CSA2020
neibus = neibus.rename({'CSA': 'CSA2020'}, axis=1)

#Add Baltimore City Row
neibus.loc[len(neibus.index)] = ['Baltimore City', neibus['neibus_count'].sum()]

#Append CSA population and CSA2020 names - This csv includes CSA2010, CSA2020 names & 2020 pop.
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

neibus = pop2020_and_2020CSA.merge(neibus, left_on='CSA2020', right_on='CSA2020', how='outer')

#Create indicator
neibus['neibus'] = (neibus['neibus_count'] / neibus['tpop20']) *1000

"""###neiemp Indicator"""

#export
#neiemp Indicator
#Output - Total number of Employees by Selected Neighborhood Industry (NAICS Sectors)

#Make copy of original df for neiemp indicator
neiemp = original.copy()

#Create new column where the 'prim_naics' column is trasformed to a string. 
#Then remove the last 6 characters from the string, and transform the column back to int
neiemp['naics_extra_short'] = neiemp.prim_naics.astype(str).str[:-6].astype(np.int64)

#Create df with only the short naic values needed
neiemp = original[(neiemp['naics_extra_short'].isin( [44, 45, 52, 54, 62, 71, 72, 81]))]

#Fix typos in CSA names.
neiemp['CSA'] = neiemp['CSA'].str.replace('Greektown/Bayview', 'Greentown/Bayview')
neiemp['CSA'] = neiemp['CSA'].str.replace('Hamiliton Hills', 'Hamilton Hills')
neiemp['CSA'] = neiemp['CSA'].str.replace('Oliver/Johnston Square', 'Oliver/Johnson Square')

#Frequency table for CSAs
neiemp = neiemp[['CSA', 'empl_size']]
neiemp = neiemp.groupby('CSA').sum(numeric_only=True) 

#make index the CSA2020 column
neiemp.reset_index(inplace=True)

#Rename CSA column to CSA2020, and empl_size to neiemp
neiemp = neiemp.rename({'CSA': 'CSA2020', 'empl_size': 'neiemp'}, axis=1)

#Add Baltimore City Row
neiemp.loc[len(neiemp.index)] = ['Baltimore City', neiemp['neiemp'].sum()]

#Append CSA population and CSA2010 names
pop2020_and_2020CSA = pd.read_csv('CSA2020_CSA2010_&_2020pop.csv')

neiemp = pop2020_and_2020CSA.merge(neiemp, left_on='CSA2020', right_on='CSA2020', how='outer')