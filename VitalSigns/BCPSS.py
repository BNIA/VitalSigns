# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/BCPSS_Schools.ipynb (unless otherwise specified).

__all__ = ['eattend', 'mattend', 'hsattend', 'aastud', 'wstud', 'hstud', 'abse', 'absmd', 'abshd', 'drop', 'compl',
           'sclsw', 'eenrol', 'menrol', 'hsenrol']

# Cell
def eattend(df, csa, yr):

  # Create the Numerator
  eattend = df.copy()
  eattend = eattend[ eattend['grade'].str.contains('^1$|^2$|^3$|^4$|^5$', regex=True)  & (eattend['daysattend'] > 1) ]

  eattend['count'] = 1
  eattend = eattend.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  eattend = csa.merge( eattend, left_on='CSA2010', right_on='CSA2010', how='outer' )
  eattend.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  # Baltimoire has records not in the
  eattend.at[55,'count']=eattend['count'].sum()
  # Perform the calculation
  eattend['66-eattend'+year] = eattend['count']

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/Eattend/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = 'eattend'+ str( int(year) - goback )
  if prevYear in compareYears.columns:
    eattend = eattend.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    eattend['change'] = eattend['66-eattend'+year] - eattend[ prevYear ]
    eattend['percentChange'] = eattend['change' ] / eattend[ prevYear ] * 100
    eattend['change'] = eattend['change'].apply(lambda x: "{:.2f}".format(x) )
  print( 'Records Matching Query: ', eattend.size / len(eattend.columns) )
  return eattend.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode', 'daysabsent', 'race_AIAN', 'race_asian', 'race_AA', 'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def mattend(df, csa, yr):

  # Create the Numerator
  mattend = df.copy()

  mattend = mattend[ mattend['grade'].str.contains('^6$|^7$|^8$', regex=True)  & (mattend['daysattend'] > 1) ]

  mattend['count'] = 1
  mattend = mattend.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  mattend = csa.merge( mattend, left_on='CSA2010', right_on='CSA2010', how='outer' )
  mattend.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  # Baltimoire has records not in the
  mattend.at[55,'count']=mattend['count'].sum()
  # Perform the calculation
  mattend['67-mattend'+year] = mattend['count']

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/Mattend/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = 'mattend'+ str( int(year) - goback )
  if prevYear in compareYears.columns:
    mattend = mattend.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    mattend['change'] = mattend['67-mattend'+year] - mattend[ prevYear ]
    mattend['percentChange'] = mattend['change' ] / mattend[ prevYear ] * 100
    mattend['change'] = mattend['change'].apply(lambda x: "{:.2f}".format(x) )
  print( 'Records Matching Query: ', mattend.size / len(mattend.columns) )
  return mattend.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode', 'daysabsent', 'race_AIAN', 'race_asian', 'race_AA', 'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def hsattend(df, csa, yr):

  # Create the Numerator
  hsattend = df.copy()

  hsattend = hsattend[ hsattend['grade'].str.contains('^9$|^10$|^11$|^12$', regex=True)  & (hsattend['daysattend'] > 1) ]

  hsattend['count'] = 1
  hsattend = hsattend.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  hsattend = csa.merge( hsattend, left_on='CSA2010', right_on='CSA2010', how='outer' )
  hsattend.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  # Baltimoire has records not in the
  hsattend.at[55,'count']=hsattend['count'].sum()
  # Perform the calculation
  hsattend['68-hsattend'+year] = hsattend['count']

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/Hsattend/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = 'hsattend'+ str( int(year) - goback )
  if prevYear in compareYears.columns:
    hsattend = hsattend.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    hsattend['change'] = hsattend['68-hsattend'+year] - hsattend[ prevYear ]
    hsattend['percentChange'] = hsattend['change' ] / hsattend[ prevYear ] * 100
    hsattend['change'] = hsattend['change'].apply(lambda x: "{:.2f}".format(x) )
  print( 'Records Matching Query: ', hsattend.size / len(hsattend.columns) )
  return hsattend.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def aastud(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom['grade'] = denom['grade'].apply(pd.to_numeric, errors='coerce')
  denom = denom[ (denom['daysattend'] > 1) & (denom['grade'] < 13) ]

  # Create the Numerator
  numer = denom[ (denom['race_AA'] > 0 ) & (denom['hispani_la'] == 'N') ]

  id = '70'
  shortname = 'aastud'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname+ str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def wstud(df, csa, yr):
  id = '71'
  shortname = 'wstud'
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom['grade'] = denom['grade'].apply(pd.to_numeric, errors='coerce')
  denom = denom[ (denom['daysattend'] > 1) & (denom['grade'] < 13) ]

  # Create the Numerator
  numer = denom[ (denom['race_white'] > 0 ) & (denom['hispani_la'] == 'N') ]

  id = '71'
  shortname = 'wstud'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def hstud(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom['grade'] = denom['grade'].apply(pd.to_numeric, errors='coerce')
  denom = denom[ (denom['daysattend'] > 1) & (denom['grade'] < 13) ]

  # Create the Numerator
  numer = denom[ (denom['hispani_la'] == 'Y') ]

  id = '72'
  shortname = 'hstud'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def abse(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom = denom[ denom['grade'].str.contains('^1$|^2$|^3$|^4$|^5$', regex=True)  & (denom['daysattend'] > 1) ]

  # Create the Numerator
  numer = denom[ (denom['daysabsent'] > 200 ) ]

  id = '73'
  shortname = 'abse'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  denom.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)

  numer.drop(columns=['tpop10', 'EnrollmentFlag', 'daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate']).to_csv(id+'-'+shortname+year+'_numer.csv', index=False)
  denom.drop(columns=['tpop10', 'EnrollmentFlag', 'daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate']).to_csv(id+'-'+shortname+year+'_denom.csv', index=False)

  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def absmd(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom = denom[ denom['grade'].str.contains('^6$|^7$|^8$', regex=True)  & (denom['daysattend'] > 1) ]

  # Create the Numerator
  numer = denom[ (denom['daysabsent'] > 200 ) ]

  id = '74'
  shortname = 'absmd'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  denom.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)

  numer.drop(columns=['tpop10', 'EnrollmentFlag', 'daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate']).to_csv(id+'-'+shortname+year+'_numer.csv', index=False)
  denom.drop(columns=['tpop10', 'EnrollmentFlag', 'daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate']).to_csv(id+'-'+shortname+year+'_denom.csv', index=False)

  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def abshd(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom = denom[ denom['grade'].str.contains('^9$|^10$|^11$|^12$', regex=True)  & (denom['daysattend'] > 1) ]

  # Create the Numerator
  numer = denom[ (denom['daysabsent'] > 200 ) ]

  id = '75'
  shortname = 'abshs'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  denom.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)

  numer.drop(columns=['tpop10', 'EnrollmentFlag', 'daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate']).to_csv(id+'-'+shortname+year+'_numer.csv', index=False)
  denom.drop(columns=['tpop10', 'EnrollmentFlag', 'daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate']).to_csv(id+'-'+shortname+year+'_denom.csv', index=False)

  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def drop(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom = denom[ denom['grade'].str.contains('^9$|^10$|^11$|^12$', regex=True)  & (denom['daysattend'] > 1) ]

  # Create the Numerator
  denom['wleavecode'] = denom['wleavecode'].astype(str)
  numer = denom[ ( denom['wleavecode'].str.contains('30|31|32|33|34|35|36|37|38|39|41|42|44|46|50|71|85', regex=True) ) ]

  id = '91'
  shortname = 'drop'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def compl(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  denom = df.copy()
  denom = denom[ denom['grade'].str.contains('^12$', regex=True)  & (denom['daysattend'] > 1) ]

  # Create the Numerator
  denom['wleavecode'] = denom['wleavecode'].astype(str)
  numer = denom[ ( denom['wleavecode'].str.contains('85|62|10|60', regex=True) ) ]

  id = '92'
  shortname = 'compl'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def sclsw(df, denomdf, csa, yr):
  df['count'] = 1
  denomdf['count'] = 1

  # Create the Denominator
  denom = denomdf.copy() #.sort_values('enterdate', ascending=False).drop_duplicates(['std_number'])
  denom = denom[ (denom['daysattend'] > 1) ]

  # Create the Numerator
  numer = df.copy()
  numer = numer[ (numer['daysattend'] > 1) ]

  id = '94'
  shortname = 'sclsw'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)
  denom = denom.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  denom = csa.merge( denom, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)
  numer['denomCount'] = denom['count']

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()
  numer.at[55,'denomCount']=numer['denomCount'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count'] / numer['denomCount'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def eenrol(df, csa, yr):
  df['count'] = 1

  # Create the Numerator
  numer = df.copy() # .sort_values('enterdate', ascending=False).drop_duplicates(['std_number'])
  numer = numer[ numer['grade'].str.contains('^1$|^2$|^3$|^4$|^5$', regex=True) ]

  id = '195'
  shortname = 'eenrol'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count']

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def menrol(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  numer = df.copy()
  numer = numer[ numer['grade'].str.contains('^6$|^7$|^8$', regex=True) ]

  id = '196'
  shortname = 'menrol'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)

  # Do after sortViaCsaMerge to get index right. False records would show underneath it but still get added to the sum.
  numer.at[55,'count']=numer['count'].sum()

  # Perform the calculation
  numer[id+'-'+shortname+year] = numer['count']

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[id+'-'+shortname+year] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'SchoolSwitcherFlag', 'wleavecode',
               'daysabsent', 'race_AIAN', 'race_asian', 'race_AA',
               'race_NHPI', 'race_white', 'std_number', 'enterdate'])

# Cell
def hsenrol(df, csa, yr):
  df['count'] = 1

  # Create the Denominator
  numer = df.copy() #.sort_values('enterdate', ascending=False).drop_duplicates(['std_number'])
  numer = numer[ numer['grade'].str.contains('^9$|^10$|^11$|^12$', regex=True) ]
  print( numer['grade'].unique() )

  id = '197'
  shortname = 'hsenrol'

  # Group by CSA
  numer = numer.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  numer = csa.merge( numer, left_on='CSA2010', right_on='CSA2010', how='outer' )
  numer.drop( columns=['geometry', 'Shape__Length','Shape__Area'], inplace=True)

  # Bcity is the sum of the community sums.
  # Incorrect Bcity Sum IFF Groupby keeps a 'False' row (index 56)
  numer.at[55,'count']=numer['count'].sum()

  # Perform the calculation
  fincol = id+'-'+shortname+year
  numer[fincol] = numer['count']

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/"+shortname.capitalize()+"/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  goback = 2 if year == '19' else 3
  prevYear = shortname + str( int(year) - goback )
  if prevYear in compareYears.columns:
    numer = numer.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    numer['change'] = numer[fincol] - numer[ prevYear ]
    numer['percentChange'] = numer['change' ] / numer[ prevYear ] * 100
    numer['change'] = numer['change'].apply(lambda x: "{:.2f}".format(x) )
    print( 'Records Matching Query: ', numer.size / len(numer.columns) )
  return numer.drop(columns=['daysattend', 'daysabsent', 'race_AIAN', 'race_asian', 'race_AA', 'race_NHPI', 'race_white', 'std_number', 'enterdate'])