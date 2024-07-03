
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    'Country': ['USA', 'USA', 'China', 'China', 'India', 'India', 'Germany', 'Germany', 'Brazil', 'Brazil', 'France', 'France'],
    'FoodItem': ['Beef', 'Chicken', 'Rice', 'Pork', 'Wheat', 'Milk', 'Potatoes', 'Apples', 'Coffee', 'Sugarcane', 'Cheese', 'Wine'],
    'ProductionVolume': [90000, 120000, 300000, 150000, 180000, 80000, 95000, 40000, 85000, 30000, 70000, 20000],
    'Calories': [250, 210, 130, 242, 339, 42, 77, 52, 2, 36, 402, 83]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(16, 12))
bubble_plot = sns.scatterplot(data=df, x='Country', y='Calories', size='ProductionVolume', hue='FoodItem',
                              sizes=(100, 2000), alpha=0.7, palette=["#8A2BE2", "#5F9EA0", "#D2691E", "#FF7F50", "#6495ED", "#DC143C", "#00008B", "#006400", "#B8860B", "#8B0000", "#E9967A", "#8FBC8F"])

# Customize legend and axis labels
bubble_plot.legend(title='Food Item', loc='upper right')
plt.xlabel('Country')
plt.ylabel('Calories per 100g')
plt.title('Calories Content by Food Item in Different Countries', pad=20)

# Show the plot
plt.show()