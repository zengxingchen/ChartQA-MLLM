
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the above CSV data
data = {
    'Company': ['Apple', 'Samsung', 'Xiaomi', 'Oppo', 'Vivo', 'Huawei', 'Lenovo', 'LG', 'Motorola', 'Nokia'],
    'SalesUnits': [220.4, 320.1, 145.8, 111.7, 95.8, 75.7, 45.6, 20.3, 18.6, 16.4],
    'MarketShare': [25.3, 18.2, 14.5, 10.4, 8.9, 6.7, 4.2, 1.9, 1.8, 1.5],
    'Revenue': [365.8, 283.9, 125.7, 91.2, 69.5, 52.4, 30.7, 13.8, 11.3, 10.2]
}
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 8))

# Create the bubble chart
bubble = sns.scatterplot(data=df, x='MarketShare', y='SalesUnits', size='Revenue', 
                         hue='Company', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
                                                 '#33FFFB', '#FFFB33', '#FBFF33', '#837FF3',
                                                 '#8FF73F', '#3FF786'],
                         sizes=(20, 1000), alpha=0.7, edgecolor='w', linewidth=1)
bubble.set_title('Global Smartphone Sales by Company in 2022', weight='bold', size=16)
bubble.set_xlabel('Market Share (%)', weight='bold', size=12)
bubble.set_ylabel('Sales Units (in millions)', weight='bold', size=12)

# Adjust legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.show()