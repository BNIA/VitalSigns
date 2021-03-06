# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/DHR_SNAP_TANF_Create.ipynb (unless otherwise specified).

__all__ = ['tanf', 'snap']

# Cell
def tanf(df, csa, yr):

  # Create the Numerator
  tanf = df.copy()
  tanf['count'] = 1
  tanf = tanf.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  tanf = csa.merge( tanf, left_on='CSA2010', right_on='CSA2010', how='outer' )
  # Baltimoire may have records not in the CSA (not actually the case right now but..)
  tanf.at[55,'count']=tanf['count'].sum()
  # Perform the calculation
  tanf['106-tanf'+year] = tanf['count'] / tanf['FamHH_2010'] * 100

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/Tanf/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  prevYear = 'tanf'+ str( int(year) - 1 )
  if prevYear in compareYears.columns:
    tanf = tanf.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    tanf['change'] = tanf['106-tanf'+year] - tanf[ prevYear ]
    tanf['percentChange'] = tanf['change' ] / tanf[ prevYear ] * 100
    tanf['change'] = tanf['change'].apply(lambda x: "{:.2f}".format(x) )
  print( 'Records Matching Query: ', tanf.size / len(tanf.columns) )
  return tanf

# Cell
def snap(df, csa, yr):

  # Create the Numerator
  snap = df.copy()
  snap['count'] = 1
  snap = snap.groupby('CSA2010').sum(numeric_only=True)

  # Make sure ALL csas and BaltimoreCity are included and sorted.
  snap = csa.merge( snap, left_on='CSA2010', right_on='CSA2010', how='outer' )
  # Baltimoire may have records not in the CSA (not actually the case right now but..)
  snap.at[55,'count']=snap['count'].sum()
  # Perform the calculation
  snap['???-snap'+year] = snap['count']

  compareYears = gpd.read_file("https://services1.arcgis.com/mVFRs7NF4iFitgbY/ArcGIS/rest/services/Snap/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=true&f=pgeojson");
  prevYear = 'snap'+ str( int(year) - 1 )
  if prevYear in compareYears.columns:
    snap = snap.merge( compareYears[['CSA2010', prevYear]], left_on='CSA2010', right_on='CSA2010', how='outer' )
    snap['change'] = snap['???-snap'+year] - snap[ prevYear ]
    snap['percentChange'] = snap['change' ] / snap[ prevYear ] * 100
    snap['change'] = snap['change'].apply(lambda x: "{:.2f}".format(x) )
  print( 'Records Matching Query: ', snap.size / len(snap.columns) )
  return snap