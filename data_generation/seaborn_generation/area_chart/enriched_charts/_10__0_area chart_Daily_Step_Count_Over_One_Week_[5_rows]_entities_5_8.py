
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Date': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'HoursStudied': [2, 3, 4, 5, 3, 2, 4, 5, 6, 7, 5, 6, 4, 3, 5, 7, 8, 6, 7, 8, 6, 5, 7, 8, 6, 7, 5, 4, 6, 7, 8]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 7))
area_chart = sns.lineplot(data=df, x='Date', y='HoursStudied', color='#1f77b4')
area_chart.fill_between(df['Date'], df['HoursStudied'], color='#aec7e8', alpha=0.5)

# Annotate the highest point
max_hours = df['HoursStudied'].max()
max_day = df['HoursStudied'].idxmax() + 1
plt.text(max_day, max_hours, 'Max Study\nHours', horizontalalignment='center', verticalalignment='bottom', color='#ff7f0e')

# Set the title and labels
plt.title("Daily Study Hours Over a Month")
plt.xlabel("Day of the Month")
plt.ylabel("Hours Studied")

# Display the plot
plt.show()