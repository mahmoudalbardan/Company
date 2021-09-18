# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:20:04 2021

@author: albardan
"""
import sys
import pandas as pd
from math import cos, asin, sqrt, pi
import matplotlib.pyplot as plt
from collections import Counter
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon
sys.exit()
path = "pop_SG_sample_GT_disaggregated.csv"
dataframe = pd.read_csv(path)

# check for nan values
print (dataframe.isnull().sum()) # clean dataset

# get info about the dataset
print (dataframe.info()) 

# see how many person in the dataset
print (len(dataframe["agent"].unique())) # 100000 person in the dataset 


# convert time 0 and time1 to datetime objects
#dateframe["time0"] = pd.to_datetime(dataframe["time0"],format="%H:%M:%S")
#dateframe["time1"] = pd.to_datetime(dataframe["time1"],format="%H:%M:%S")


# distance in km
def distance(lat1, lon1,
             lat2, lon2):
    """
    calculate distance between two points 
    based on longitude and lattitude (from stackoverflow)
    """
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))   

# for each person we suppose he has home location and (work,school, university) location
# we want to speficy the home location: the location in the night (after midnight until morning)
# first we group rows of each agent

gagent = dataframe.groupby(by="agent")
gagent = [gp[1] for gp in gagent]

list_of_dfs = []
for j,gp in enumerate(gagent):
    print (j)
    try:
        df = pd.DataFrame([])
        gp = gp[gp["duration"]!=0] # remove rows with duration 0
        subzones = list(gp["subzone"].unique())
        if len(subzones)>1:
            # defining home
            home_info = gp[gp["time0"]=="00:00:00"] # define home
            home_subzone = home_info["subzone"].values[0]
            
            # defining work
            outside_info = gp[gp["subzone"]!=home_subzone]
            work_index = outside_info[outside_info["duration"]==outside_info["duration"].max()].index[0]
            work_info = gp.loc[work_index]  
            
            
            # creating a the new dataframe
            df["agent"] = gp["agent"].unique()
            df["home_subzone"] = home_info["subzone"].values
            df["home_lon"] = home_info["lon"].mean()
            df["home_lat"] = home_info["lat"].mean()
            df["work_subzone"] = work_info["subzone"]
            df["work_lon"] = work_info["lon"].mean()
            df["work_lat"] = work_info["lat"].mean()
            df["nb_subzones"] =  len(subzones)
            df["time_at_work"] =  outside_info["duration"].sum()  # outside duration is equal to work duration
            df["distance_to_work"] = distance( home_info["lat"].mean(),
                                                 home_info["lon"].mean(),
                                                 work_info["lat"].mean(),
                                                 work_info["lon"].mean())
            df["work_start_time"] = work_info["time0"]
            df["work_end_time"] = work_info["time1"]
            df["time_to_work"] =int(work_info["time0"][:2]) - int(home_info["time1"].values[0][:2])
        else:
            home_info = gp[gp["time0"]=="00:00:00"] # define home
            home_subzone = home_info["subzone"].values[0]
            df["agent"] = gp["agent"].unique()
            df["home_subzone"] = home_info["subzone"].values
            df["home_lon"] = home_info["lon"].mean()
            df["home_lat"] = home_info["lat"].mean()
            print ("one subzone")
    except:
        continue
    list_of_dfs.append(df)
        
new_dataframe = pd.concat(list_of_dfs)
new_dataframe.to_pickle("new_dataframe")
new_dataframe = pd.read_pickle("new_dataframe")
    


# Exploratory data analysis
variables = ['agent', 'home_subzone', 
       'home_lon', 'home_lat', 
       'work_subzone',
       'work_lon', 'work_lat',
       'nb_subzones', 'time_at_work',
       'distance_to_work', 'work_start_time', 
       'work_end_time', 'time_to_work']

var = "distance_to_work"
y = new_dataframe[var].values.tolist()


plt.figure()
plt.hist(new_dataframe["distance_to_work"].values.tolist(),bins=50)
plt.title("distance to work (in km) distribution")
plt.show()


plt.figure()
plt.hist(new_dataframe["time_to_work"].values.tolist(),bins=50)
plt.title("time to work (in hours) distribution")
plt.show()



var = "work_start_time"
y = new_dataframe[var].values.tolist()
y = [int(e[:2]) for e in y if str(e)!='nan']

plt.figure()
plt.hist(y,bins=48)
plt.title("Work starting time (in hours) distribution")
plt.show()


var = "work_end_time"
y = new_dataframe[var].values.tolist()
y = [int(e[:2]) for e in y if str(e)!='nan']


plt.figure()
plt.hist(y,bins=48)
plt.title("Work ending time (in hours) distribution")
plt.show()


    
home_locations = new_dataframe[["home_lat","home_lon"]]
work_locations = new_dataframe[["work_lat","work_lon"]]
work_locations.dropna(axis=0,inplace=True,how="any")


map_name = "SGP_adm0.shp"
mapfile = gpd.read_file(map_name)
fig,ax = plt.subplots(figsize=(15,15))
mapfile.plot(ax=ax,color="grey", alpha=0.3)

geometry_home = [Point(xy) for xy in zip(home_locations["home_lon"],home_locations["home_lat"])]



import pandas as pd
from folium import Map
from folium.plugins import HeatMap


for_map = Map(location=[1.42825, 103.84825], zoom_start=8, )
hm_wide = HeatMap(
    list(zip(for_map.latitude.values, for_map.longitude.values)),
    min_opacity=0.2,
    radius=17, 
    blur=15, 
    max_zoom=1,
)

















# import gmaps

# api_key = "AIzaSyA2b3hxqyl1U5EnDp0RgaE4njUhkvxGqf0"
# gmaps.configure(api_key=api_key)

# fig = gmaps.figure()
# fig.add_layer(gmaps.heatmap_layer(home_locations))
# fig

# fig = gmaps.figure()
# fig.add_layer(gmaps.heatmap_layer(work_locations))
# fig



# Lon = np.arange(-71.21, -71, 0.0021) 
# Lat = np.arange(42.189, 42.427, 0.00238) 


# Straits of Singapore
# 1.183374, 103.597561


# Straits of Singapore
# 1.312010, 104.128733



# 1.568313, 104.073656

# 1.434647, 103.515127