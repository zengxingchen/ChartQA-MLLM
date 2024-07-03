
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data above
data = {
    'Location': ['Paris', 'London', 'New York', 'Tokyo', 'Sydney', 
                 'Rome', 'Barcelona', 'Berlin', 'Dubai', 'Singapore', 
                 'Hong Kong', 'Bangkok', 'Los Angeles', 'Amsterdam'],
    'Visitor Numbers': [18000, 17000, 19000, 16000, 17500, 
                        16500, 15500, 15000, 14500, 16000, 
                        15200, 14800, 15800, 15100],
    'Average Review Score': [4.7, 4.5, 4.8, 4.6, 4.4, 
                             4.6, 4.3, 4.4, 4.5, 4.7, 
                             4.6, 4.3, 4.5, 4.4],
    'Travel Popularity': [9.2, 8.9, 9.5, 8.7, 8.8, 
                          8.6, 8.5, 8.4, 8.3, 8.7,
                          8.5, 8.4, 8.6, 8.5]
}

df = pd.DataFrame(data)

# Define the bubble chart
plt.figure(figsize=(18, 14))
bubble_chart = sns.scatterplot(data=df, x='Visitor Numbers', y='Average Review Score', 
                               hue='Travel Popularity', size='Travel Popularity', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#1E90FF", "#32CD32", "#FFD700", "#FF6347", 
                                        "#8A2BE2", "#FF4500", "#00CED1", "#DA70D6",
                                        "#FF1493", "#20B2AA", "#7B68EE", "#FF00FF", "#4B0082"])

# Enhance legend and labels
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Travel Popularity')
plt.title('Visitor Numbers vs. Average Review Score by Location with Travel Popularity', fontsize=18, pad=20)
plt.xlabel('Visitor Numbers', fontsize=14)
plt.ylabel('Average Review Score', fontsize=14)

# Create the visualization
plt.show()