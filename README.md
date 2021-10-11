# Company

This is a an exploratory data analysis test presented to "Company" by Mahmoud Albardan. The idea is to analyse the mobility patterns for Singapore.
To do so, I started with the dataset given by "Compnay" and containing multiple columns about subzones in agents, subzones and the time we detected  these agents in the subzones given precise information about latitude and longitude.

From this dataset, I wanted to extract multiple features about two types of locations for each agent: the home and the work(or university if student, ect ..)
I determined the location of the home as the location at which the agent was at **0 O'clock** . I supposed that the working location of an agent is the one with the maximum duration outside its home.


You will find in this repository the python script `code.py`, the csv dataframe file that I computed and used to infer the information `new_dataframe.csv` and few `png` files:
1. distance from home to work (in km)
2. time from home to work (in hours)
3. start working time (in hours)
4. end working time (in hours)
5. heatmap of home locations in Singapore
6. heatmap of work locations in Singapore



Notes: 
1. I am having some problems with jupyter notebook, that's why I created this repository.
2. I did not make an outlier detetion phase due to the time given to the test but it should be added. Outliers can be seen obviously in the histograms.
