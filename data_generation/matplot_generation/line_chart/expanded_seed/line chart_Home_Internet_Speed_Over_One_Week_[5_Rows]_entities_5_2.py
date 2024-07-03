
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Given data
data = [
    {'Date': '2023-03-01', 'Download Speed (Mbps)': 55.2, 'Upload Speed (Mbps)': 11.7},
    {'Date': '2023-03-02', 'Download Speed (Mbps)': 60.1, 'Upload Speed (Mbps)': 12.5},
    {'Date': '2023-03-03', 'Download Speed (Mbps)': 58.4, 'Upload Speed (Mbps)': 12.0},
    {'Date': '2023-03-04', 'Download Speed (Mbps)': 59.8, 'Upload Speed (Mbps)': 12.3},
    {'Date': '2023-03-05', 'Download Speed (Mbps)': 54.3, 'Upload Speed (Mbps)': 11.4}
]

# Extracting data for plotting
dates = [datetime.strptime(item['Date'], '%Y-%m-%d') for item in data]
download_speeds = [item['Download Speed (Mbps)'] for item in data]
upload_speeds = [item['Upload Speed (Mbps)'] for item in data]

# Setting up the plot
plt.figure(figsize=(10, 5))

# Plotting both download and upload speeds
plt.plot(dates, download_speeds, marker='o', linestyle='-', color='b', label='Download Speed (Mbps)')
plt.plot(dates, upload_speeds, marker='s', linestyle='--', color='r', label='Upload Speed (Mbps)')

# Formatting the x-axis to show dates clearly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Adding some aesthetics
plt.xlabel('Date')
plt.ylabel('Speed (Mbps)')
plt.title('Internet Speeds Over Time')
plt.legend()
plt.grid(True)

# Rotating the date labels for better readability
plt.gcf().autofmt_xdate()

# To show the plot
plt.show()