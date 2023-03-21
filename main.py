import pandas as pd
import numpy as np

# Read coordinates and get index
coordinates=pd.read_csv("coordinates_2021_august6_august12_geocodio_b2946f753524e70f3a68a1da581cd14abdeb272b.csv", header=None)
state_list = coordinates[[11]].values.tolist()
county_list= coordinates[[12]].values.tolist()

indx=[]
CA_county_list=[]
for i in range(len(state_list)):
    if ['CA'] == state_list[i]:
        indx.append(i)


for value in indx:
  CA_county_list.append(county_list[value])
CA_county_list=[county for sublist in CA_county_list for county in sublist]
print(CA_county_list)
region=[]
for i in CA_county_list:
  if i =="Butte County" or i == "Colusa County" or i == "El Dorado County" or i == "Glenn County" or i == "Lassen County" or i == "Modoc County" or i == "Nevada County" or i == "Placer County" or i == "Plumas County" or i == "Sacramento County" or i == "Shasta County" or i == "Sierra County" or i == "Siskiyou County" or i == "Sutter County" or i == "Tehama County" or i == "Yolo County" or i == "Yuba County":
    region.append(1)
  elif i=="Del Norte County" or i == "Humboldt County" or i == "Lake County" or i == "Mendocino County" or i == "Napa County" or i == "Sonoma County" or i == "Trinity County":
    region.append(2)
  elif i=="Alameda County" or i == "Contra Costa County" or i == "Marin County" or i == "San Francisco County" or i == "San Mateo County" or i == "Santa Clara County" or i == "Solano County":
    region.append(3)
  elif i=="Alpine County" or i == "Amador County" or i == "Calaveras County" or i == "Madera County" or i == "Mariposa County" or i == "Merced County" or i == "Mono County" or i == "San Joaquin County" or i == "Stanislaus County" or i == "Tuolumne County":
    region.append(4)
  elif i=="Monterey County" or i == "San Benito County" or i == "San Luis Obispo County" or i == "Santa Barbara County" or i == "Santa Cruz County" or i == "Ventura County":
    region.append(5)
  elif i=="Fresno County" or i == "Inyo County" or i == "Kern County" or i == "Kings County" or i == "Tulare County":
    region.append(6)
  elif i=="Riverside County" or i == "San Bernardino County":
    region.append(7)
  elif i=="Los Angeles County":
    region.append(8)
  elif i=="Orange County":
    region.append(9)
  elif i=="Imperial County" or i =="San Diego County":
    region.append(10)
  else:
    region.append("NA")
    print(i)
print(region)
# Read full and get ID
full=pd.read_csv("full_2021_august6_august12.csv", on_bad_lines='skip', header=None)
full_ID_list=full[[6]].values.tolist()
CA_ID_list=[]
for value in indx:
  CA_ID_list.append(full_ID_list[value])



CA_ID_list = [int(num) for sublist in CA_ID_list for num in sublist]
# Read ID+senti and get senti
senti = pd.read_csv("id+senti_2021_august6_august12.csv", on_bad_lines='skip', header=None)
ID_list=senti[[0]].values.tolist()
full_senti_list=senti[[1]].values.tolist()
ID_list=[int(num) for sublist in ID_list for num in sublist]

full_senti_list=[num for sublist in full_senti_list for num in sublist]

CA_senti=[]
for i in range(len(CA_ID_list)):
  if CA_ID_list[i] in ID_list:
    CA_senti.append(full_senti_list[i])

print(len(CA_senti))
print(len(CA_county_list))
print(len(region))
dict = {'ID': CA_ID_list, 'Sentiment': CA_senti, 'County': CA_county_list,'Region':region} 
df = pd.DataFrame(dict)
df.to_csv("id+senti+county+region_2021_august6_august12.csv",index=False)


