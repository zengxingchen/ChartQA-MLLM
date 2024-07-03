
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [123, 150, 200, 165, 180, 175, 190, 160, 170, 185, 210, 195]
}

# Create DataFrame
df = pd.DataFrame(data)

# seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = ['#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600', '#a50026', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(12, 8))

# Plot the Sales
sns.barplot(x="Sales", y="Month", data=df, palette=palette)

# Customize the axes and title
ax.set_xlabel('Monthly Sales')
ax.set_ylabel('Month')
ax.set_title('Monthly Sales Data Visualization')

# Show values on bars
for p in ax.patches:
    width = p.get_width()
    plt.text(5+p.get_width(), p.get_y()+0.55*p.get_height(),
             '{:1.0f}'.format(width),
             ha='center', va='center')

# Set the band width
ax.bar_label(ax.containers[0], label_type='center')

# Set the margins
plt.subplots_adjust(left=0.15, right=0.95, top=0.9, bottom=0.1)

# Show the plot
plt.show()