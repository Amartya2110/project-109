import pandas as pd
import csv 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random 

df = pd.read_csv("data.csv")
reading_score = df["reading score"].to_list()
mean = statistics.mean(reading_score)
std_deviation = statistics.stdev(reading_score)
median = statistics.median(reading_score)
mode = statistics.mode(reading_score)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([reading_score], ["reading scores"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()