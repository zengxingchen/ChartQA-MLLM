
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Manufacturer': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Lenovo', 'LG', 'Motorola', 'Nokia'],
    'Sales': [321.2, 215.8, 150.3, 125.6, 111.8, 95.2, 72.3, 55.1, 45.4, 23.5]
}

df = pd.DataFrame(data)

# Colors
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]

# Pie chart
plt.figure(figsize=(10, 8))
plt.pie(df['Sales'], labels=df['Manufacturer'], colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Global Smartphone Sales by Manufacturer (Million Units)')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()