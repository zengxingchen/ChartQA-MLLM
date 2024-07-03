
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Calories Burned': [300, 350, 400, 370, 390, 360, 420, 380, 410, 430, 440, 450]
}

# Create DataFrame
df = pd.DataFrame(data)

# seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e']

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(14, 8))

# Plot the Calories Burned
sns.barplot(y="Month", x="Calories Burned", data=df, palette=palette, ci=None)

# Customize the axes and title
ax.set_ylabel('Month')
ax.set_xlabel('Calories Burned')
ax.set_title('Monthly Calories Burned Data Visualization', fontsize=18)

# Show values on bars
for p in ax.patches:
    width = p.get_width()
    plt.text(width, p.get_y() + p.get_height() / 2., '{:1.0f}'.format(width), ha='left', va='center')

# Adjust the bar label position
ax.bar_label(ax.containers[0], label_type='center')

# Set the margins
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)

# Show the plot
plt.show()