
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Your data provided as a list of dictionaries
data = [
    {'Age Range': '18-24', 'Number of Visits (Last Month)': 320, 'Average Spend ($)': 5.5, 'Customer Satisfaction (1-5)': 4.5},
    {'Age Range': '25-34', 'Number of Visits (Last Month)': 410, 'Average Spend ($)': 6.25, 'Customer Satisfaction (1-5)': 4.2},
    # ... (rest of the data)
    {'Age Range': 'Tourists', 'Number of Visits (Last Month)': 300, 'Average Spend ($)': 7.0, 'Customer Satisfaction (1-5)': 4.3}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Create a figure and axis for the plot
plt.figure(figsize=(10, 6))

# Create a bubble chart using seaborn
bubble_plot = sns.scatterplot(
    data=df,
    x='Age Range',  # X-axis
    y='Average Spend ($)',  # Y-axis
    size='Number of Visits (Last Month)',  # Bubble sizes
    sizes=(20, 2000),
    hue='Customer Satisfaction (1-5)',  # Bubble colors
    palette='coolwarm',  # Color palette for hue encoding
    alpha=0.7,
)

# Adjust legends
bubble_plot.legend(loc='best', title='Number of Visits (Last Month)')
plt.title('Bubble Chart of Age Range vs Average Spend with Number of Visits and Customer Satisfaction')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels

# Show the plot
plt.show()