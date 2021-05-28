import random
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")

weight = df["Weight(Pounds)"].tolist()

fig = ff.create_distplot([weight],["Weight in Pounds"],show_hist=False)
fig.show()
