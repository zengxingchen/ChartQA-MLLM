
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Country': ['United States', 'Canada', 'Germany', 'United Kingdom', 'France', 
                'Japan', 'Australia', 'China', 'India', 'Brazil', 
                'Russia', 'South Korea', 'Italy', 'Mexico', 'Spain'],
    'Healthcare_Expenditure_Per_Capita': [10223, 4974, 5986, 4070, 4968, 
                                          4751, 5195, 527, 74, 947, 
                                          1410, 2829, 3656, 1041, 3100],
    'Life_Expectancy': [78.8, 82.3, 81.0, 81.2, 82.5, 
                        84.6, 83.4, 76.7, 69.4, 75.7, 
                        72.6, 83.3, 83.2, 75.0, 83.4],
    'Healthcare_Percentage_of_GDP': [16.9, 10.7, 11.7, 10.0, 11.2, 
                                     10.9, 9.3, 5.4, 3.5, 9.2, 
                                     5.3, 8.1, 8.8, 5.4, 9.0],
    'Population_Millions': [331, 38, 83, 68, 65, 
                            126, 25, 1441, 1380, 213, 
                            146, 52, 60, 129, 47]
})

# Calculate Healthcare Expenditure Ratio
data['Healthcare_Ratio'] = data['Healthcare_Percentage_of_GDP'] / data['Life_Expectancy']

# Set style
sns.set(style='whitegrid')

# Create the bubble chart
plt.figure(figsize=(16, 12))
bubble = sns.scatterplot(data=data, x='Healthcare_Expenditure_Per_Capita', y='Life_Expectancy',
                         size='Healthcare_Ratio', hue='Healthcare_Ratio',
                         palette=['#1f77b4','#ff7f0e','#2ca02c','#d62728'],
                         legend='brief', alpha=0.7, sizes=(100, 2000))

# Adjust the labels and title
plt.xlabel('Healthcare Expenditure Per Capita (USD)')
plt.ylabel('Life Expectancy (years)')
plt.title('Healthcare Expenditure vs Life Expectancy')

# Show the plot
plt.show()