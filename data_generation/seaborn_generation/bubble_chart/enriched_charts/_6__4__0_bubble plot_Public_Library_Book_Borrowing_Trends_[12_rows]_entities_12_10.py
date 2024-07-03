
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Company': ['Apple', 'Microsoft', 'Amazon', 'Google', 'Facebook', 'Tesla', 'Nvidia', 'Samsung', 'Intel', 
                'IBM', 'Cisco', 'Adobe', 'Oracle', 'SAP', 'Salesforce', 'Uber', 'Lyft', 'Spotify', 
                'Netflix', 'Twitter'],
    'Avg_Annual_Growth_Rate': [12, 15, 25, 18, 20, 35, 30, 10, 8, 5, 7, 14, 6, 9, 23, 40, 38, 30, 24, 19],
    'Profit_Margin': [21, 18, 7, 20, 29, 10, 26, 8, 22, 4, 20, 40, 28, 17, 15, 6, 3, 4, 16, 5],
    'Employee_Count': [154000, 181000, 1600000, 156500, 86000, 99000, 20000, 287439, 121100, 345900, 83000, 26000, 
                       132000, 102430, 73541, 32000, 10000, 8200, 12300, 7500]
})

sns.set(style="whitegrid")
palette = sns.color_palette(["#4daf4a", "#377eb8", "#ff7f00", "#e41a1c", "#984ea3", "#f781bf", "#999999", "#a65628", "#fdae61", "#e6f598"])

plt.figure(figsize=(18, 14))
bubble = sns.scatterplot(x="Avg_Annual_Growth_Rate", y="Profit_Margin", size="Employee_Count",
                         sizes=(100, 2500), hue="Company", palette=palette, data=data, legend=True)

plt.title('Company Performance Metrics: Growth Rate vs Profit Margin', fontsize=22)
plt.xlabel('Average Annual Growth Rate (%)', fontsize=18)
plt.ylabel('Profit Margin (%)', fontsize=18)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True, color='gray', linestyle='--', linewidth=0.5)

plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Company')
plt.show()