
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Location': ['Paris', 'New York', 'Tokyo', 'Sydney', 'Rome', 'Cape Town', 'Rio de Janeiro', 'Bangkok', 'Dubai', 'London', 'Barcelona', 'Hong Kong', 'Singapore', 'Istanbul', 'Los Angeles'],
    'Average_Rating': [4.8, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 4.0, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 10))
sns.barplot(y='Location', x='Average_Rating', data=df, palette=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#33FFA1", "#FF8C33", "#B833FF", "#FF5733", "#57FF33", "#5733FF", "#33FFF2", "#F2FF33", "#FF33F2", "#A1FF33", "#8C33FF"], linewidth=0.8)

# Customize the chart
plt.title('Average Ratings of Popular Travel Destinations', fontsize=18, pad=20)
plt.ylabel('Location', fontsize=14)
plt.xlabel('Average Rating', fontsize=14)
plt.grid(axis='y')

# Show the plot
plt.show()