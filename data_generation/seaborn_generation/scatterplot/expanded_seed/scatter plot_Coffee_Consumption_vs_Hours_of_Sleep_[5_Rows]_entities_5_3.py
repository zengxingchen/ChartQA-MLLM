
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Creating a DataFrame from the provided data
data = [
    {'Country': 'Finland', 'Average Cups of Coffee Per Day': 3.4, 'Average Hours of Sleep': 7.8},
    {'Country': 'Netherlands', 'Average Cups of Coffee Per Day': 2.4, 'Average Hours of Sleep': 8.0},
    {'Country': 'Canada', 'Average Cups of Coffee Per Day': 1.5, 'Average Hours of Sleep': 7.5},
    {'Country': 'Australia', 'Average Cups of Coffee Per Day': 1.3, 'Average Hours of Sleep': 7.0},
    {'Country': 'USA', 'Average Cups of Coffee Per Day': 1.6, 'Average Hours of Sleep': 6.8}
]

df = pd.DataFrame(data)

# Setting the style and context for more aesthetically pleasing results
sns.set(style="whitegrid", context="talk")

# Creating the scatterplot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(
    data=df,
    x='Average Cups of Coffee Per Day',
    y='Average Hours of Sleep',
    size='Average Cups of Coffee Per Day',  # Variable that sizes the markers
    hue='Country',  # Color by Country
    palette='viridis',  # Color palette for distinction
    sizes=(100, 400),  # Size range for 'size' encoding
    legend='full'
)

# Setting plot title and labels
scatter_plot.set_title('Coffee Consumption vs. Sleep Hours by Country')
scatter_plot.set_xlabel('Average Cups of Coffee Per Day')
scatter_plot.set_ylabel('Average Hours of Sleep')

# Enhancing legend
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Country')

# Showing the plot
plt.show()