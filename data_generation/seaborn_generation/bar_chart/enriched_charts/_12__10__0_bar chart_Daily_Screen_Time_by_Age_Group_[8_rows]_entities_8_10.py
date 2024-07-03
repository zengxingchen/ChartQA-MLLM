
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data points
data = {
    'Destination': ['Paris', 'Tokyo', 'New York', 'Sydney', 'Rome', 'Cape Town', 'Dubai'],
    'AverageExpense': [1500, 2000, 1800, 2200, 1600, 1700, 2100]
}
df = pd.DataFrame(data)

# Setting the color codes for clarity
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Initialize the matplotlib figure size
f, ax = plt.subplots(figsize=(10, 8))

# Create the horizontal bar chart
sns.barplot(y='Destination', x='AverageExpense', data=df, palette=colors)

# Setting the bar width
for container in ax.containers:
    plt.setp(container, height=0.6)

# Customize the chart
plt.title('Average Travel Expense to Various Destinations')
plt.xlabel('Average Expense ($)')
plt.ylabel('Destination')

# Display the chart
plt.show()