
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Table data provided
data = [
    {'Day': 'Monday', 'Steps': 7524},
    {'Day': 'Tuesday', 'Steps': 8472},
    {'Day': 'Wednesday', 'Steps': 9631},
    {'Day': 'Thursday', 'Steps': 7239},
    {'Day': 'Friday', 'Steps': 6689}
]

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Create a line plot, we use 'lineplot' function from Seaborn for the line
line = sns.lineplot(data=df, x='Day', y='Steps', sort=False, marker='o', color='skyblue')

# Now, let's fill the area under the line to create an area plot effect
# We'll use the 'fill_between' function from Matplotlib
plt.fill_between(x=df['Day'], y1=df['Steps'], color='skyblue', alpha=0.3)

# Enhance the visualization with diversified visual encoding
# Let's set the title and labels with custom font sizes
plt.title('Steps by Day', fontsize=16)
plt.xlabel('Day of the Week', fontsize=12)
plt.ylabel('Number of Steps', fontsize=12)

# Adding the actual data points as annotations on the chart
for x, y in zip(df['Day'], df['Steps']):
    plt.text(x, y, f'{y}', ha='center', va='bottom')

# Customize the x and y axis limits to provide better visual appeal
plt.ylim(0, df['Steps'].max() + 1000)
plt.xlim(-0.5, len(df['Day']) - 0.5)

# Remove the top and right spines
sns.despine()

# Display the plot
plt.show()