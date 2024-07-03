
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Constructing DataFrame from the table data.
data = {
    'City': ['London', 'Paris', 'Rome', 'Berlin', 'Madrid', 'Amsterdam', 'Prague', 
             'Vienna', 'Venice', 'Barcelona', 'Lisbon', 'Athens',
             'Dublin', 'Oslo', 'Stockholm', 'Helsinki', 'Copenhagen', 
             'Budapest', 'Warsaw', 'Istanbul'],
    'AverageTemperature': [15.1, 16.5, 20.4, 13.2, 17.8, 12.6, 12.4, 12.1, 16.7, 18.2, 
                           19.5, 21.2, 11.3, 9.8, 10.5, 8.7, 11.9, 13.3, 12.7, 19.1],
    'TouristVisits': [19200, 21500, 27900, 18600, 23000, 19800, 17600, 17200, 20500, 
                      26000, 23900, 25700, 16400, 14900, 15300, 12700,
                      15900, 17400, 17100, 27800]
}

df = pd.DataFrame(data)

# Create a scatterplot.
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='AverageTemperature', y='TouristVisits', 
                palette=['#FF6347', '#4682B4'], 
                s=100)  # s is the marker size

# Add chart title and labels
plt.title('Relationship between Average Temperature and Tourists Visits in European Cities', fontsize=16)
plt.xlabel('Average Temperature (°C)', fontsize=14)
plt.ylabel('Number of Tourist Visits', fontsize=14)

# Show the plot
plt.show()