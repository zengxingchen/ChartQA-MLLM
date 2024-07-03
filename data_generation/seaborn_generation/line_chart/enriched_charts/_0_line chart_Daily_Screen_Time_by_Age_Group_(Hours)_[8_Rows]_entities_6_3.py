
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a DataFrame using the provided table data
data = {
    'Day': [i for i in range(1, 32)],
    'Temperature': [56, 58, 60, 59, 61, 64, 65, 67, 66, 68, 69, 71, 70, 68,
                    65, 67, 66, 68, 69, 71, 73, 72, 71, 70, 68, 66, 64, 62, 60, 58, 56]
}

df = pd.DataFrame(data)

# Customizing plot size
plt.figure(figsize=(14, 6))

# Creating a line plot
sns.lineplot(x='Day', y='Temperature', data=df, color='#1E90FF')

# Adding annotations
for day, temp in zip(data['Day'], data['Temperature']):
    if day == 15:  # example of specific annotation on Day 15
        plt.text(day, temp, f"{temp}°", fontsize=9, ha='center')

# Setting plot title and labels
plt.title('Daily Average Temperature Trend over a Month', fontsize=18)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Temperature (°F)', fontsize=14)

# Display the plot
plt.show()