
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Platform': ['PlayStation', 'Xbox', 'PC', 'Nintendo Switch', 'Mobile', 'VR', 'Others'],
    'Count': [320, 240, 450, 165, 325, 50, 150]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define the color palette for the pie chart
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#C0C0C0', '#8A2BE2']

# Plot
plt.figure(figsize=(10, 8))
plt.pie(df['Count'], labels=df['Platform'], colors=colors, startangle=140, autopct='%1.1f%%')

# Title
plt.title('Survey on Preferred Gaming Platforms')

# Display the chart
plt.show()