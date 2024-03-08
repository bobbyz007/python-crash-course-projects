from die import Die
import plotly.express as px

# Generate data
die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
frequencies = []
poss_results = range(2, die_1.num_sides + die_2.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling Two D6 Dice 1000 times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# Further customize chart. specifies the distance between tick marks on the x-axis so that every bar is labeled
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html("dice_visual.html")