# Vital Signs
> Scripts to create our annual, publicly-available, community-focused datasets; for Baltimore City.


<img src="https://raw.githubusercontent.com/bniajfi/bniajfi/main/bnia_logo_new.png" height="160px" width="auto" style="max-width: autopx">

<h2 align="left"><img src="https://raw.githubusercontent.com/sidbelbase/sidbelbase/master/wave.gif" width="30px">Hi! We are <a href="https://bniajfi.org/">BNIA-JFI</a>.</h2>

This package was made to create Vital Signs data.

Check our [Github](https://github.com/bniajfi) page for more information and tools.

__About__
- Functions built and used by BNIA for annual Vital Signs data release.
- Made to be shared via IPYNB/ Google Colab notebooks. 
- Data may be private and is sometimes public.
- Online [documentation](https://bniajfi.org/VitalSigns/)  and [PyPi](https://pypi.org/project/VitalSigns/) libraries created from the notebooks.

__Included__ (but not limited to)
- CloseCrawl - Pull MD Courts data.
- TidyAddr - Expertly clean addresses in Baltimore (and beyond). Works Seamlessly with Closecrawl. 
- Download ACS - ACS Tutorial. Gives a function and also teaches you how to pull any data for any geography using this API (can aggregate tracts on along a crosswalk).
- Create ACS Statistics - Create pre-made statistics from ACS data. Builds off the ACS Downloader
- VS Indicators - Create other (non ACS) Vital Signs statistics using these pre-made functions.
- convertvssheetforwpupload - For internal developer use when publishing at BNIA

[VitalSigns](https://bniajfi.org/VitalSigns/) uses functions found in our [Dataplay](https://bniajfi.org/dataplay/)  Module and vice-versa.

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

The code is on <a href="https://pypi.org/project/test-template/">PyPI</a> so you can install the scripts as a python library using the command:

`!pip install VitalSigns dataplay geopandas`

{% include important.html content='Contributers should follow the maintanance instructions and will not need to run this line. ' %}

Then...

### Import Modules

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

### Getting Help

You can get information on the package by using the help command.

Here we look at the package's modules:

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
        0.0.10
    
    FILE
        /content/drive/My Drive/Software Development Documents/VitalSigns/VitalSigns/__init__.py
    
    


Lets take a look at what functions the geoms module provides:

```
import VitalSigns.acsDownload
help(VitalSigns.acsDownload)
```

    Help on module VitalSigns.acsDownload in VitalSigns:
    
    NAME
        VitalSigns.acsDownload - # AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/03_ACS_Download.ipynb (unless otherwise specified).
    
    FUNCTIONS
        retrieve_acs_data(state, county, tract, tableId, year)
    
    DATA
        __all__ = ['retrieve_acs_data']
    
    FILE
        /content/drive/My Drive/Software Development Documents/VitalSigns/VitalSigns/acsDownload.py
    
    


And here we can look at an individual function and what it expects:

```
import VitalSigns.acsDownload
help(VitalSigns.acsDownload.retrieve_acs_data)
```

    Help on function retrieve_acs_data in module VitalSigns.acsDownload:
    
    retrieve_acs_data(state, county, tract, tableId, year)
    


## Examples

So heres an example:


Import your modules

```
from VitalSigns.acsDownload import retrieve_acs_data
```

Read in some data

Define our download parameters.

More information on these parameters can be found in the tutorials!

```
# Our download function will use Baltimore City's tract, county and state as internal paramters
# Change these values in the cell below using different geographic reference codes will change those parameters
tract = '*'
county = '510'
state = '24'

# Specify the download parameters the function will receieve here
tableId = 'B19001'
year = '17'
```

And download the Baltimore City ACS data using the imported VitalSigns library.

```
df = retrieve_acs_data(state, county, tract, tableId, year)
df.head(1)
```




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
      <th>...</th>
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Census Tract 2710.02</th>
      <td>1510</td>
      <td>209</td>
      <td>73</td>
      <td>...</td>
      <td>24</td>
      <td>510</td>
      <td>271002</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 20 columns</p>
</div>



From there, you can go on to do even greater things using our [dataplay](https://github.com/BNIA/dataplay) library. Like these visuals: 

```
ls
```

    checkpoint.json     [0m[01;34mdocs[0m/     MANIFEST.in  settings.ini
    CONTRIBUTING.md     LICENSE   [01;34mnotebooks[0m/   setup.py
    docker-compose.yml  Makefile  README.md    [01;34mVitalSigns[0m/


```
from VitalSigns.create import createAcsIndicator, mhhi 
mergeUrl = 'https://raw.githubusercontent.com/bniajfi/bniajfi/main/CSA-to-Tract-2010.csv'
merge_left_col = 'tract'
merge_right_col= 'TRACTCE10' 
merge_how = 'outer'

groupBy = 'CSA2010'

method = mhhi
aggMethod = 'sum'
columnsToInclude = []


createAcsIndicator(state, county, tract, year, tableId,
                    mergeUrl, merge_left_col, merge_right_col, merge_how, groupBy,
                    aggMethod, method, columnsToInclude, finalFileName=False).head(1)
```

    Table: B19001, Year: 17 imported.
    Index(['TRACTCE10',
           'GEOID10',
           'CSA2010'],
          dtype='object')
    Merge file imported
    Both are now merged.
    Aggregating...
    Aggregated
    Creating Indicator
    Indicator Created





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
      <th>B19001_002E_Total_Less_than_$10,000</th>
      <th>B19001_003E_Total_$10,000_to_$14,999</th>
      <th>B19001_004E_Total_$15,000_to_$19,999</th>
      <th>...</th>
      <th>midpoint_index_range</th>
      <th>midpoint_index_minus_one_cumulative_sum</th>
      <th>final</th>
    </tr>
    <tr>
      <th>CSA2010</th>
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
      <th>Allendale/Irvington/S. Hilton</th>
      <td>739</td>
      <td>1246</td>
      <td>1656</td>
      <td>...</td>
      <td>4999</td>
      <td>2667</td>
      <td>39495.628472</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 23 columns</p>
</div>



```
from VitalSigns.closecrawl import close_crawl
```

```
help(close_crawl)
```

    Help on function close_crawl in module VitalSigns.closecrawl:
    
    close_crawl(case_type, case_year, output, cases='', lower_bound=0, upper_bound=0, debug=False, scrape=True, mine=True, clean=True)
        Main function for Close Crawl.
        
        Args:
            case_type (`str`): type of foreclosure case, options are 'O' and 'C'
            case_year (`str`): year of foreclosure cases
            output (`str`): path of the output CSV file, along with the valid
                extension (.csv)
            lower_bound (`int`, optional): lower bound of range of cases
            upper_bound (`int`, optional): upper bound of range of cases
            debug (`bool`, optional): option for switching between debug mode.
                Default -> True
        
        Returns:
            None
    


```
args = {'type': 'C', 'year': '2020', 'output': 'outputfile.csv', 'file': '', 'lower': '1000', 'upper': '1030', 'debug': '0', 'scrape': True, 'mine': True, 'clean': True}
close_crawl(
    case_type=args["type"], case_year=args["year"], output=args["output"],
    cases=args["file"], lower_bound=args["lower"],
    upper_bound=args["upper"], debug=args["debug"],
    scrape=args["scrape"], mine=args["mine"],
    clean=args["clean"]
)
```

```
from VitalSigns import tidyaddr
```

```
help(tidyaddr)
```

    Help on module VitalSigns.tidyaddr in VitalSigns:
    
    NAME
        VitalSigns.tidyaddr - Create a module object.
    
    DESCRIPTION
        The name must be a string; the optional doc argument can have any type.
    
    FUNCTIONS
        runTidyAddr(filename)
    
    DATA
        __all__ = ['uploadedFilename', 'runTidyAddr']
        uploadedFilename = 'outputfile.csv'
    
    FILE
        /content/drive/My Drive/Software Development Documents/VitalSigns/VitalSigns/tidyaddr.py
    
    


```
output = 'outputfile.csv'
tidyaddr.runTidyAddr( output )
```

    outputfile.csv
     ~~~~~~~~~~~ Getting TIDYADDR ~~~~~~~~~~~ 
     ~~~~~~~~~~~ Installing TIDYADDR ~~~~~~~~~~~
     ~~~~~~~~~~~ Running TIDYADDR ~~~~~~~~~~~
    cd tidyaddr-js && node tidyaddr.js clean-csv outputfile.csv outputfile_tidyaddred.csv


```
! cd tidyaddr-js && ls
```

    dev	 LICENSE	 outputfile_tidyaddred.csv  README.md	 todo.todo
    init.js  outputfile.csv  package.json		    tidyaddr.js


<h2 align="left">Have Fun!</h2>
<img src="https://bniajfi.org/images/mermaid/vitalSignsCorrelations.png" width="500px" style="max-width: 500pxpx">
<img src="https://bniajfi.org/images/mermaid/vitalSignsGif.gif" width="500px" style="max-width: 500pxpx">

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

```
! nbdev_build_lib
```

```
ls
```

    checkpoint.json     [0m[01;34mdocs[0m/         Makefile     package-lock.json  setup.py
    CONTRIBUTING.md     [01;34mindex_files[0m/  MANIFEST.in  README.md          [01;34mVitalSigns[0m/
    docker-compose.yml  LICENSE       [01;34mnotebooks[0m/   settings.ini


```
# !git mv index.md README.md -f
```

    fatal: bad source, source=index.md, destination=README.md


```
!nbdev_update_lib
```

```
# ! git remote remove origin
```

```
# ! git remote remove origin
```

```
# !git remote add origin https://github.com/BNIA/VitalSigns.git
```

```
!git remote -v
```

    origin	https://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@github.com/BNIA/VitalSigns.git (fetch)
    origin	https://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@github.com/BNIA/VitalSigns.git (push)


```
# step 3
project = 'VitalSigns'
token = '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' 
username = 'BNIA'
print(f'https://{token}@github.com/{username}/{project}.git')
! git remote remove origin 
! git remote add origin 'https://{token}@github.com/{username}/{project}.git'
#! git push -u origin main 
!git push 'https://{token}@github.com/{username}/{project}.git' 
```

    https://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@github.com/BNIA/VitalSigns.git
    Counting objects: 17, done.
    Delta compression using up to 2 threads.
    Compressing objects: 100% (17/17), done.
    Writing objects: 100% (17/17), 6.24 KiB | 1.04 MiB/s, done.
    Total 17 (delta 13), reused 0 (delta 0)
    remote: Resolving deltas: 100% (13/13), completed with 3 local objects.[K
    To https://github.com/BNIA/VitalSigns.git
       9b8fcc9..bdcbbdb  main -> main


```
! git push -u ORIGIN main #-f
```

    fatal: 'ORIGIN' does not appear to be a git repository
    fatal: Could not read from remote repository.
    
    Please make sure you have the correct access rights
    and the repository exists.

