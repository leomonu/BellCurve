import random
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")
height = df["Height(Inches)"].tolist()


fig = ff.create_distplot([height],["Height in Inches"],show_hist = False)
fig.show()
