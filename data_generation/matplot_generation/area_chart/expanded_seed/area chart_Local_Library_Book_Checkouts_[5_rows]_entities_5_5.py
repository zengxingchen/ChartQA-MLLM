
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Data from the table
data = [
    {'Date': '2023-01-01', 'Total Checkouts': 340},
    {'Date': '2023-02-01', 'Total Checkouts': 290},
    {'Date': '2023-03-01', 'Total Checkouts': 315},
    {'Date': '2023-04-01', 'Total Checkouts': 360},
    {'Date': '2023-05-01', 'Total Checkouts': 305}
]

# Preprocessing the data for plotting
dates = [datetime.strptime(d['Date'], '%Y-%m-%d') for d in data]
checkouts = [d['Total Checkouts'] for d in data]

# Plotting the area chart
fig, ax = plt.subplots()

# Fill the area under the line plot
ax.fill_between(dates, checkouts, color="skyblue", alpha=0.4)

# Plot the line to outline the filled area
ax.plot(dates, checkouts, color="Slateblue", alpha=0.6, linewidth=2)

# Enhance the x-axis with month formatting
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator())

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Adding title and labels
ax.set_title('Total Checkouts by Month')
ax.set_xlabel('Date')
ax.set_ylabel('Total Checkouts')

# Display grid
ax.grid(True)

# Adjust plot parameters to make sure the date labels fit
plt.tight_layout()

# Show the plot
plt.show()