
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'Country': ['USA', 'Canada', 'Germany', 'France', 'UK', 'Japan', 'Australia', 'Italy', 'Spain', 'South Korea', 'China', 'India', 'Brazil', 'Russia', 'Mexico', 'Nigeria', 'South Africa'],
    'Average_Daily_Fruit_Consumption_g': [130, 150, 160, 180, 140, 200, 135, 190, 185, 210, 220, 230, 145, 125, 110, 90, 100],
    'Obesity_Rate_Percentage': [36.2, 29.4, 23.1, 21.6, 27.8, 4.3, 30.4, 19.9, 23.8, 4.7, 6.2, 3.9, 22.1, 26.2, 28.9, 11.2, 26.6]
}

df = pd.DataFrame(data)

# Plotting the scatterplot
plt.figure(figsize=(14, 10))
scatterplot = sns.scatterplot(data=df, x='Average_Daily_Fruit_Consumption_g', y='Obesity_Rate_Percentage', palette=['#FF6347', '#4682B4'])

scatterplot.set_title('Average Daily Fruit Consumption vs. Obesity Rate by Country', fontsize=16)
scatterplot.set_xlabel('Average Daily Fruit Consumption (g)', fontsize=14)
scatterplot.set_ylabel('Obesity Rate (%)', fontsize=14)
plt.show()