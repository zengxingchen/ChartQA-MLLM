
import matplotlib.pyplot as plt
import seaborn as sns

# Data
brand_data = {
    'Brand': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Vivo', 'Others'],
    'Market Share': [20.5, 19.2, 13.8, 12.6, 10.2, 9.1, 14.6]
}

# Colors (using seaborn to generate a color palette)
palette = sns.color_palette(["#2c7bb6", "#00ccbc", "#d7191c", "#fdae61", "#abd9e9", "#ffffbf", "#1a9641"])
sns.set_palette(palette)

# Pie chart
plt.figure(figsize=(8, 8))  # Width and height of the chart
plt.pie(brand_data['Market Share'], labels=brand_data['Brand'], autopct='%1.1f%%', colors=palette)
plt.title('Smartphone Market Share in 2023')
plt.show()