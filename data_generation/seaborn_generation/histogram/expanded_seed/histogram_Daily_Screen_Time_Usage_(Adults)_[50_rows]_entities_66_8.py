
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Given chart data
chart_data = [
    {'Age Group': '18-24', 'Hours per Day': 3.6},
    {'Age Group': '25-34', 'Hours per Day': 4.5},
    {'Age Group': '35-44', 'Hours per Day': 3.1},
    {'Age Group': '45-54', 'Hours per Day': 4.2},
    {'Age Group': '55-64', 'Hours per Day': 5.3},
    {'Age Group': '65+', 'Hours per Day': 6.1},
    {'Age Group': '18-24', 'Hours per Day': 5.7},
    {'Age Group': '25-34', 'Hours per Day': 6.4},
    {'Age Group': '35-44', 'Hours per Day': 2.9},
    {'Age Group': '45-54', 'Hours per Day': 3.8},
    {'Age Group': '55-64', 'Hours per Day': 4.1},
    {'Age Group': '65+', 'Hours per Day': 6.3},
    {'Age Group': '18-24', 'Hours per Day': 2.4},
    {'Age Group': '25-34', 'Hours per Day': 5.8},
    {'Age Group': '35-44', 'Hours per Day': 3.5}
]

# Convert the chart data to a DataFrame
df = pd.DataFrame(chart_data)

# Set up the seaborn theme and color palette for better aesthetics
sns.set_theme(style="whitegrid")
palette = sns.color_palette("pastel")

# Create the histogram using displot
sns.displot(
    data=df,
    x='Hours per Day',
    hue='Age Group',
    palette=palette,
    kind='hist',
    kde=True,  # Adds Kernel Density Estimate to smooth the distribution
    multiple='stack',  # Stacks the histograms
    shrink=0.8,  # Controls the width of the bars
    binwidth=0.5,  # Set the width of the bins of the histogram
    edgecolor='black',  # Color for the edges of the bars
    linewidth=1.5  # Width of the edge lines
)

# Set up labels and titles
plt.xlabel('Hours per Day', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Distribution of Hours per Day by Age Group', fontsize=12)

# Improve layout
plt.tight_layout()

# Show the plot
plt.show()