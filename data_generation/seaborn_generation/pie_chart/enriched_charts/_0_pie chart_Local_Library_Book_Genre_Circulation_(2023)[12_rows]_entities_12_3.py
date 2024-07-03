
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Brand': ['Samsung', 'Apple', 'Xiaomi', 'OPPO', 'Vivo', 'Huawei', 'Others'],
    'Market Share': [31, 22, 12, 9, 8, 5, 13]
}

# Create DataFrame
df = pd.DataFrame(data)

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']

# Plotting pie chart with a given height and width
plt.figure(figsize=(10, 8))
plt.pie('Market Share', labels='Brand', data=df, colors=colors, autopct='%1.1f%%')

# Title
plt.title('Global Smartphone Market Share in 2022')

# Display the pie chart
plt.show()