
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Table data as a string to mimic reading a CSV.
csv_data = """Month,Books,Games,Movies
January,15000,10000,7000
February,16000,11000,7500
March,17000,11500,8000
April,18000,12000,8500
May,19000,12500,9000
June,20000,13000,9500
July,21000,13500,10000
August,22000,14000,10500
September,23000,14500,11000
October,24000,15000,11500
November,25000,15500,12000
December,26000,16000,12500
"""

# Read the CSV data into a DataFrame.
data = pd.read_csv(StringIO(csv_data), index_col='Month')

# Prepare the data for the stacked area chart.
x = data.index
y = [data['Books'], data['Games'], data['Movies']]

# Create the plot.
fig, ax = plt.subplots(figsize=(12, 8))  # Change width and height of the chart.

# Plot the stacked area chart.
ax.stackplot(x, y, labels=['Books', 'Games', 'Movies'], colors=['#FF6F61', '#6B5B95', '#88B04B'])

# Customize the chart.
ax.set_title('Monthly Entertainment Sales Report (in Units)', fontsize=16)  # Change the topic and headline.
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.legend(loc='upper right')

# Assign annotation/text label on the chart.
for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Books']}", xy=(i, values['Books']/2), ha='center', fontsize=8, color='black')
    ax.annotate(f"{values['Games']}", xy=(i, values['Books'] + values['Games']/2), ha='center', fontsize=8, color='black')
    ax.annotate(f"{values['Movies']}", xy=(i, values['Books'] + values['Games'] + values['Movies']/2), ha='center', fontsize=8, color='black')

# Show the plot.
plt.tight_layout()
plt.show()