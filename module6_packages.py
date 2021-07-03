##################### problem1 ######################

# 1.For the dataset “Indian_cities”, 
# a)Find out top 10 states in female-male sex ratio
# b)Find out top 10 cities in total number of graduates
# c)Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

import pandas as pd
state = pd.read_csv("C:/Users/DELL/Downloads/Python Problem Statements/Indian_cities.csv")

a = state.nlargest(10 ,'sex_ratio')[['state_name', 'sex_ratio' ]]
a
b = state.nlargest(10,'total_graduates')[['name_of_city', 'total_graduates']]
b
c = state.nlargest(10,'effective_literacy_rate_total')[['name_of_city','location','effective_literacy_rate_total']]

######################## problem2 #############################
# 2.For the data set “Indian_cities”
# a)Construct histogram on literates_total and comment about the inferences
# b)Construct scatter  plot between  male graduates and female graduates

import matplotlib.pyplot as plt
plt.hist(state["literates_total"])    
plt.xlabel('literates_total')
# from the histogram graph we can say that graph is positively skewed 
# there is a presence of outliers
# most of the values lies in between 0.01*1e7 to 0.1*le7
plt.scatter(state['male_graduates'],state['female_graduates'])
#positive association
# strong association
#linear association
###################### problem3 ################################
# 3.For the data set “Indian_cities”
# a)Construct Boxplot on total effective literacy rate and draw inferences
# b)Find out the number of null values in each column of the dataset and delete them.

plt.boxplot(state['effective_literacy_rate_total'])
#there is a presence of outliers
# graph is negatively skewed
# least value of the outlier is 50
# minimum quartile value is 70
#maximum quartile value is 96
state.isna().sum()
state.dropna()
