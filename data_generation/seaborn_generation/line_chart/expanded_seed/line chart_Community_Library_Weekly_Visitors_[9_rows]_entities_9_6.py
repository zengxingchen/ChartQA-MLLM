
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# The given chart table data
data = [
    {'Week': '2023-W01', 'Children': 80, 'Adults': 120, 'Seniors': 40},
    {'Week': '2023-W02', 'Children': 105, 'Adults': 110, 'Seniors': 55},
    {'Week': '2023-W03', 'Children': 95, 'Adults': 130, 'Seniors': 35},
    {'Week': '2023-W04', 'Children': 100, 'Adults': 140, 'Seniors': 45},
    {'Week': '2023-W05', 'Children': 110, 'Adults': 150, 'Seniors': 50},
    {'Week': '2023-W06', 'Children': 120, 'Adults': 160, 'Seniors': 60},
    {'Week': '2023-W07', 'Children': 115, 'Adults': 155, 'Seniors': 65},
    {'Week': '2023-W08', 'Children': 130, 'Adults': 170, 'Seniors': 70},
    {'Week': '2023-W09', 'Children': 125, 'Adults': 175, 'Seniors': 75}
]

# Convert the chart table data into a pandas DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format suitable for seaborn.lineplot
df_long = df.melt(id_vars='Week', var_name='Category', value_name='Count')

# Create a lineplot with Seaborn
sns.set_theme(style='whitegrid')
plt.figure(figsize=(10, 6))

# Generate the line plot with diversification in terms of style and markers
sns.lineplot(data=df_long, x='Week', y='Count', hue='Category', style='Category', 
             palette='tab10', markers=True, dashes=False)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Set plot title and labels
plt.title('Weekly Counts by Category')
plt.xlabel('Week')
plt.ylabel('Count')

# Show a legend
plt.legend(title='Category')

# Adjust plot to prevent cutting off labels
plt.tight_layout()

# Display the plot
plt.show()