
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating the data as a DataFrame
data = {
    'Destination': ['Paris', 'New York', 'Tokyo', 'Rome', 'London', 'Sydney', 'Barcelona', 'Dubai', 'Istanbul', 'Bangkok'],
    'Visitors': [2500, 1800, 2200, 1400, 2000, 1600, 1300, 2100, 1500, 1700]
}

df = pd.DataFrame(data)

# Sorting data to make the chart easier to read
df = df.sort_values('Visitors', ascending=False)

# Set up the matplotlib figure with changed width and height
plt.figure(figsize=(10, 8))

# Create the horizontal bar plot
sns.barplot(
    y='Destination',
    x='Visitors',
    data=df,
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#F333FF', '#33FFF5',
        '#F5FF33', '#FF33A8', '#33FFBD', '#FFC733', '#C733FF'
    ],
    linewidth=1.5,
    edgecolor='black'
)

# Adjust the height of the bars
for bar in plt.gca().patches:
    bar.set_height(0.6)

# Adding chart labels and title
plt.xlabel('Number of Visitors (in thousands)')
plt.ylabel('Travel Destination')
plt.title('Most Popular Travel Destinations')

# Show the plot
plt.show()