# Plotting Bar Charts with Matplotlib

```python
import matplotlib.pyplot as plt

# Create a figure and a set of subplots (a single subplot in this case)
fig, ax = plt.subplots()
# Creates a figure (fig) and a single subplot (ax). The fig is the container that holds everything, and ax is the axes object where the data will be plotted.

# Data for the bar chart
x = [0, 1, 2]
y = [59, 150, 48]

# Create a bar chart with the specified width of a bar
ax.bar(x, y, width=0.2)

# Set the label for the x-axis
ax.set_xlabel('Category')

# Set the label for the y-axis
ax.set_ylabel('Counts')

# Set the positions of the ticks on the x-axis
ax.set_xticks([0, 1, 2])

# Set the labels for the ticks on the x-axis and the font size of the labels
ax.set_xticklabels(['0', '1', '2'], fontsize=12)

# Add text labels above each bar displaying the height of the bar
for index, value in enumerate(y):
    plt.text(x=int(index), y=value + 1, s=str(value), ha='center') # y=value+1 to put the text label above the bar, to prevent overlapping

# Adjust the layout to make sure everything fits within the figure area
plt.tight_layout()

# Display the plot
plt.show()


```
