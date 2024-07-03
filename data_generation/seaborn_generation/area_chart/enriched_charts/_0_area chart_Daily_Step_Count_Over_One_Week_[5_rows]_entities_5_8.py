
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'AvgTemp': [55, 56, 54, 53, 57, 58, 60, 61, 62, 64, 65, 63, 59, 60, 62, 64, 66, 67, 68, 69, 70, 68, 66, 64, 65, 67, 69, 68, 66, 65, 64]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(12, 6))
area_chart = sns.lineplot(data=df, x='Day', y='AvgTemp', color='#FF5733')
area_chart.fill_between(df['Day'], df['AvgTemp'], color='#FFC300', alpha=0.5)

# Annotate the highest point
max_temp = df['AvgTemp'].max()
max_day = df['AvgTemp'].idxmax() + 1
plt.text(max_day, max_temp, 'Highest\nTemp', horizontalalignment='center', verticalalignment='bottom', color='#C70039')

# Set the title and labels
plt.title("Average Daily Temperature Over a Month")
plt.xlabel("Day of the Month")
plt.ylabel("Average Temperature (°F)")

# Display the plot
plt.show()