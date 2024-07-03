
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a DataFrame using the provided table data
data = {
    'Day': [i for i in range(1, 32)],
    'Revenue': [1000, 1500, 1600, 1700, 1800, 1750, 1900, 2000, 2100, 2200, 2300, 2400, 2350, 2250, 2200, 2150, 2100, 2050, 2000, 1950, 1900, 1850, 1800, 1750, 1700, 1650, 1600, 1550, 1500, 1450, 1400]
}

df = pd.DataFrame(data)

# Customizing plot size
plt.figure(figsize=(12, 8))

# Creating a line plot
sns.lineplot(x='Day', y='Revenue', data=df, color='#FF6347')

# Adding annotations
for day, revenue in zip(data['Day'], data['Revenue']):
    if day == 8:  # example of specific annotation on Day 8
        plt.text(day, revenue, f"${revenue}", fontsize=9, ha='center')

# Setting plot title and labels
plt.title('Daily Revenue Trend over a Month', fontsize=18)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Revenue ($)', fontsize=14)

# Display the plot
plt.show()