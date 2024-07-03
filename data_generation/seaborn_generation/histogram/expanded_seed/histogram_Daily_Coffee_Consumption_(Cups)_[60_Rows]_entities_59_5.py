
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your provided data
data = [
    {'Daily Coffee Cups': 2}, {'Daily Coffee Cups': 4},
    {'Daily Coffee Cups': 1}, {'Daily Coffee Cups': 0},
    {'Daily Coffee Cups': 3}, {'Daily Coffee Cups': 2},
    {'Daily Coffee Cups': 1}, {'Daily Coffee Cups': 1},
    {'Daily Coffee Cups': 5}, {'Daily Coffee Cups': 4},
    {'Daily Coffee Cups': 0}, {'Daily Coffee Cups': 2},
    {'Daily Coffee Cups': 1}, {'Daily Coffee Cups': 3},
    {'Daily Coffee Cups': 1}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Set style and color palette for Seaborn
sns.set(style="whitegrid")
sns.set_palette("husl")

# Create the histogram using Seaborn
plt.figure(figsize=(10, 6)) # Set the size of the figure

# Histplot
hist_plot = sns.histplot(df['Daily Coffee Cups'], kde=False, bins=6, color='purple', edgecolor='black')

# Enhancements
hist_plot.set_title('Daily Coffee Cups Histogram', fontsize=16) # Title
hist_plot.set_xlabel('Number of Coffee Cups', fontsize=14) # X-label
hist_plot.set_ylabel('Frequency', fontsize=14) # Y-label

for p in hist_plot.patches: # Add annotation to bars
    hist_plot.annotate(f"{int(p.get_height())}",
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'center',
                xytext = (0, 9), 
                textcoords = 'offset points')

plt.show()