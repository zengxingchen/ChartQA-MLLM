
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import pandas as pd

# Data provided
data = [
    {'Date': '2023-04-10', 'Steps': 7584},
    {'Date': '2023-04-11', 'Steps': 6621},
    {'Date': '2023-04-12', 'Steps': 9891},
    {'Date': '2023-04-13', 'Steps': 10472},
    {'Date': '2023-04-14', 'Steps': 4551}
]

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Converting the Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sorting the DataFrame just in case it's not in the correct order
df.sort_values('Date', inplace=True)

# Setting up the plot
plt.figure(figsize=(10, 6))

# Plotting the 'Steps' as a line chart
plt.plot(df['Date'], df['Steps'], label='Daily Steps', color='blue', linestyle='-', marker='o')

# Beautifying the x-axis with date formatting
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))

# Rotating the dates on the x-axis for better visibility
plt.gcf().autofmt_xdate()

# Adding title and labels
plt.title('Steps over Time')
plt.xlabel('Date')
plt.ylabel('Number of Steps')

# Adding a legend
plt.legend()

# Optional: Adding a grid
plt.grid(True)

# Displaying the plot
plt.show()