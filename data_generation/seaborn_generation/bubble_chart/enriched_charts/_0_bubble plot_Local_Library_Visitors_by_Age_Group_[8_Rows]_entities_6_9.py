
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India',
                'United Kingdom', 'France', 'Brazil', 'Canada', 'Russia',
                'Australia', 'South Korea', 'Italy', 'Mexico', 'Spain'],
    'GDP_Trillion': [21.43, 14.34, 5.08, 3.86, 2.87, 2.83, 2.72, 1.84, 1.73, 1.70, 1.39, 1.63, 2.00, 1.22, 1.39],
    'Renewable_Production': [2.5, 3.0, 0.5, 0.9, 0.8, 0.7, 0.6, 1.2, 0.9, 0.1, 0.5, 0.3, 0.4, 0.7, 0.6],
    'Total_Energy_Consumption': [100, 120, 40, 30, 60, 20, 25, 15, 15, 70, 25, 30, 35, 30, 20],
    'Population_Millions': [331, 1441, 126, 83, 1380, 68, 65, 213, 38, 146, 25, 52, 60, 129, 47]
})

# calculate per capita energy consumption
data['Energy_Per_Capita'] = data['Total_Energy_Consumption'] / data['Population_Millions']

# size for bubble
data['Renewable_Ratio'] = data['Renewable_Production'] / data['Total_Energy_Consumption']

# Set style
sns.set(style='whitegrid')

# Create the bubble chart
plt.figure(figsize=(14, 10))
bubble = sns.scatterplot(data=data, x='GDP_Trillion', y='Energy_Per_Capita',
                         size='Renewable_Ratio', hue='Renewable_Ratio',
                         palette=['#FF5733','#33FF57','#3357FF','#FF33FB'],
                         legend=False, alpha=0.7, sizes=(20, 2000))

# Adjust the labels and title
plt.xlabel('GDP in Trillions of USD')
plt.ylabel('Energy Consumption Per Capita (tonnes of oil equivalent)')
plt.title('Energy Profile of Countries')

# Show the plot
plt.show()