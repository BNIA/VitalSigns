# Vital Signs
> Scripts to create our annual, publicly-available, community-focused datasets; for Baltimore City.


<img src="https://raw.githubusercontent.com/bniajfi/bniajfi/main/bnia_logo_new.png" height="160px" width="auto" style="max-width: autopx">

<h2>Hi! We are <a href="https://bniajfi.org/">BNIA-JFI</a>.</h2>

This package was made to create Vital Signs data.

Check our [Github](https://github.com/bniajfi) page for more information and tools.

__About__
- Functions built and used by BNIA for annual Vital Signs data release.
- Made to be shared via IPYNB/ Google Colab notebooks. 
- Data may be private and is sometimes public.
- [PyPi](https://pypi.org/project/VitalSigns2022TEST/) libraries created from the notebooks.

__Included__ (but not limited to)
- CloseCrawl - Pull MD Courts data.
- TidyAddr - Expertly clean addresses in Baltimore (and beyond). Works Seamlessly with Closecrawl. 
- Download ACS - ACS Tutorial. Gives a function and also teaches you how to pull any data for any geography using this API (can aggregate tracts on along a crosswalk).
- Create ACS Statistics - Create pre-made statistics from ACS data. Builds off the ACS Downloader
- VS Indicators - Create other (non ACS) Vital Signs statistics using these pre-made functions.
- convertvssheetforwpupload - For internal developer use when publishing at BNIA

VitalSigns uses functions found in our Dataplay Module and vice-versa.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bnia/VitalSigns/main?filepath=%2Fnotebooks%2Findex.ipynb)
[![Binder](https://pete88b.github.io/fastpages/assets/badges/colab.svg)](https://colab.research.google.com/github/bnia/VitalSigns/blob/main/notebooks/index.ipynb)
[![Binder](https://pete88b.github.io/fastpages/assets/badges/github.svg)](https://github.com/bnia/VitalSigns/tree/main/notebooks/index.ipynb)
[![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

[![NPM License](https://img.shields.io/npm/l/all-contributors.svg?style=flat)](https://github.com/bnia/VitalSigns/blob/main/LICENSE)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://bnia.github.io) 
[![Python Versions](https://img.shields.io/pypi/pyversions/VitalSigns.svg)](https://pypi.python.org/pypi/VitalSigns/)
[![GitHub last commit](https://img.shields.io/github/last-commit/bnia/VitalSigns.svg?style=flat)]()  

[![GitHub stars](https://img.shields.io/github/stars/bnia/VitalSigns.svg?style=social&label=Star)](https://github.com/bnia/VitalSigns) 
[![GitHub watchers](https://img.shields.io/github/watchers/bnia/VitalSigns.svg?style=social&label=Watch)](https://github.com/bnia/VitalSigns) 
[![GitHub forks](https://img.shields.io/github/forks/bnia/VitalSigns.svg?style=social&label=Fork)](https://github.com/bnia/VitalSigns) 
[![GitHub followers](https://img.shields.io/github/followers/bnia.svg?style=social&label=Follow)](https://github.com/bnia/VitalSigns) 

[![Tweet](https://img.shields.io/twitter/url/https/github.com/bnia/VitalSigns.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20this%20%E2%9C%A8%20colab%20by%20@bniajfi%20https://github.com/bnia/VitalSigns%20%F0%9F%A4%97) 
[![Twitter Follow](https://img.shields.io/twitter/follow/bniajfi.svg?style=social)](https://twitter.com/bniajfi)

## Usage Instructions

### Install the Package

The code is on <a href="https://pypi.org/project/VitalSigns2022TEST/">PyPI</a> so you can install the scripts as a python library using the command:
```
!pip install VitalSigns2022TEST dataplay geopandas
```

### Import Modules

1) Import the installed module into your code:
``` 
from VitalSigns.acsDownload import retrieve_acs_data
```

2) use it
```
retrieve_acs_data(state, county, tract, tableId, year, saveAcs)
```

# Getting Help

You can get information on the package by using the help command.

Here we look at the package's modules:
```
import VitalSigns
help(VitalSigns)
```

Lets take a look at what functions the geoms module provides:
```
import VitalSigns.acsDownload
help(VitalSigns.acsDownload)
```

And here we can look at an individual function and what it expects:
```
import VitalSigns.acsDownload
help(VitalSigns.acsDownload.retrieve_acs_data)
```

## Example #1 
Follow this process for all VitalSigns scripts, with the exception of the ractiv indicator (shown in Example #2)

### ACS Download

Install the package.
```
!pip install VitalSigns2022TEST dataplay geopandas
```

Import your modules.
```
from VitalSigns.acsDownload import retrieve_acs_data
```

Read in some data.
```
#Define our download parameters (tract, county, state, tableId, and state)
#Our download function will use Baltimore City's tract, county and state as internal parameters
#Changing these values using different geographic reference codes will change those parameters

tract = '*'
county = '510'
state = '24'

tableId = 'B01001'
year = '19'
```

And download the Baltimore City ACS data using the imported VitalSigns library.
```
df = retrieve_acs_data(state, county, tract, tableId, year)
df.head(2)
```

Save the ACS data (Use this method ONLY if you are working in Google Colab. Otherwise, you can save the data however you prefer)
```
from google.colab import files
df.to_csv('YourFileName.csv') 
files.download('YourFileName.csv')
```

### ACS Calculations and Indicators

Now that we have the ACS data, we can use any of the scripts in the VitalSigns library to create the Baltimore City indicators.

These scripts will download and clean ACS data for Baltimore and then construct indicators from the data.

A list of all the tables used and their respective indicator scripts can be found here -ADD LINK HERE--

First, import the script(s)  you would like to use for the ACS data chosen.
```
#Script to create the Percent of Population Under 5 Years old indicator.
from VitalSigns.create import createAcsIndicator, age5 
```

Once the script has been imported, we can now create the Baltimore City indicators.
```
mergeUrl = 'https://raw.githubusercontent.com/gparedes10/2022VitalSigns/main/CSA_2010_and_2020.csv'
merge_left_col = 'tract'
merge_right_col= 'TRACTCE' 
merge_how = 'outer'

groupBy = 'CSA2010'     #For the 2020 CSAs use 'CSA2020', for 2010 CSAs use 'CSA2010'

method = age5
aggMethod = 'sum'
columnsToInclude = []


MyIndicator = createAcsIndicator(state, county, tract, year, tableId,
                    mergeUrl, merge_left_col, merge_right_col, merge_how, groupBy,
                    aggMethod, method, columnsToInclude, finalFileName=False)

MyIndicator.head(2)
```

Now we can save the Baltimore City indicators (Use this method ONLY if you are working in Google Colab. Otherwise, you can save the data however you prefer)
```
from google.colab import files
MyIndicator.to_csv('YourIndicatorFileName.csv') 
files.download('YourIndicatorFileName.csv')
```

## Example #2 (racdiv indicator)
The Racial Diversity Index (racdiv) indicator is the only script in our library that relies on two ACS tables. 
Due to this difference, this is the only script that will ask the user for an input while the script is running (the user needs to re-enter the year)

Lets follow the same process we did during example #1
### ACS Download

Install the package.
```
!pip install VitalSigns2022TEST dataplay geopandas
```

Import your modules.
```
from VitalSigns.acsDownload import retrieve_acs_data
```

Read in some data.
```
tract = '*'
county = '510'
state = '24'

tableId = 'B02001'
year = '19' #This is the number that the user NEEDS to re-enter once the script asks for an input
```

And download the Baltimore City ACS data using the imported VitalSigns library.
```
df = retrieve_acs_data(state, county, tract, tableId, year)
df.head(2)
```

Save the ACS data (Use this method ONLY if you are working in Google Colab. Otherwise, you can save the data however you prefer)
```
from google.colab import files
df.to_csv('YourFileName.csv') 
files.download('YourFileName.csv')
```
### ACS Calculations and Indicators
To see the table IDs, Names, and their respective indicators again, click here --ADD LINK HERE--

Import the racdiv script 
```
#Script to create the Racial Diversity Index indicator.
from VitalSigns.create import createAcsIndicator, racdiv 
```

Once the script has been imported, we can now create the Baltimore City indicators.
```
mergeUrl = 'https://raw.githubusercontent.com/gparedes10/2022VitalSigns/main/CSA_2010_and_2020.csv'
merge_left_col = 'tract'
merge_right_col= 'TRACTCE' 
merge_how = 'outer'

groupBy = 'CSA2010'     #For the 2020 CSAs use 'CSA2020', for 2010 CSAs use 'CSA2010'

method = racdiv
aggMethod = 'sum'
columnsToInclude = []


MyIndicator = createAcsIndicator(state, county, tract, year, tableId,
                    mergeUrl, merge_left_col, merge_right_col, merge_how, groupBy,
                    aggMethod, method, columnsToInclude, finalFileName=False)

MyIndicator.head(2)
```

The cell below shows the output while the racdiv script is being run. As you can see on the last line, the script asks the user to re-enter their chosen year. After re-entering the year, the script will finish running, and the racdiv indicator table will be completed.
```
Table: B02001, Year: 19 imported.
Index(['TRACTCE', 'GEOID10', 'CSA2010', 'GEOID', 'CSA2020'], dtype='object')
Merge file imported
Both are now merged.
Aggregating...
Aggregated
Creating Indicator
Please enter your chosen year again (i.e., '17', '20'): 
```

Now we can save the Baltimore City indicators (Use this method ONLY if you are working in Google Colab. Otherwise, you can save the data however you prefer)
```
from google.colab import files
MyIndicator.to_csv('YourIndicatorFileName.csv') 
files.download('YourIndicatorFileName.csv')
```