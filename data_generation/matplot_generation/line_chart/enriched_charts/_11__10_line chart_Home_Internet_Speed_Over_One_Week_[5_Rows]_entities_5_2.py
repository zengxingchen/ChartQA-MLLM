
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Meditation Duration (minutes)': 30, 'Mood Score': 7},
    {'Date': '2023-03-02', 'Meditation Duration (minutes)': 35, 'Mood Score': 8},
    {'Date': '2023-03-03', 'Meditation Duration (minutes)': 25, 'Mood Score': 6},
    {'Date': '2023-03-04', 'Meditation Duration (minutes)': 40, 'Mood Score': 9},
    {'Date': '2023-03-05', 'Meditation Duration (minutes)': 20, 'Mood Score': 5},
    {'Date': '2023-03-06', 'Meditation Duration (minutes)': 45, 'Mood Score': 8},
    {'Date': '2023-03-07', 'Meditation Duration (minutes)': 30, 'Mood Score': 7},
    {'Date': '2023-03-08', 'Meditation Duration (minutes)': 50, 'Mood Score': 9},
    {'Date': '2023-03-09', 'Meditation Duration (minutes)': 30, 'Mood Score': 7},
    {'Date': '2023-03-10', 'Meditation Duration (minutes)': 35, 'Mood Score': 8},
    {'Date': '2023-03-11', 'Meditation Duration (minutes)': 25, 'Mood Score': 6},
    {'Date': '2023-03-12', 'Meditation Duration (minutes)': 40, 'Mood Score': 9},
    {'Date': '2023-03-13', 'Meditation Duration (minutes)': 20, 'Mood Score': 5},
    {'Date': '2023-03-14', 'Meditation Duration (minutes)': 45, 'Mood Score': 8}
]

# Extracting data for plotting
dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
meditation_duration = [item['Meditation Duration (minutes)'] for item in data]
mood_score = [item['Mood Score'] for item in data]

# Setting up the plot
plt.figure(figsize=(14, 8))

# Plotting both meditation duration and mood score
plt.plot(dates, meditation_duration, marker='o', linestyle='-', color='#007ACC', label='Meditation Duration (minutes)')
plt.plot(dates, mood_score, marker='s', linestyle='--', color='#FF5733', label='Mood Score')

# Formatting the x-axis to show dates clearly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding some aesthetics
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Daily Meditation Duration and Mood Score Over Two Weeks', pad=20)
plt.legend(loc='upper right')
plt.grid(True)

# Rotating the date labels for better readability
plt.gcf().autofmt_xdate()

# Adding annotations
for i, txt in enumerate(meditation_duration):
    plt.annotate(txt, (dates[i], meditation_duration[i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(mood_score):
    plt.annotate(txt, (dates[i], mood_score[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='#FF5733')

# To show the plot
plt.show()