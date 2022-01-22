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

fig=ff.create_distplot([data],["Math_score"],show_hist=False)
fig.show()

