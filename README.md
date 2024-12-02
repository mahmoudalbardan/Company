# Company

The idea is to analyse the mobility patterns for city in Singapore.
To do so, I started with the dataset and containing multiple columns about subzones in agents, subzones and the time we detected  these agents in the subzones given precise information about latitude and longitude.

From this dataset, I wanted to extract multiple features about two types of locations for each agent: the home and the work(or university if student, ect ..)
I determined the location of the home as the location at which the agent was at **0 O'clock** . I supposed that the working location of an agent is the one with the maximum duration outside its home.


You will find in this repository the python script `code.py`, the csv dataframe file that I computed and used to infer the information `new_dataframe.csv` and few `png` files:
1. distance from home to work (in km)
2. time from home to work (in hours)
3. start working time (in hours)
4. end working time (in hours)
5. heatmap of home locations in city
6. heatmap of work locations in city



Notes: 
1. I am having some problems with jupyter notebook, that's why I created this repository.
2. I did not make an outlier detetion phase due to the time given to the test but it should be added. Outliers can be seen obviously in the histograms.



# Types of Car Collisions and Their Percentages

Car collisions can be categorized based on the nature of the crash. Below are the common types of collisions along with approximate percentage ranges (note: percentages vary by region, road conditions, and traffic patterns).
(https://crashstats.nhtsa.dot.gov/#!/PublicationList/35)), page82


## 1. Rear-End Collisions (29-38%)
- **Description**: Occur when a vehicle crashes into the vehicle directly in front of it.
- **Source**: [NHTSA Data][https://www.nhtsa.gov/]

## 2. Side-Impact Collisions (T-Bone) (13-27%)
- **Description**: Happen when the front of one vehicle crashes into the side of another.

## 3. Head-On Collisions (2-10%)
- **Description**: Involve the front ends of two vehicles colliding.

## 4. Sideswipe Collisions (7-12%)
- **Description**: Occur when the side of one vehicle scrapes or collides with the side of another.

