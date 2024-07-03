
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Input data
data = [
    {'Date': '2023-02-01', 'Children (0-12)': 120, 'Teens (13-17)': 80, 'Adults (18-64)': 200, 'Seniors (65+)': 50},
    {'Date': '2023-02-02', 'Children (0-12)': 95, 'Teens (13-17)': 70, 'Adults (18-64)': 180, 'Seniors (65+)': 40},
    {'Date': '2023-02-03', 'Children (0-12)': 110, 'Teens (13-17)': 75, 'Adults (18-64)': 210, 'Seniors (65+)': 45},
    {'Date': '2023-02-04', 'Children (0-12)': 130, 'Teens (13-17)': 85, 'Adults (18-64)': 220, 'Seniors (65+)': 50},
    {'Date': '2023-02-05', 'Children (0-12)': 140, 'Teens (13-17)': 90, 'Adults (18-64)': 230, 'Seniors (65+)': 60},
    {'Date': '2023-02-06', 'Children (0-12)': 135, 'Teens (13-17)': 88, 'Adults (18-64)': 225, 'Seniors (65+)': 55},
    {'Date': '2023-02-07', 'Children (0-12)': 125, 'Teens (13-17)': 80, 'Adults (18-64)': 215, 'Seniors (65+)': 50},
    {'Date': '2023-02-08', 'Children (0-12)': 150, 'Teens (13-17)': 95, 'Adults (18-64)': 240, 'Seniors (65+)': 65}
]

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort DataFrame by date (just in case the data is not in order)
df.sort_values('Date', inplace=True)

# Prepare data for the stacked plot
dates = df['Date']
children = df['Children (0-12)']
teens = df['Teens (13-17)']
adults = df['Adults (18-64)']
seniors = df['Seniors (65+)']

# Create the stacked area chart
plt.figure(figsize=(10, 7))
plt.stackplot(dates, children, teens, adults, seniors, 
              labels=['Children (0-12)', 'Teens (13-17)', 'Adults (18-64)', 'Seniors (65+)'], 
              colors=['#FFDDC1', '#FCB555', '#6497B1', '#BBD686'])

# Customize the format of the dates in the x-axis
date_form = DateFormatter("%m-%d")
plt.gca().xaxis.set_major_formatter(date_form)

# Adding the title and labels for the axes
plt.title('Age Group Distribution Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Individuals')

# Add a legend to identify which colors represent which age group
plt.legend(loc='upper left')

# Additional style customization
plt.grid(True, linestyle='--', alpha=0.7)

# Rotate and align the tick labels so they look better
plt.gcf().autofmt_xdate()

# Display the plot
plt.tight_layout()
plt.show()