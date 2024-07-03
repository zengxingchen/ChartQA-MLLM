
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Constructing DataFrame from the table data.
data = {
    'City': ['London', 'Paris', 'Rome', 'Berlin', 'Madrid', 'Amsterdam', 'Prague', 
             'Vienna', 'Venice', 'Barcelona', 'Lisbon', 'Athens',
             'Dublin', 'Oslo', 'Stockholm', 'Helsinki', 'Copenhagen', 
             'Budapest', 'Warsaw', 'Istanbul'],
    'AverageMoviesWatched': [50, 55, 40, 60, 45, 48, 52, 46, 51, 58, 
                             47, 49, 53, 41, 42, 44, 43, 54, 56, 57],
    'LeisureHoursPerYear': [1200, 1300, 1100, 1250, 1150, 1220, 1170, 1210, 1240, 
                            1270, 1190, 1230, 1260, 1120, 1130, 1140,
                            1180, 1215, 1280, 1290]
}

df = pd.DataFrame(data)

# Create a scatterplot.
plt.figure(figsize=(14, 10))
sns.scatterplot(data=df, x='AverageMoviesWatched', y='LeisureHoursPerYear', 
                palette=['#FF4500', '#1E90FF'], 
                s=120)  # s is the marker size

# Add chart title and labels
plt.title('Relationship between Average Movies Watched and Leisure Hours in European Cities', fontsize=18)
plt.xlabel('Average Movies Watched per Year', fontsize=14)
plt.ylabel('Leisure Hours per Year', fontsize=14)

# Show the plot
plt.show()