
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data points above
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Temperature': [10, 12, 15, 14, 13, 16, 18, 17, 14, 12,
                    15, 16, 17, 19, 21, 22, 20, 18, 17, 16,
                    15, 17, 19, 21, 22, 24, 23, 21, 20, 19]
}
df = pd.DataFrame(data)

# Define the color palette as specific color codes
palette = sns.color_palette(["#3498db"])

# Set the figure size for width and height
plt.figure(figsize=(12, 6))

# Create an area plot
sns.lineplot(data=df, x='Day', y='Temperature', palette=palette)
plt.fill_between(data['Day'], data['Temperature'], color="#3498db", alpha=0.3)

# Annotating the highest temperature on the chart
max_temp_day = df['Temperature'].idxmax() + 1
max_temp = df['Temperature'].max()
plt.text(max_temp_day, max_temp + 0.5, f'Peak: {max_temp}°C', horizontalalignment='center', color='black')

# Set the title
plt.title('Daily Average Temperatures Over a Month')

# Show the plot
plt.show()