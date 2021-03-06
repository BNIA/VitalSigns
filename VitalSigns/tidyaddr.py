# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/02_TidyAddr.ipynb (unless otherwise specified).

__all__ = ['uploadedFilename', 'runTidyAddr']

# Cell
uploadedFilename = "outputfile.csv"
# d = list( uploaded.keys() )[0]

# Cell
# Input: A CSV with a single column titled 'address' (may require pre-processing to get it like this)
# Output: A CSV with a single column containing text that can be split into 5 columns in xl.
# - Needs to be re-merged with any other columns removed before tidy addring.
import os
def runTidyAddr( filename ):
  print( filename )
  print(' ~~~~~~~~~~~ Getting TIDYADDR ~~~~~~~~~~~ ')
  os.system( "! rm tidyaddr-js -r")
  os.system("! git clone https://github.com/BNIA/tidyaddr-js.git")
  print(' ~~~~~~~~~~~ Installing TIDYADDR ~~~~~~~~~~~')
  # os.system("! echo $(ls)")
  os.system("! cp *.csv tidyaddr-js/")
  os.system("! npm install tidyaddr-js")
  print(' ~~~~~~~~~~~ Running TIDYADDR ~~~~~~~~~~~')
  # os.system("! echo TIDYADDR_DIRECTORY && cd tidyaddr-js && echo $(ls)")
  txt = "cd tidyaddr-js && node tidyaddr.js clean-csv " + filename + " " + filename.replace(".", "_tidyaddred.")
  print(txt)
  os.system(txt)