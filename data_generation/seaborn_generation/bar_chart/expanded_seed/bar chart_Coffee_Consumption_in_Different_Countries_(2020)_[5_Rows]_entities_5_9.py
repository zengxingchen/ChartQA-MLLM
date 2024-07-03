
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data provided in table format
data = [{'Country': 'Finland', 'Cups per Capita': 1298},
        {'Country': 'Netherlands', 'Cups per Capita': 723},
        {'Country': 'Slovenia', 'Cups per Capita': 621},
        {'Country': 'Sweden', 'Cups per Capita': 516},
        {'Country': 'Canada', 'Cups per Capita': 360}]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Initialize a seaborn style
sns.set_style("whitegrid")

# Create a color palette for the bar chart
palette = sns.color_palette("husl", len(df))

# Create the bar chart
plt.figure(figsize=(10, 6))
barplot = sns.barplot(x='Country', y='Cups per Capita', data=df, palette=palette)

# Annotate each bar with the value of cups per capita
for p in barplot.patches:
    barplot.annotate(format(p.get_height(), '.1f'), 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha = 'center', va = 'center', 
                     xytext = (0, 9), 
                     textcoords = 'offset points')

# Set the title and labels for the axes
plt.title('Coffee Consumption: Cups per Capita by Country', fontsize=16)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Cups per Capita', fontsize=12)

# Increase the bottom margin to fit the x-axis labels
plt.tight_layout()

# Show the plot
plt.show()