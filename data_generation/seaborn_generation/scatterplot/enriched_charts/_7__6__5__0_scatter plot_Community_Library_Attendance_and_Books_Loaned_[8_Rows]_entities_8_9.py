
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'Country': ['USA', 'Canada', 'Germany', 'France', 'UK', 'Japan', 'Australia', 'Italy', 'Spain', 'South Korea', 'China', 'India', 'Brazil', 'Russia', 'Mexico', 'Nigeria', 'South Africa'],
    'Average_Daily_Study_Hours': [5, 6, 7, 5.5, 6.5, 8, 5.2, 6.8, 6, 9, 8.5, 7.5, 4.8, 6.3, 5.4, 4.5, 4.2],
    'Graduation_Rate_Percentage': [85, 88, 90, 87, 89, 95, 86, 88, 87, 97, 96, 93, 82, 89, 84, 80, 78]
}

df = pd.DataFrame(data)

# Plotting the scatterplot
plt.figure(figsize=(16, 12))
scatterplot = sns.scatterplot(data=df, x='Average_Daily_Study_Hours', y='Graduation_Rate_Percentage', palette=['#FF5733', '#33FFCE'])

scatterplot.set_title('Average Daily Study Hours vs. Graduation Rate by Country', fontsize=18)
scatterplot.set_xlabel('Average Daily Study Hours', fontsize=16)
scatterplot.set_ylabel('Graduation Rate (%)', fontsize=16)
plt.show()