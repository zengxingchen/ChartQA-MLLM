
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Prepare the data in a Pandas DataFrame
data = {
    'Destination': ['Paris', 'New York', 'Tokyo', 'Sydney', 'Dubai', 'Rome', 'Barcelona', 'Bangkok', 'Cape Town', 'Istanbul', 'Rio de Janeiro'],
    'Average_Cost': [3000, 2500, 2000, 3500, 4000, 2700, 2200, 1500, 1800, 2300, 2600],
    'Popularity': [85, 90, 75, 70, 80, 65, 95, 60, 55, 70, 50],
    'Visitors': [2.1, 3.5, 4.1, 1.8, 1.5, 2.0, 2.7, 3.9, 1.2, 1.4, 1.3]
}
df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(16, 10))
bubble = sns.scatterplot(data=df, x='Average_Cost', y='Visitors', size='Popularity', hue='Destination', 
                         palette=['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#FFFF33', '#33FFFF', '#FF33FF', '#333FFF', '#33FF3F', '#3F33FF'], 
                         sizes=(20, 1000), alpha=0.7, edgecolor='w', linewidth=0.5)

# Customize the axes and title
plt.title('Top Travel Destinations: Cost vs. Visitor Numbers Popularity Bubble Chart', fontsize=16, pad=20)
plt.xlabel('Average Cost ($)', fontsize=12)
plt.ylabel('Number of Visitors (Millions)', fontsize=12)

# Adjust legend
bubble.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Destinations')

# Show the bubble chart
plt.show()