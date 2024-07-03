
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the data is in a CSV file named 'ev_sales_data.csv'
data = {
    'Country': ['United States', 'China', 'Germany', 'Norway', 'France', 'United Kingdom', 
                'Netherlands', 'Canada', 'Sweden', 'Italy', 'Japan', 'South Korea'],
    'Battery Capacity (GWh)': [100, 500, 70, 30, 60, 55, 25, 45, 20, 35, 80, 50],
    'EV Sales (Thousands)': [400, 1200, 300, 150, 250, 200, 100, 150, 80, 140, 220, 190],
    'CO2 Reduction (Million Tonnes)': [70, 200, 45, 15, 40, 33, 13, 25, 11, 23, 50, 32]
}

# Convert the data dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create the bubble chart
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(data=df, 
                               x='EV Sales (Thousands)', 
                               y='Battery Capacity (GWh)', 
                               size='CO2 Reduction (Million Tonnes)', 
                               hue='Country', 
                               palette=["#f46d43", "#d73027", "#fdae61", "#fee08b", 
                                        "#e0f3f8", "#abd9e9", "#74add1", "#4575b4",
                                        "#313695", "#a50026", "#d73027", "#f46d43"],
                               sizes=(20, 2000))

plt.title('Global EV Sales vs Battery Capacity and CO2 Reduction Potential')
plt.xlabel('EV Sales (Thousands)')
plt.ylabel('Battery Capacity (GWh)')

# Adjust legend
bubble_chart.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Country')

# Show the plot
plt.show()