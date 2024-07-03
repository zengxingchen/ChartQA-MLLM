
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data = [
    {'Day': 'Monday', 'Minutes of Exercise': 30},
    {'Day': 'Tuesday', 'Minutes of Exercise': 45},
    {'Day': 'Wednesday', 'Minutes of Exercise': 20},
    {'Day': 'Thursday', 'Minutes of Exercise': 50},
    {'Day': 'Friday', 'Minutes of Exercise': 15}
]

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a figure and one subplot
fig, ax = plt.subplots()

# Create a color palette
palette = sns.color_palette("husl", 5)

# Sort DataFrame by 'Day' to ensure the area chart is in order
df['Day'] = pd.Categorical(df['Day'], categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], ordered=True)
df.sort_values('Day', inplace=True)

# FacetGrid for diverse hues across different days
g = sns.FacetGrid(df, hue='Day', palette=palette, height=5, aspect=1.5)

# Map the lineplot across the FacetGrid and use the 'ax' from subplots
g.map(sns.lineplot, 'Day', 'Minutes of Exercise', estimator=None)

# Now we fill the area under the line using `fill_between`
days = range(len(df['Day']))  # Convert days to numerical values for fill_between
ax.fill_between(days, 0, df['Minutes of Exercise'], color=palette[0], alpha=0.3)

# Optionally, set the limits for the y-axis
ax.set_ylim(0, 60)

# Set the title of the chart
ax.set_title('Minutes of Exercise by Day')

# Enhance the legend
g.add_legend(title="Day")

# Display the plot
plt.show()