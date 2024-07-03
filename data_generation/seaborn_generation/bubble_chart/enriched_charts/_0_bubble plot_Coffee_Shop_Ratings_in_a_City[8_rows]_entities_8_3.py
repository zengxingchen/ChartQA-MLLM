
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Prepare the data in a Pandas DataFrame
data = {
    'Model': ['Sedan A', 'SUV B', 'Hatchback C', 'Sports D', 'Minivan E', 'Truck F', 'Crossover G', 'Coupe H', 'Convertible I', 'Electric J', 'Hybrid K'],
    'MPG': [24, 18, 30, 22, 20, 15, 25, 27, 23, 120, 75],
    'Cost': [25000, 35000, 18000, 45000, 28000, 33000, 30000, 39000, 48000, 58000, 32000],
    'Popularity': [70, 80, 60, 90, 40, 50, 85, 75, 65, 95, 85]
}
df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(14, 8))
bubble = sns.scatterplot(data=df, x='Cost', y='MPG', size='Popularity', hue='Model', 
                         palette=['#FF5733','#33FF57','#3357FF','#57FF33','#FF3357','#FFFF33','#33FFFF','#FF33FF','#333FFF','#33FF3F','#3F33FF'], 
                         sizes=(20, 1000), alpha=0.7, edgecolor='w', linewidth=0.5)

# Customize the axes and title
plt.title('Car Model Performance: Fuel Efficiency vs. Cost Popularity Bubble Chart', fontsize=16)
plt.xlabel('Average Cost ($)', fontsize=12)
plt.ylabel('Miles per Gallon (MPG)', fontsize=12)

# Adjust legend
bubble.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Car Models')

# Show the bubble chart
plt.show()