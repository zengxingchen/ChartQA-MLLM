
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Day': 'Monday', 'Revenue ($)': 500},
    {'Day': 'Tuesday', 'Revenue ($)': 630},
    {'Day': 'Wednesday', 'Revenue ($)': 470},
    {'Day': 'Thursday', 'Revenue ($)': 560},
    {'Day': 'Friday', 'Revenue ($)': 690}
]

# Convert the data to a DataFrame for Seaborn
import pandas as pd
df = pd.DataFrame(data)

# Set the visual aesthetics for the plot
sns.set_theme(style="whitegrid")

# Creating the bar plot
bar_plot = sns.barplot(
    x='Day', 
    y='Revenue ($)', 
    data=df,
    palette='viridis',     # Use a diversified color palette
    edgecolor='black',     # Adds a black edge color to the bars
    linewidth=1.5,         # Specifies the line width of the bar edges
    saturation=0.7         # Adjusts the saturation of the colors
)

# Adding additional visual details
bar_plot.set_title('Revenue by Day of the Week', fontsize=16) # Sets the title of the plot
bar_plot.set_xlabel('Day', fontsize=14)                       # Sets the label for the x-axis
bar_plot.set_ylabel('Revenue ($)', fontsize=14)               # Sets the label for the y-axis

# Rotate the x-axis labels for better readability
plt.setp(bar_plot.get_xticklabels(), rotation=45)

# Show the values on top of the bars
for p in bar_plot.patches:
    bar_plot.annotate(
        format(p.get_height(), '.1f'), 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha = 'center', va = 'center', 
        xytext = (0, 9), 
        textcoords = 'offset points'
    )

plt.tight_layout()
plt.show()