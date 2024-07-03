
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [120, 135, 190, 175, 185, 160, 195, 170, 180, 200, 205, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

# seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFF6', '#FF8C33', '#A633FF', '#57FF33', '#FF3357', '#33FF8C', '#8C33FF', '#F633FF']

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Plot the Sales
sns.barplot(x="Month", y="Sales", data=df, palette=palette)

# Customize the axes and title
ax.set_xlabel('Month')
ax.set_ylabel('Monthly Sales')
ax.set_title('Monthly Sales Data Visualization', fontsize=16)

# Show values on bars
for p in ax.patches:
    height = p.get_height()
    plt.text(p.get_x() + p.get_width() / 2., height,
             '{:1.0f}'.format(height),
             ha='center', va='bottom')

# Set the band height
ax.bar_label(ax.containers[0], label_type='center')

# Set the margins
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.2)

# Show the plot
plt.show()