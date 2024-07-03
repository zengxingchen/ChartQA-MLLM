
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = [
    {'Hour of Day': '6 AM', ' Weekday Visitors': 5, ' Weekend Visitors': 15},
    {'Hour of Day': '7 AM', ' Weekday Visitors': 10, ' Weekend Visitors': 25},
    {'Hour of Day': '8 AM', ' Weekday Visitors': 15, ' Weekend Visitors': 35},
    {'Hour of Day': '9 AM', ' Weekday Visitors': 20, ' Weekend Visitors': 40},
    {'Hour of Day': '10 AM', ' Weekday Visitors': 25, ' Weekend Visitors': 50},
    {'Hour of Day': '11 AM', ' Weekday Visitors': 40, ' Weekend Visitors': 60},
    {'Hour of Day': '12 PM', ' Weekday Visitors': 55, ' Weekend Visitors': 70},
    {'Hour of Day': '1 PM', ' Weekday Visitors': 65, ' Weekend Visitors': 85},
    {'Hour of Day': '2 PM', ' Weekday Visitors': 75, ' Weekend Visitors': 95},
    {'Hour of Day': '3 PM', ' Weekday Visitors': 80, ' Weekend Visitors': 110},
    {'Hour of Day': '4 PM', ' Weekday Visitors': 90, ' Weekend Visitors': 120},
    {'Hour of Day': '5 PM', ' Weekday Visitors': 100, ' Weekend Visitors': 130}
]

# Create DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to format it for sns.scatterplot
df_melted = df.melt(id_vars='Hour of Day', var_name='Type', value_name='Visitors')

# Plotting
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

scatter = sns.scatterplot(
    data=df_melted,
    x='Hour of Day',
    y='Visitors',
    hue='Type',
    style='Type',
    size='Type',
    sizes=(50, 100),
    palette='deep',
    markers=['o', 's']
)

# Improve the legend
handles, labels = scatter.get_legend_handles_labels()
scatter.legend(handles=handles[1:], labels=labels[1:], title='Visitor Type')

plt.title('Visitor Count by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Visitors')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()