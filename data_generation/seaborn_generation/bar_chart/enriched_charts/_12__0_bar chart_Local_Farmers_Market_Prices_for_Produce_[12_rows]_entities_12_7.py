
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data = {
    'Country': ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan', 'Ethiopia', 'Philippines', 'Egypt', 'Vietnam'],
    'Population (millions)': [1402, 1366, 331, 273, 220, 213, 206, 164, 146, 128, 126, 115, 110, 102, 97]
}

df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 15))
sns.barplot(y='Population (millions)', x='Country', data=df, palette=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "#1f78b4", "#ff79b4", "#79b4ff", "#b4ff79", "#ffb479"], linewidth=1.2)

# Customize the chart
plt.title('Population Distribution by Country', fontsize=15)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population (millions)', fontsize=12)
plt.grid(axis='y', linestyle='--', linewidth=0.7)

# Show the plot
plt.show()