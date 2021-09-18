# geotwin

This is a an exploratory data analysis test presented to Geotwin by Mahmoud Albardan. The idea is to analyse the mobility patterns for Singapore.
To do so, I started with the dataset given by Geotwin and containing multiple columns about subzones in agents, subzones and the time we detected  these agents in the subzones given precise information about latitude and longitude.

From this dataset, I wanted to extract multiple features about two types of locations for each agent: the home and the work(or university if student, ect ..)
I determined the location of the home as the location at which the agent was at **0 O'clock** . I supposed that the working location of an agent is the one with the maximum duration outside its home.

Note: I am having some problems with jupyter notebook, that's why I created this repository.
