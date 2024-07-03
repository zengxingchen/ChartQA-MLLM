
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Country': ['United States', 'China', 'Germany', 'Norway', 'France', 'United Kingdom', 
                'Netherlands', 'Canada', 'Sweden', 'Italy', 'Japan', 'South Korea',
                'Australia', 'Brazil', 'India'],
    'Battery Capacity (GWh)': [100, 500, 75, 30, 65, 55, 28, 48, 20, 37, 85, 52, 42, 60, 70],
    'Mental Health Index': [80, 85, 78, 88, 82, 75, 83, 79, 90, 74, 77, 81, 76, 80, 70],
    'CO2 Reduction (Million Tonnes)': [70, 200, 45, 15, 40, 33, 13, 25, 11, 23, 50, 32, 27, 35, 38]
}

df = pd.DataFrame(data)

plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df, 
                               x='Mental Health Index', 
                               y='Battery Capacity (GWh)', 
                               size='CO2 Reduction (Million Tonnes)', 
                               hue='Country', 
                               palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", 
                                        "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
                                        "#bcbd22", "#17becf", "#1f77b4", "#ff7f0e",
                                        "#2ca02c", "#d62728", "#9467bd"],
                               sizes=(20, 2000))

plt.title('Mental Health Index vs Battery Capacity and CO2 Reduction')
plt.xlabel('Mental Health Index')
plt.ylabel('Battery Capacity (GWh)')

bubble_chart.legend(loc='upper right', bbox_to_anchor=(1.2, 1), title='Country')

plt.show()