
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Your data as a list of dictionaries
data = [
    # ... (Your data here)
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Prepare the figure
plt.figure(figsize=(10, 8))

# Extract unique drink names and days for plotting
drinks = df['Drink'].unique()
days = df['Day'].unique()

# Generate a color palette with the same number of colors as days
palette = sns.color_palette("hsv", len(drinks))

# Plot a scatter plot for each cup size
for i, size in enumerate(['Small (8oz)', 'Medium (12oz)', 'Large (16oz)', 'Extra Large (20oz)']):
    # Temporary DataFrame for the current cup size
    temp_df = df[['Day', 'Drink', 'Total Sales ($)', size]].copy()
    temp_df['Size'] = size
    temp_df.rename(columns={size: 'Cup Size'}, inplace=True)
    
    # Plotting the scatter plot
    sns.scatterplot(
        x='Drink',
        y='Day',
        size='Cup Size',
        sizes=(10, 500),  # Range of size variation for bubbles
        hue='Drink',
        palette=palette,
        data=temp_df,
        alpha=0.5,
        legend='brief',
        label=size
    )

# Improve the layout
plt.title('Sales Volume by Drink Type and Cup Size')
plt.xlabel('Drink Type')
plt.ylabel('Day of Week')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Cup Sizes')
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()