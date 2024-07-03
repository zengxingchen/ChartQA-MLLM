
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data: Average Monthly Temperature of Various Cities
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 
             'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 'Charlotte'],
    'Average_Temperature': [3, 13, 1, 12, 15, 2, 16, 14, 11, 10, 17, 19, 12, 4, 8]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 8))

# Custom color palette
palette = ['#3366cc', '#dc3912', '#ff9900', '#109618', '#990099', '#0099c6', 
           '#dd4477', '#66aa00', '#b82e2e', '#316395', '#994499', '#22aa99', 
           '#aaaa11', '#6633cc', '#e67300']

# Plot a horizontal bar chart
sns.barplot(x='Average_Temperature', y='City', data=df,
            palette=palette, orient='h', ax=ax, dodge=False)

# Customize the Axes
ax.set(xlim=(0, 20), ylabel="City", xlabel="Average Monthly Temperature (°C)")
ax.set_title('Average Monthly Temperature of Various Cities')

# Adjust bar width/height
for container in ax.containers:
    ax.bar_label(container, label_type='edge', padding=3)

plt.show()