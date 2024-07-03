
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Your provided data
data = [
    {'Date': '2023-02-01', 'Yoga Class': 34, 'Cooking Workshop': 12, 'Language Course': 25, 'Art Sessions': 19, 'Gardening Club': 5},
    {'Date': '2023-02-02', 'Yoga Class': 30, 'Cooking Workshop': 15, 'Language Course': 22, 'Art Sessions': 20, 'Gardening Club': 8},
    {'Date': '2023-02-03', 'Yoga Class': 28, 'Cooking Workshop': 18, 'Language Course': 23, 'Art Sessions': 17, 'Gardening Club': 6},
    {'Date': '2023-02-04', 'Yoga Class': 35, 'Cooking Workshop': 11, 'Language Course': 27, 'Art Sessions': 15, 'Gardening Club': 7},
    {'Date': '2023-02-05', 'Yoga Class': 40, 'Cooking Workshop': 14, 'Language Course': 30, 'Art Sessions': 18, 'Gardening Club': 9},
    {'Date': '2023-02-06', 'Yoga Class': 38, 'Cooking Workshop': 16, 'Language Course': 28, 'Art Sessions': 21, 'Gardening Club': 4},
    {'Date': '2023-02-07', 'Yoga Class': 42, 'Cooking Workshop': 13, 'Language Course': 26, 'Art Sessions': 22, 'Gardening Club': 6},
    {'Date': '2023-02-08', 'Yoga Class': 37, 'Cooking Workshop': 17, 'Language Course': 29, 'Art Sessions': 20, 'Gardening Club': 5}
]

# Create a DataFrame from the data
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# We need to rearrange data to plot a stacked area chart
activities = df.columns[1:]

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))  # You can adjust the size if needed

# We'll use the 'Date' column for the x-axis and the count of each activity for the y-axis
for activity in activities:
    ax.stackplot(df['Date'], df[activity], labels=[activity], alpha=0.5)

# Adding labels, title, and legend
ax.set_title('Daily Attendance of Various Activities')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Participants')
ax.legend(loc='upper left')

# Formatting the x-axis to make dates more readable
plt.gcf().autofmt_xdate()

plt.show()