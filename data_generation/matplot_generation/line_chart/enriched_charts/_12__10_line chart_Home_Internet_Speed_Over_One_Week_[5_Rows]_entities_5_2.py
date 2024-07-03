
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Sunlight Hours': 5.2, 'UV Index': 2},
    {'Date': '2023-03-02', 'Sunlight Hours': 6.1, 'UV Index': 3},
    {'Date': '2023-03-03', 'Sunlight Hours': 4.8, 'UV Index': 2},
    {'Date': '2023-03-04', 'Sunlight Hours': 7.0, 'UV Index': 4},
    {'Date': '2023-03-05', 'Sunlight Hours': 5.3, 'UV Index': 2},
    {'Date': '2023-03-06', 'Sunlight Hours': 6.5, 'UV Index': 3},
    {'Date': '2023-03-07', 'Sunlight Hours': 5.9, 'UV Index': 3},
    {'Date': '2023-03-08', 'Sunlight Hours': 6.7, 'UV Index': 4},
    {'Date': '2023-03-09', 'Sunlight Hours': 4.5, 'UV Index': 2},
    {'Date': '2023-03-10', 'Sunlight Hours': 6.3, 'UV Index': 3},
    {'Date': '2023-03-11', 'Sunlight Hours': 5.0, 'UV Index': 2},
    {'Date': '2023-03-12', 'Sunlight Hours': 7.2, 'UV Index': 4},
    {'Date': '2023-03-13', 'Sunlight Hours': 6.0, 'UV Index': 3},
    {'Date': '2023-03-14', 'Sunlight Hours': 5.4, 'UV Index': 2}
]

# Extracting data for plotting
dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
sunlight_hours = [item['Sunlight Hours'] for item in data]
uv_index = [item['UV Index'] for item in data]

# Setting up the plot
plt.figure(figsize=(14, 7))

# Plotting both sunlight hours and UV index
plt.plot(dates, sunlight_hours, marker='o', linestyle='-', color='#2ca02c', label='Sunlight Hours')
plt.plot(dates, uv_index, marker='s', linestyle='--', color='#d62728', label='UV Index')

# Formatting the x-axis to show dates clearly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding some aesthetics
plt.xlabel('Date')
plt.ylabel('Measurements')
plt.title('Daily Sunlight Hours and UV Index Over Two Weeks', pad=20)
plt.legend(loc='upper right')
plt.grid(True)

# Rotating the date labels for better readability
plt.gcf().autofmt_xdate()

# Adding annotations
for i, txt in enumerate(sunlight_hours):
    plt.annotate(txt, (dates[i], sunlight_hours[i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(uv_index):
    plt.annotate(txt, (dates[i], uv_index[i]), textcoords="offset points", xytext=(0,-15), ha='center', color='#d62728')

# To show the plot
plt.show()