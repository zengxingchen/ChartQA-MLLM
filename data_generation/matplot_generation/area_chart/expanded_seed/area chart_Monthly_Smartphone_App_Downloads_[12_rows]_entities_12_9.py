
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Provided data in a list of dictionaries
data = [
    {'Month': 'January', 'Downloads': 5500},
    {'Month': 'February', 'Downloads': 5200},
    {'Month': 'March', 'Downloads': 6000},
    {'Month': 'April', 'Downloads': 5700},
    {'Month': 'May', 'Downloads': 6200},
    {'Month': 'June', 'Downloads': 5800},
    {'Month': 'July', 'Downloads': 6100},
    {'Month': 'August', 'Downloads': 6300},
    {'Month': 'September', 'Downloads': 6500},
    {'Month': 'October', 'Downloads': 6600},
    {'Month': 'November', 'Downloads': 6400},
    {'Month': 'December', 'Downloads': 6700}
]

# Extract months and downloads
months = [d['Month'] for d in data]
downloads = [d['Downloads'] for d in data]

# Convert month names to datetime objects for better formatting on the x-axis
months = [mdates.datestr2num(f"2023-{month[:3]}-01") for month in months]

# Create an area chart
plt.figure(figsize=(10, 6))  # Set figure size
plt.fill_between(months, downloads, color="skyblue", alpha=0.4)
plt.plot(months, downloads, color="Slateblue", alpha=0.6)

# Modify x-axis to show the month names
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# Customize the plot
plt.title('Monthly Downloads for Year 2023', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Number of Downloads')
plt.xticks(months, [mdates.num2date(month).strftime('%b') for month in months], rotation=45)
plt.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Add a legend
plt.legend(['Downloads'], loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()