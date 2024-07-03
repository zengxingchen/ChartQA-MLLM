
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
             'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
             'Fort Worth', 'Columbus', 'Charlotte', 'Seattle', 'Denver', 'El Paso',
             'Detroit', 'Washington', 'Boston'],
    'Average_Fitness_Level': [7.5, 8.0, 7.2, 6.8, 7.1, 6.9, 6.5, 8.1, 7.0, 7.8,
                              8.3, 6.7, 6.9, 7.2, 7.0, 7.9, 8.2, 6.4, 6.6, 7.6, 7.8],
    'Gym_Density': [8.2, 7.9, 8.0, 7.4, 6.8, 7.0, 6.9, 8.5, 7.6, 7.2,
                    8.7, 6.6, 6.8, 7.1, 7.0, 8.3, 8.0, 6.4, 6.7, 7.5, 8.1],
    'Population': [8419000, 3980400, 2706000, 2325500, 1663000, 1584200, 1547700,
                   1423800, 1340500, 1026900, 993200, 903000, 902000, 898000, 885400,
                   753600, 727200, 688700, 674800, 705700, 691500]
})

sns.set(style="whitegrid")
palette = sns.color_palette(["#FF6347", "#3CB371", "#1E90FF", "#FFD700", "#FF69B4", "#8A2BE2", "#00CED1", "#DC143C", "#FF4500", "#2E8B57"])

plt.figure(figsize=(16, 12))
bubble = sns.scatterplot(x="Average_Fitness_Level", y="Gym_Density", size="Population",
                         sizes=(100, 2000), hue="City", palette=palette, data=data, legend='brief')

plt.title('City Fitness Levels and Gym Density Bubble Chart', fontsize=20)
plt.xlabel('Average Fitness Level', fontsize=16)
plt.ylabel('Gym Density (per 100,000 people)', fontsize=16)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.show()