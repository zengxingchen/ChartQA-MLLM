
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Table data as a string to mimic reading a CSV.
csv_data = """Month,Electronics,Clothing,Home Goods
January,20000,15000,5000
February,22000,16000,5100
March,23000,16500,5300
April,25000,18000,5400
May,27000,19000,5500
June,26000,18500,5600
July,28000,20000,6000
August,29000,21000,6100
September,30000,22000,6200
October,31000,23000,6300
November,32000,24000,6400
December,34000,25000,6500
"""

# Read the CSV data into a DataFrame.
data = pd.read_csv(StringIO(csv_data), index_col='Month')

# Prepare the data for the stacked area chart.
x = data.index
y = [data['Electronics'], data['Clothing'], data['Home Goods']]

# Create the plot.
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart.

# Plot the stacked area chart.
ax.stackplot(x, y, labels=['Electronics', 'Clothing', 'Home Goods'], colors=['#FF5733', '#33C1FF', '#8EFF33'])

# Customize the chart.
ax.set_title('Monthly Sales Report (in USD)')  # Change the topic and headline.
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.legend(loc='upper left')

# Assign annotation/text label on the chart.
for i, (month, values) in enumerate(data.iterrows()):
    ax.annotate(f"{values['Electronics']}", xy=(i, values['Electronics']/2), ha='center')
    ax.annotate(f"{values['Clothing']}", xy=(i, values['Electronics']+values['Clothing']/2), ha='center')
    ax.annotate(f"{values['Home Goods']}", xy=(i, values['Electronics']+values['Clothing']+values['Home Goods']/2), ha='center')

# Show the plot.
plt.tight_layout()
plt.show()