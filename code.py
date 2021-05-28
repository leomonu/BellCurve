import random
import plotly.figure_factory as ff

diceSum = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    sum = dice1 + dice2
    diceSum.append(sum)
    count.append(i)



fig = ff.create_distplot([diceSum],["Result"],show_hist=False)
fig.show()