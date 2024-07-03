
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Company': ['Samsung', 'Apple', 'Xiaomi', 'Oppo', 'Vivo', 'Huawei', 'Realme', 'Lenovo', 'LG', 'Nokia', 'Others'],
    'Shipments': [75.1, 59.9, 40.5, 31.6, 26.5, 18.4, 15.7, 12.3, 8.3, 5.8, 95.8],
    'MarketShare': [21.2, 16.9, 11.4, 8.9, 7.5, 5.2, 4.4, 3.5, 2.3, 1.6, 27.1],
    'Revenue': [54.2, 65.6, 8.5, 6.7, 6.2, 5.1, 2.8, 2.9, 1.7, 0.4, 12.3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 10))
bubble = sns.scatterplot(data=df, x='MarketShare', y='Shipments', size='Revenue', hue='Company', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#57FFC1', '#FFD133', '#8333FF', '#33FFF7', '#FF335B', '#FF9733', '#737373'], sizes=(20, 1000), alpha=0.7, edgecolor='black')

plt.title('Global Smartphone Shipments and Market Share by Company', fontsize=16)
plt.xlabel('Market Share (%)', fontsize=12)
plt.ylabel('Shipments (Millions)', fontsize=12)

# Customize legend
hand, labl = bubble.get_legend_handles_labels()
bubble.legend(hand[1:], labl[1:], title='Company', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()