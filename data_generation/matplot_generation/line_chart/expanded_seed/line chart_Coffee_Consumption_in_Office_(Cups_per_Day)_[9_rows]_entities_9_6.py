
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Create a list of dictionaries with the data provided
data = [
    {'Date': '2023-04-01', 'Marketing': 24, 'Sales': 36, 'Development': 45, 'HR': 15},
    {'Date': '2023-04-02', 'Marketing': 29, 'Sales': 31, 'Development': 48, 'HR': 18},
    {'Date': '2023-04-03', 'Marketing': 35, 'Sales': 29, 'Development': 40, 'HR': 11},
    {'Date': '2023-04-04', 'Marketing': 21, 'Sales': 38, 'Development': 50, 'HR': 17},
    {'Date': '2023-04-05', 'Marketing': 30, 'Sales': 35, 'Development': 47, 'HR': 20},
    {'Date': '2023-04-06', 'Marketing': 27, 'Sales': 32, 'Development': 45, 'HR': 22},
    {'Date': '2023-04-07', 'Marketing': 18, 'Sales': 38, 'Development': 49, 'HR': 16},
    {'Date': '2023-04-08', 'Marketing': 33, 'Sales': 40, 'Development': 60, 'HR': 19},
    {'Date': '2023-04-09', 'Marketing': 26, 'Sales': 42, 'Development': 55, 'HR': 14}
]

# Helper function to parse dates
def parse_date(d):
    return datetime.strptime(d, '%Y-%m-%d')

# Prepare data for plotting
dates = [parse_date(record['Date']) for record in data]
marketing_values = [record['Marketing'] for record in data]
sales_values = [record['Sales'] for record in data]
development_values = [record['Development'] for record in data]
hr_values = [record['HR'] for record in data]

# Plotting the data
plt.figure(figsize=(10, 6))

plt.plot(dates, marketing_values, marker='o', linestyle='-', color='blue', label='Marketing')
plt.plot(dates, sales_values, marker='s', linestyle='--', color='green', label='Sales')
plt.plot(dates, development_values, marker='^', linestyle='-.', color='red', label='Development')
plt.plot(dates, hr_values, marker='x', linestyle=':', color='purple', label='HR')

# Formatting the date axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

# Rotating date labels for better clarity
plt.gcf().autofmt_xdate(rotation=45)

# Adding labels and title
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Department Performance Over Time")

# Displaying legend
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()