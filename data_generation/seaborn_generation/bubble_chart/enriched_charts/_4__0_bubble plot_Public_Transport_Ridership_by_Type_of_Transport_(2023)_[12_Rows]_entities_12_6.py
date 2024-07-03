
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = {
    'Destination': ['Paris', 'New York', 'Tokyo', 'Barcelona', 'Rome', 'Dubai', 'London', 'Bangkok', 'Singapore', 'Istanbul'],
    'Visitors': [38.2, 32.1, 29.3, 24.7, 21.4, 20.2, 19.3, 18.5, 17.8, 15.7],
    'Revenue': [18.5, 16.4, 14.8, 12.1, 11.5, 10.8, 9.7, 9.1, 8.4, 7.9],
    'ReviewScore': [4.7, 4.5, 4.6, 4.3, 4.4, 4.5, 4.6, 4.2, 4.5, 4.3]
}
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 10))

# Create the bubble chart
bubble = sns.scatterplot(data=df, x='ReviewScore', y='Visitors', size='Revenue', 
                         hue='Destination', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
                                                     '#33FFFB', '#FFFB33', '#FBFF33', '#837FF3',
                                                     '#8FF73F', '#3FF786'],
                         sizes=(100, 2000), alpha=0.7, edgecolor='w', linewidth=1)
bubble.set_title('Top Tourist Destinations by Visitors and Reviews in 2023', weight='bold', size=18, pad=20)
bubble.set_xlabel('Average Review Score', weight='bold', size=14)
bubble.set_ylabel('Visitors (in millions)', weight='bold', size=14)

# Adjust legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.show()