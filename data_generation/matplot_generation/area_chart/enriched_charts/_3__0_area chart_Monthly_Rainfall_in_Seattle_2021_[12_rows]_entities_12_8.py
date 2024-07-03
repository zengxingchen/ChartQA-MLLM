
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data points above
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Steps': [3000, 4500, 5000, 5200, 4800, 5300, 6000, 5800, 6200, 6500,
              6700, 7000, 7200, 6800, 7400, 7600, 7800, 8000, 8200, 8500,
              8300, 8700, 8900, 9100, 9300, 9500, 9200, 9400, 9600, 9800]
}
df = pd.DataFrame(data)

# Define the color palette as specific color codes
palette = sns.color_palette(["#FF5733"])

# Set the figure size for width and height
plt.figure(figsize=(14, 8))

# Create an area plot
sns.lineplot(data=df, x='Day', y='Steps', palette=palette)
plt.fill_between(data['Day'], data['Steps'], color="#FF5733", alpha=0.3)

# Annotating the highest steps on the chart
max_steps_day = df['Steps'].idxmax() + 1
max_steps = df['Steps'].max()
plt.text(max_steps_day, max_steps + 200, f'Peak: {max_steps} steps', horizontalalignment='center', color='black')

# Set the title
plt.title('Daily Steps Over a Month')

# Show the plot
plt.show()