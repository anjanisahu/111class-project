import csv
import pandas as pd
import plotly.express as px
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random
df=pd.read_csv("math_score.csv")
data=df["Math_score"].tolist()

mean=statistics.mean(data)
print("MEAN:")
print(mean)

median=statistics.median(data)
print("MEDIAN:")
print(median)

mode=statistics.mode(data)
print("MODE:")
print(mode)

standard_deviation=statistics.stdev(data)
print("STANDARD DEVIATION:")
print(standard_deviation)

def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data)
    print("MEAN:")
    print(mean)
    return mean    

mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)
    #standard_devation
std_deviation=statistics.stdev(data)
print("STANDARD DEVIATION:")
print(standard_deviation)   

#variables
first_std_deviation_start,first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.
df = pd.read_csv("grp3.csv") 
data = df["Math_score"].tolist() 
mean_of_sample3 = statistics.mean(data)
print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO GOT FUNSHEETS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()


   



