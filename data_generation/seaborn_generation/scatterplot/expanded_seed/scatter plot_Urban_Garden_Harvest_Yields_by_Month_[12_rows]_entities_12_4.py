
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data = [
    {'Month': 'January', 'Tomatoes (kg)': 0, 'Lettuce (kg)': 10, 'Carrots (kg)': 5, 'Cucumbers (kg)': 0},
    {'Month': 'February', 'Tomatoes (kg)': 0, 'Lettuce (kg)': 12, 'Carrots (kg)': 7, 'Cucumbers (kg)': 0},
    # ... (other months here)
    {'Month': 'December', 'Tomatoes (kg)': 1, 'Lettuce (kg)': 10, 'Carrots (kg)': 5, 'Cucumbers (kg)': 2}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Now, let's melt the pandas DataFrame so that we have one column for the month,
# one for the vegetable, and one for the weight, which will be useful for Seaborn plotting.
df_melted = df.melt(id_vars=['Month'], var_name='Vegetable', value_name='Weight (kg)')

# Create a scatter plot using seaborn
sns.set(style='whitegrid')  # Setting the style of the plot
plt.figure(figsize=(10, 8))  # Set the size of the figure

# Plot the data
scatterplot = sns.scatterplot(
    x='Month',
    y='Weight (kg)',
    hue='Vegetable',  # Differentiate by vegetable type
    palette='viridis',  # Color palette used
    data=df_melted,
    s=100  # Size of the scatter points
)

# Improve readability by rotating the x-labels
plt.xticks(rotation=45)

# Set title and labels with font size adjustment
plt.title('Monthly Vegetable Production (kg)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Weight (kg)', fontsize=12)

# Show the legend
plt.legend(title='Vegetable')

# Show the plot
plt.show()