
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating the DataFrame from the data provided
data = {
    'Month': ['January', 'February', 'March'],
    'Car': [50, 45, 40],
    'Bike': [20, 25, 30],
    'Bus': [15, 20, 20],
    'Train': [15, 10, 10]
}

df = pd.DataFrame(data)

# Calculate the percentage
df_percentage = df.copy()
df_percentage['Car'] = df['Car'] / 100 * df['Car'].sum()
df_percentage['Bike'] = df['Bike'] / 100 * df['Bike'].sum()
df_percentage['Bus'] = df['Bus'] / 100 * df['Bus'].sum()
df_percentage['Train'] = df['Train'] / 100 * df['Train'].sum()

# Create the horizontal stacked bar chart
categories = df_percentage['Month']
N = len(categories)
ind = np.arange(N)
width = 0.5

# Colors for each transport mode
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Stacking the bars
plt.barh(ind, df_percentage['Car'],   height=width, color=colors[0], label='Car')
plt.barh(ind, df_percentage['Bike'],  height=width, left=df_percentage['Car'], color=colors[1], label='Bike')
plt.barh(ind, df_percentage['Bus'],   height=width, left=df_percentage['Car'] + df_percentage['Bike'], color=colors[2], label='Bus')
plt.barh(ind, df_percentage['Train'], height=width, left=df_percentage['Car'] + df_percentage['Bike'] + df_percentage['Bus'], color=colors[3], label='Train')

# Title and labels
plt.title('Transportation Mode Usage (%) by Month')
plt.xlabel('Percentage')
plt.yticks(ind, categories)
plt.xlim(0, 100)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=4)

# Adjust the size of the chart
plt.subplots_adjust(left=0.2, right=0.8, top=0.9, bottom=0.1)

# Show the plot
plt.show()