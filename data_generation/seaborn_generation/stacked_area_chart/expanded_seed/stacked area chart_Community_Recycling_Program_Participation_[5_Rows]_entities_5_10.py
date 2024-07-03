
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The provided data
data = [
    {'Year': 2016, 'Households Participating': 3200, 'Pounds Recycled': 128000, 'Schools Participating': 15, 'Pounds Recycled by Schools': 4500},
    {'Year': 2017, 'Households Participating': 3400, 'Pounds Recycled': 136000, 'Schools Participating': 18, 'Pounds Recycled by Schools': 5400},
    {'Year': 2018, 'Households Participating': 3550, 'Pounds Recycled': 142000, 'Schools Participating': 20, 'Pounds Recycled by Schools': 6000},
    {'Year': 2019, 'Households Participating': 3700, 'Pounds Recycled': 148000, 'Schools Participating': 22, 'Pounds Recycled by Schools': 6600},
    {'Year': 2020, 'Households Participating': 3900, 'Pounds Recycled': 156000, 'Schools Participating': 25, 'Pounds Recycled by Schools': 7500}
]

# Convert the data to a pandas DataFrame for plotting
df = pd.DataFrame(data)

# Prepare data for the stacked area chart
years = df['Year']
household_recycled_pounds = df['Pounds Recycled'] - df['Pounds Recycled by Schools']
schools_recycle_pounds = df['Pounds Recycled by Schools']

# Initialize Seaborn
sns.set_style("whitegrid")
palette = sns.color_palette("husl", 2)  # selecting a color palette with 2 distinct colors

# Create the stackplot
plt.stackplot(years, household_recycled_pounds, schools_recycle_pounds, labels=['Households', 'Schools'], colors=palette, alpha=0.8)

# Add title and labels
plt.title('Recycling over Time by Households and Schools')
plt.xlabel('Year')
plt.ylabel('Pounds Recycled')

# Add a legend, specify the location, and make sure it doesn't cover the plot
plt.legend(loc='upper left')

# Optimize layout to ensure the legend and labels are visible
plt.tight_layout()

# Show the plot
plt.show()