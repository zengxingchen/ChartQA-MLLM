
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Day': list(range(1, 31)),
    'Calories': [
        2000, 2200, 2100, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
        3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900,
        4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900
    ]
}
df = pd.DataFrame(data)

# Define the color palette as specific color codes
color = "#1f77b4"

# Set the figure size for width and height
plt.figure(figsize=(16, 10))

# Create an area plot
plt.plot(df['Day'], df['Calories'], color=color)
plt.fill_between(df['Day'], df['Calories'], color=color, alpha=0.5)

# Annotating the highest calorie intake on the chart
max_calories_day = df['Calories'].idxmax() + 1
max_calories = df['Calories'].max()
plt.text(max_calories_day, max_calories + 100, f'Peak: {max_calories} calories', horizontalalignment='center', color='black')

# Set the title
plt.title('Daily Calorie Intake Over a Month', pad=20)

# Show the plot
plt.show()