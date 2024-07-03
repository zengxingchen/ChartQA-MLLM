
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data: Market share of major smartphone brands in 2022
data = {
    'Brand': ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OPPO', 'Others'],
    'Market Share': [21, 16, 15, 14, 10, 24]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define colors for each brand
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Create the pie chart using matplotlib since seaborn doesn't natively support pie charts
plt.figure(figsize=(8, 6))
plt.pie(df['Market Share'], labels=df['Brand'], colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Global Smartphone Market Share in 2022')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()