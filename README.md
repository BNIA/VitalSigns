# Vital Signs
> Scripts to create our annual, publicly-available, community-focused datasets; for Baltimore City.


<img src="https://raw.githubusercontent.com/bniajfi/bniajfi/main/bnia_logo_new.png" height="160px" width="auto" style="max-width: autopx">

<h2 align="left"><img src="https://raw.githubusercontent.com/sidbelbase/sidbelbase/master/wave.gif" width="30px">Hi! We are <a href="https://bniajfi.org/">BNIA-JFI</a>.</h2>

This is [BNIA-JFI](http://www.bniajfi.org)'s principal repository for creating Vital Signs Indicators.

__Included__
- IPYNB/ Google Colab notebooks with indicator creation notes and scripts.
- Online documentation and PyPi libraries created from the notebooks.


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bnia/datalab/master?filepath=%2Fnotebooks%2Findex.ipynb)
[![Binder](https://pete88b.github.io/fastpages/assets/badges/colab.svg)](https://colab.research.google.com/github/bnia/datalab/blob/master/notebooks/index.ipynb)
[![Binder](https://pete88b.github.io/fastpages/assets/badges/github.svg)](https://github.com/bnia/datalab/tree/master/notebooks/index.ipynb)
[![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

[![NPM License](https://img.shields.io/npm/l/all-contributors.svg?style=flat)](https://github.com/bnia/VitalSigns/blob/master/LICENSE)
[![Active](http://img.shields.io/badge/Status-Active-green.svg)](https://bnia.github.io) 
[![Python Versions](https://img.shields.io/pypi/pyversions/VitalSigns.svg)](https://pypi.python.org/pypi/VitalSigns/)
[![GitHub last commit](https://img.shields.io/github/last-commit/bnia/VitalSigns.svg?style=flat)]() 
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/) 

[![GitHub stars](https://img.shields.io/github/stars/bnia/VitalSigns.svg?style=social&label=Star)](https://github.com/bnia/VitalSigns) 
[![GitHub watchers](https://img.shields.io/github/watchers/bnia/VitalSigns.svg?style=social&label=Watch)](https://github.com/bnia/VitalSigns) 
[![GitHub forks](https://img.shields.io/github/forks/bnia/VitalSigns.svg?style=social&label=Fork)](https://github.com/bnia/VitalSigns) 
[![GitHub followers](https://img.shields.io/github/followers/bnia.svg?style=social&label=Follow)](https://github.com/bnia/VitalSigns) 

[![Tweet](https://img.shields.io/twitter/url/https/github.com/bnia/VitalSigns.svg?style=social)](https://twitter.com/intent/tweet?text=Check%20out%20this%20%E2%9C%A8%20colab%20by%20@bniajfi%20https://github.com/bnia/VitalSigns%20%F0%9F%A4%97) 
[![Twitter Follow](https://img.shields.io/twitter/follow/bniajfi.svg?style=social)](https://twitter.com/bniajfi)

## ACS Scripts

These scripts will download and clean ACS data for Baltimore and then construct indicators from the data.

AcsDownload.ipynb
Mount notebook to google drive
Read in ACS Meta Data from XLSX and the crosswalk data from a csv
Add path to python script that performs download function
Enter a year and Run the download function for every record in XLSX sheet
For each dataset, remove columnID’s then save it as Raw
Then, Append Community Names using a crosswalk and save again in as Clean


AcsIndicators.ipynb
Mount notebook to google drive
Read in ACS Meta Data from XLSX
Prepare the Compare Historic Data
- For Each Indicator
- Grab its Meta Data
- If the Indicator is valid for the year, and uses ACS Data, and method exists
- retrieve the Python ACS indicator
- Put Baltimore City at the bottom of the list
- Write the results back into the XL dataframe
- Save the Dataset
- drop columns with any empty values
- Save the Data xlsx
Do comparison to historic year if exists. Write xlsx.


## Install

The code is on <a href="https://pypi.org/project/test-template/">PyPI</a> so you can install the scripts as a python library using the command:

`!pip install VitalSigns geopandas`

{% include important.html content='Contributers should follow the maintanance instructions and will not need to run this step. ' %}>
> Their modules will be retrieved from the VitalSigns-GDrive repo they have mounted into their Colabs Enviornment. 

Then...

### Examples

1) Import the installed module into your code:
``` 
from VitalSigns.acsDownload import retrieve_acs_data 
```
2) use it
```
retrieve_acs_data(state, county, tract, tableId, year, saveAcs)
```
Now you could do something like merge it to another dataset! 
```
from dataplay.merge import mergeDatasets
mergeDatasets(left_ds=False, right_ds=False, crosswalk_ds=False,  use_crosswalk = True, left_col=False, right_col=False, crosswalk_left_col = False, crosswalk_right_col = False, merge_how=False, interactive=True)
```

You can get information on the package by using the help command.

```
import VitalSigns
help(VitalSigns)
```

    Help on package VitalSigns:
    
    NAME
        VitalSigns
    
    PACKAGE CONTENTS
        BCPSS
        HUD
        _nbdev
        acsDownload
        bidbaltimore
        bpd
        citistat
        cityfinance
        closecrawl
        create
        dhr
        enoch
        fares
        fdic
        indicators
        infousa
        liquor
        mdprop
        rbintel
        tidyaddr
        treebaltimore
        utils
    
    VERSION
        0.0.5
    
    FILE
        /content/drive/My Drive/Software Development Documents/VitalSigns/VitalSigns/__init__.py
    
    


```
help(VitalSigns.acsDownload)
```

    Help on module VitalSigns.acsDownload in VitalSigns:
    
    NAME
        VitalSigns.acsDownload - # AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/90_ACS_Explore_and_Download.ipynb (unless otherwise specified).
    
    FUNCTIONS
        retrieve_acs_data(state, county, tract, tableId, year, save)
    
    DATA
        __all__ = ['retrieve_acs_data']
        __warningregistry__ = {'version': 352, ('Passing a negative integer is...
    
    FILE
        /content/drive/My Drive/Software Development Documents/VitalSigns/VitalSigns/acsDownload.py
    
    


```
help(VitalSigns.acsDownload.retrieve_acs_data)
```

    Help on function retrieve_acs_data in module VitalSigns.acsDownload:
    
    retrieve_acs_data(state, county, tract, tableId, year, save)
    


Here an example:

```
from VitalSigns.acsDownload import retrieve_acs_data
```

```
# Our download function will use Baltimore City's tract, county and state as internal paramters
# Change these values in the cell below using different geographic reference codes will change those parameters
tract = '*'
county = '510'
state = '24'

# Specify the download parameters the function will receieve here
tableId = 'B19001'
year = '17'
saveAcs = False
```

```
df = retrieve_acs_data(state, county, tract, tableId, year, saveAcs)
df.head()
```

    Number of Columns 17





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B19001_001E_Total</th>
      <th>B19001_002E_Total_Less_than_$10,000</th>
      <th>B19001_003E_Total_$10,000_to_$14,999</th>
      <th>B19001_004E_Total_$15,000_to_$19,999</th>
      <th>B19001_005E_Total_$20,000_to_$24,999</th>
      <th>B19001_006E_Total_$25,000_to_$29,999</th>
      <th>B19001_007E_Total_$30,000_to_$34,999</th>
      <th>B19001_008E_Total_$35,000_to_$39,999</th>
      <th>B19001_009E_Total_$40,000_to_$44,999</th>
      <th>B19001_010E_Total_$45,000_to_$49,999</th>
      <th>B19001_011E_Total_$50,000_to_$59,999</th>
      <th>B19001_012E_Total_$60,000_to_$74,999</th>
      <th>B19001_013E_Total_$75,000_to_$99,999</th>
      <th>B19001_014E_Total_$100,000_to_$124,999</th>
      <th>B19001_015E_Total_$125,000_to_$149,999</th>
      <th>B19001_016E_Total_$150,000_to_$199,999</th>
      <th>B19001_017E_Total_$200,000_or_more</th>
      <th>state</th>
      <th>county</th>
      <th>tract</th>
    </tr>
    <tr>
      <th>NAME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Census Tract 2710.02</th>
      <td>1510</td>
      <td>209</td>
      <td>73</td>
      <td>94</td>
      <td>97</td>
      <td>110</td>
      <td>119</td>
      <td>97</td>
      <td>65</td>
      <td>36</td>
      <td>149</td>
      <td>168</td>
      <td>106</td>
      <td>66</td>
      <td>44</td>
      <td>50</td>
      <td>27</td>
      <td>24</td>
      <td>510</td>
      <td>271002</td>
    </tr>
    <tr>
      <th>Census Tract 2604.02</th>
      <td>1134</td>
      <td>146</td>
      <td>29</td>
      <td>73</td>
      <td>80</td>
      <td>41</td>
      <td>91</td>
      <td>49</td>
      <td>75</td>
      <td>81</td>
      <td>170</td>
      <td>57</td>
      <td>162</td>
      <td>63</td>
      <td>11</td>
      <td>6</td>
      <td>0</td>
      <td>24</td>
      <td>510</td>
      <td>260402</td>
    </tr>
    <tr>
      <th>Census Tract 2712</th>
      <td>2276</td>
      <td>69</td>
      <td>43</td>
      <td>41</td>
      <td>22</td>
      <td>46</td>
      <td>67</td>
      <td>0</td>
      <td>30</td>
      <td>30</td>
      <td>80</td>
      <td>146</td>
      <td>321</td>
      <td>216</td>
      <td>139</td>
      <td>261</td>
      <td>765</td>
      <td>24</td>
      <td>510</td>
      <td>271200</td>
    </tr>
    <tr>
      <th>Census Tract 2804.04</th>
      <td>961</td>
      <td>111</td>
      <td>108</td>
      <td>61</td>
      <td>42</td>
      <td>56</td>
      <td>37</td>
      <td>73</td>
      <td>30</td>
      <td>31</td>
      <td>106</td>
      <td>119</td>
      <td>74</td>
      <td>23</td>
      <td>27</td>
      <td>24</td>
      <td>39</td>
      <td>24</td>
      <td>510</td>
      <td>280404</td>
    </tr>
    <tr>
      <th>Census Tract 901</th>
      <td>1669</td>
      <td>158</td>
      <td>124</td>
      <td>72</td>
      <td>48</td>
      <td>108</td>
      <td>68</td>
      <td>121</td>
      <td>137</td>
      <td>99</td>
      <td>109</td>
      <td>191</td>
      <td>160</td>
      <td>141</td>
      <td>28</td>
      <td>88</td>
      <td>17</td>
      <td>24</td>
      <td>510</td>
      <td>90100</td>
    </tr>
  </tbody>
</table>
</div>



From there, you can go on to do even greater things using our [dataplay](https://github.com/BNIA/dataplay) library. Like these visuals: 

<h2 align="left">Have Fun!</h2>
<img src="https://bniajfi.org/images/mermaid/vitalSignsCorrelations.png" width="500px" style="max-width: 500pxpx">
<img src="https://bniajfi.org/images/mermaid/vitalSignsGif.gif" width="500px" style="max-width: 500pxpx">

## MISC

This section is not definite but provides a good idea of how our scripts are made.

__Basic Indicator Creation Outline__
- ? Count = 1
- Create the num and denom
- filter num denom
- ? sum/ median = ungrouped.median
- group by csa
- ? bcity = median or sum
- perform the calculation
- compare years  

__Miscellaneous things I should have for every notebook__
- Module/filenames need to be fixed.
- RB Intel has the best prelim analysis script. The others are messed up a bit?
- include links indicator Esri and Bnia pages details on category, name, description, years
- Don’t drop columns at end, but keep selected at beginning.
- Merge on CSA for ordering
- Bcity Median gets calculated before aggregation. Appended after
- Add Years in header. Use denom and numerator as var names.
- Code to compare past years

## FOR CONTRIBUTERS

### Dev Instructions

From a local copy of the git repo:
0. __Clone__ the repo local onto GDrive 
  - Via Direct-DL&Drive-Upload or Colab/Terminal/Git
  - `git clone https://github.com/BNIA/VitalSigns.git`
1. __Update__ the the IPYNB 
  - From the GDrive VitalSigns folder via Colabs
2. __Build__ the new libraries from these NBs 
  - Using this *index.ipynb*
  - - Mount the Colabs Enviornment (and navigate to) the GDrive VitalSigns folder
  - - run `!nbdev_build_lib` to build .py modules.
3. __Test__ the Library/ Modules
  - Using the same runtime as step 2's *index.ipynb*.
  - - Do not install the module from PyPi (if published) and then...
  - - Import your module (
  from your VitalSigns/VitalSigns)
  - - If everything runs properly, go to step 5.
4. __Edit__ modules directly
  - Within the same runtime as step 2/3's *index.ipynb*...
  - - Locate the VitalSigns/VitalSigns using the colab file nav
  - - double-click the .py modules in the file nav to open them in an in-browser editor
  - Make changes and return to step 3 with the following caveat:
  - - Use the hot module reloading to ensure updates are auto-re-imported 
  - - `%load_ext autoreload %autoreload 2`
  - Then when finished, persist the changes from the .py modules back to the .ipynb docs 
  - - via `!nbdev_update_lib` and `!relimport2name`
5. **Create** Docs, **Push** to Github, and **Publish** to PyPI
  - All done via [nbdev](https://nbdev.fast.ai/) 
  - Find more notes I made on that here: [dataplay](https://github.com/bnia/dataplay) > nbdev [notes](https://bnia.github.io/datalabs/nbdev/index.html) 
  - `!nbdev_build_docs --force_all True --mk_readme True `
  - `!git commit -m ...`
  - `%%capture ! pip install twine`
  - `!nbdev_bump_version`
  - `! make pypi`

```
# https://nbdev.fast.ai/tutorial.html#Set-up-prerequisites
# settings.ini > requirements = fastcore>=1.0.5 torchvision<0.7
# https://nbdev.fast.ai/tutorial.html#View-docs-locally
# console_scripts = nbdev_build_lib=nbdev.cli:nbdev_build_lib
# https://nbdev.fast.ai/search
```

### Dev Scripts
