
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data points
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Exercise Duration': [30, 45, 50, 55, 35, 60, 70, 65, 50, 55,
                          60, 75, 80, 90, 85, 70, 65, 60, 55, 50,
                          60, 70, 80, 90, 85, 80, 75, 70, 65, 60]
}
df = pd.DataFrame(data)

# Define the color palette as specific color codes
color = "#FF5733"

# Set the figure size for width and height
plt.figure(figsize=(14, 7))

# Create an area plot
plt.plot(df['Day'], df['Exercise Duration'], color=color, linewidth=2)
plt.fill_between(df['Day'], df['Exercise Duration'], color=color, alpha=0.3)

# Annotating the highest exercise duration on the chart
max_duration_day = df['Exercise Duration'].idxmax() + 1
max_duration = df['Exercise Duration'].max()
plt.text(max_duration_day, max_duration + 5, f'Peak: {max_duration} min', horizontalalignment='center', color='black')

# Set the title
plt.title('Daily Exercise Duration Over a Month')

# Set the x and y axis labels
plt.xlabel('Day')
plt.ylabel('Exercise Duration (minutes)')

# Show the plot
plt.show()