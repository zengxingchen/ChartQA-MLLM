
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = [
    {'Age Group': 'Children (0-14)', 'Number of Visitors': 120},
    {'Age Group': 'Youth (15-25)', 'Number of Visitors': 95},
    {'Age Group': 'Adults (26-64)', 'Number of Visitors': 130},
    {'Age Group': 'Seniors (65+)', 'Number of Visitors': 40}
]

# Convert the list of dictionaries into a pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create a scatterplot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(data=df, x='Age Group', y='Number of Visitors', s=100)

# Custom mappings for colors based on Age Group
palette = {'Children (0-14)': 'r', 'Youth (15-25)': 'g', 'Adults (26-64)': 'b', 'Seniors (65+)': 'y'}
scatterplot = sns.scatterplot(data=df, 
                              x='Age Group', 
                              y='Number of Visitors', 
                              hue='Age Group', 
                              palette=palette,
                              s=100)

# Annotate each point with the number of visitors
for line in range(0, df.shape[0]):
    scatterplot.text(df['Age Group'][line], df['Number of Visitors'][line], 
                     '  ' + str(df['Number of Visitors'][line]), 
                     horizontalalignment='left', 
                     size='medium', color='black')

# Show plot with legend and proper layout
plt.legend(title='Age Group')
plt.title('Number of Visitors by Age Group')
plt.tight_layout()
plt.show()