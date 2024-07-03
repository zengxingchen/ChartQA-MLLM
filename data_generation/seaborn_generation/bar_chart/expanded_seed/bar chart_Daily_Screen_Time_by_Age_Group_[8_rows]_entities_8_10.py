
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your chart table data
data = [
    {'Age Group': '0-5', 'Average Screen Time (hours)': 1.5},
    {'Age Group': '6-12', 'Average Screen Time (hours)': 2.5},
    {'Age Group': '13-18', 'Average Screen Time (hours)': 4.5},
    {'Age Group': '19-35', 'Average Screen Time (hours)': 7.0},
    {'Age Group': '36-50', 'Average Screen Time (hours)': 5.5},
    {'Age Group': '51-65', 'Average Screen Time (hours)': 4.0},
    {'Age Group': '66-80', 'Average Screen Time (hours)': 3.0},
    {'Age Group': '81+', 'Average Screen Time (hours)': 2.0}
]

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Set the style and color palette of the seaborn chart
sns.set(style="whitegrid")
palette = sns.color_palette("coolwarm", len(data))

# Create the bar chart
plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    x="Age Group",
    y="Average Screen Time (hours)",
    data=df,
    palette=palette
)

# Add title and labels to the plot
plt.title("Average Screen Time by Age Group", size=16)
plt.xlabel("Age Group", size=14)
plt.ylabel("Average Screen Time (hours)", size=14)

# Add the values on top of each bar for better readability
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha = 'center', va = 'center', 
                     xytext = (0, 9), 
                     textcoords = 'offset points')

# Show the plot
plt.show()