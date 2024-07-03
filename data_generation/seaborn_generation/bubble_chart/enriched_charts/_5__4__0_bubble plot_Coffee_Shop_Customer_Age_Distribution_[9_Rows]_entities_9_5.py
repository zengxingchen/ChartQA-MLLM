
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from the data above.
data = {
    'Art Piece': ['Sculpture A', 'Sculpture B', 'Sculpture C', 'Sculpture D', 'Sculpture E', 
                  'Sculpture F', 'Sculpture G', 'Sculpture H', 'Sculpture I', 'Sculpture J', 
                  'Sculpture K', 'Sculpture L', 'Sculpture M', 'Sculpture N'],
    'Gallery Attendance': [12000, 14000, 11000, 16000, 15000, 
                           13000, 17000, 12500, 15500, 13500, 
                           14500, 11500, 16500, 12200],
    'Media Coverage': [80, 90, 75, 100, 95, 
                       85, 105, 80, 98, 87,
                       92, 78, 103, 81],
    'Artist Popularity': [7.8, 8.5, 7.2, 8.9, 8.7, 
                          8.0, 9.0, 7.9, 8.8, 8.3,
                          8.6, 7.5, 8.9, 7.8]
}

df = pd.DataFrame(data)

# Define the bubble chart
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df, x='Gallery Attendance', y='Media Coverage', 
                               hue='Artist Popularity', size='Artist Popularity', 
                               sizes=(100, 1000), alpha=0.7, 
                               palette=["#FF6347", "#FFA500", "#FFD700", "#32CD32", 
                                        "#4682B4", "#6A5ACD", "#FF69B4", "#8B4513",
                                        "#00FA9A", "#20B2AA", "#7B68EE", "#FF00FF", "#4B0082"])

# Enhance legend and labels
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Artist Popularity')
plt.title('Gallery Attendance vs. Media Coverage by Art Piece with Artist Popularity', fontsize=18, pad=20)
plt.xlabel('Gallery Attendance', fontsize=14)
plt.ylabel('Media Coverage', fontsize=14)

# Create the visualization
plt.show()