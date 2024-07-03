
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Creating a DataFrame from the provided data
data = {
    'Category': ['Education', 'Healthcare', 'Infrastructure', 'Research', 'Defense', 'Environment', 'Social Welfare'],
    'Value': [300, 250, 400, 150, 350, 200, 300]
}

df = pd.DataFrame(data)

# Determine the colors for each category, using specific hex color codes
colors = ['#e6194B', '#f58231', '#ffe119', '#bfef45', '#3cb44b', '#42d4f4', '#4363d8']

# Plotting using Seaborn's pie chart capabilities through Matplotlib's pie function
plt.figure(figsize=(8, 8))  # Adjusting the figure size
plt.pie(df['Value'], labels=df['Category'], colors=colors, autopct='%1.1f%%', startangle=140)

# Adding a title to the chart
plt.title('Government Budget Allocation by Category', pad=20)

# Display the chart
plt.show()