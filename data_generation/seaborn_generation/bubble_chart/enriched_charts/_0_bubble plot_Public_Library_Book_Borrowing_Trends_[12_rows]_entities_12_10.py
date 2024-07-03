
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data Frame generated from the CSV-like data provided above.
data = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte', 'Seattle', 'Denver', 'El Paso',
             'Detroit', 'Washington', 'Boston'],
    'Average_Temperature': [3.1, 16.7, 10.8, 20.6, 23.4, 12.0, 20.9, 17.5, 18.3, 15.2,
                            20.2, 21.3, 18.5, 11.7, 16.1, 10.5, 10.1, 17.8, 10.1, 13.8, 10.2],
    'Humidity': [65, 63, 70, 76, 39, 68, 66, 73, 65, 76, 65, 75, 65, 72, 68, 77, 52, 32, 71, 71, 67],
    'Population': [8419000, 3980400, 2706000, 2325500, 1663000, 1584200, 1547700,
                   1423800, 1340500, 1026900, 993200, 903000, 902000, 898000, 885400,
                   753600, 727200, 688700, 674800, 705700, 691500]
})

# Setting the plot style and color palette
sns.set(style="whitegrid")
palette = sns.color_palette(["#FF5733", "#33FF57", "#3357FF", "#F833FF"])

# Creating the bubble chart
plt.figure(figsize=(14, 10))
bubble = sns.scatterplot(x="Average_Temperature", y="Humidity", size="Population",
                         sizes=(100, 2000), hue="City", palette=palette, data=data, legend=False)

# Adding title and labels
plt.title('City Climate and Population Bubble Chart', fontsize=18)
plt.xlabel('Average Temperature (°C)', fontsize=14)
plt.ylabel('Humidity (%)', fontsize=14)

# Adjusting the axes and grids
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

# Showing the plot
plt.show()