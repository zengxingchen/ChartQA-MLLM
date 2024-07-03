
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'City': ['London', 'New York', 'Los Angeles', 'Tokyo', 'Paris', 'Berlin', 'Moscow', 'Beijing', 'Sydney', 'Rio de Janeiro', 'Cairo', 'Mumbai'],
    'Life_Expectancy': [81, 79, 80, 84, 82, 81, 76, 75, 83, 74, 71, 68],
    'Physical_Activity_Level': [40, 35, 50, 60, 55, 45, 30, 20, 70, 25, 15, 10]
}

df = pd.DataFrame(data)

# Plotting the scatterplot
plt.figure(figsize=(12, 8))
scatterplot = sns.scatterplot(data=df, x='Life_Expectancy', y='Physical_Activity_Level', palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

scatterplot.set_title('Life Expectancy and Physical Activity Level by City')
scatterplot.set_xlabel('Life Expectancy (years)')
scatterplot.set_ylabel('Physical Activity Level (%)')
plt.show()