
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Topic': ['Galileo Galilei', 'Johannes Kepler', 'Isaac Newton', 'Edwin Hubble', 
              'Stephen Hawking', 'Carl Sagan', 'Neil deGrasse Tyson', 'Vera Rubin'],
    'Value': [1564, 1571, 1643, 1889, 1942, 1934, 1958, 1928]
}

# Create DataFrame
df = pd.DataFrame(data)

# seaborn style
sns.set_theme(style="whitegrid")

# Create a color palette
palette = ['#1b9e77', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#e6ab02', '#a6761d', '#666666']

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 6))

# Plot the Values
sns.barplot(x="Topic", y="Value", data=df, palette=palette, ci=None)

# Customize the axes and title
ax.set_ylabel('Year of Birth')
ax.set_xlabel('Famous Astronomers')
ax.set_title('Year of Birth of Famous Astronomers')

# Show values on bars
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 5,
            '{:1.0f}'.format(height),
            ha='center', va='bottom')

# Adjust the margins
plt.subplots_adjust(left=0.1, right=0.95, top=0.85, bottom=0.25)

# Show the plot
plt.show()