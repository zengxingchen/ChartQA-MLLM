
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Given data for the smartphone market share
data = {
    'Company': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Vivo', 'Others'],
    'Market Share': [19.2, 15.7, 14.1, 8.9, 8.3, 7.4, 26.4]
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Set the color palette to use specific colors
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7']

# Create the pie chart with custom size
plt.figure(figsize=(10, 6))
plt.pie(df['Market Share'], labels=df['Company'], autopct='%1.1f%%', colors=colors, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Set plot title
plt.title('Smartphone Market Share (2023)')

# Display the pie chart
plt.show()