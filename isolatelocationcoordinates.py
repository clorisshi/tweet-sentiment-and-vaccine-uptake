import pandas as pd
import numpy as np

df=pd.read_csv("full_2021_december17_december23.csv", header=None)
print(df)
coordinates = df[[0]]
# print(coordinates)
# Split up the coordinates into longitude and latitude. (Remember that it goes longitude, latitude).
list = (coordinates[[0]].values.tolist())[1:]
flattened=[]
longitude=[]
latitude=[]
print(coordinates)
print(coordinates.notnull())
df2 = coordinates.replace(np.nan, '0,0', regex=True)
list = (df2[[0]].values.tolist())[1:]
print(list)
for sublist in list:
  for val in sublist:
    flattened.append(val)
print(flattened)
for coord in flattened:
  val=coord.split(",")
  longitude.append(float(val[0]))
  latitude.append(float(val[1]))


final = pd.DataFrame(zip(latitude,longitude))
print(final)
final.to_csv("coordinates_2021_december17_december23.csv",index=False)
