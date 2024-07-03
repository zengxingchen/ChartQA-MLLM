
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime

# Your data
data = [{'Week': '2023-01-01 to 2023-01-07', 'Visitors': 540},
        {'Week': '2023-01-08 to 2023-01-14', 'Visitors': 623},
        {'Week': '2023-01-15 to 2023-01-21', 'Visitors': 579},
        {'Week': '2023-01-22 to 2023-01-28', 'Visitors': 690},
        {'Week': '2023-01-29 to 2023-02-04', 'Visitors': 712},
        {'Week': '2023-02-05 to 2023-02-11', 'Visitors': 835},
        {'Week': '2023-02-12 to 2023-02-18', 'Visitors': 589},
        {'Week': '2023-02-19 to 2023-02-25', 'Visitors': 645},
        {'Week': '2023-02-26 to 2023-03-04', 'Visitors': 702},
        {'Week': '2023-03-05 to 2023-03-11', 'Visitors': 760},
        {'Week': '2023-03-12 to 2023-03-18', 'Visitors': 810},
        {'Week': '2023-03-19 to 2023-03-25', 'Visitors': 855}]

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Extract the start of the week for the x-axis
df['StartOfWeek'] = df['Week'].apply(lambda x: datetime.strptime(x.split(' to ')[0], '%Y-%m-%d'))

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Format dates on the x-axis
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Plot the area chart
ax.fill_between(df['StartOfWeek'], df['Visitors'], color="skyblue", alpha=0.4)
ax.plot(df['StartOfWeek'], df['Visitors'], color="Slateblue", alpha=0.6, linewidth=2)

# Highlight data points
ax.scatter(df['StartOfWeek'], df['Visitors'], color='darkslateblue', zorder=3)

# Annotate the highest data point
ymax = max(df['Visitors'])
xpos = df['Visitors'].idxmax()
xmax = df.loc[xpos, 'StartOfWeek']
ax.annotate('Peak\n({})'.format(ymax), xy=(xmax, ymax), xytext=(xmax, ymax+50),
            arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Set labels and title
ax.set_xlabel("Date")
ax.set_ylabel("Number of Visitors")
ax.set_title("Weekly Visitors Area Chart")

# Rotate the date labels for better readability
plt.xticks(rotation=45)

# Show a grid
plt.grid(alpha=0.3)

# Show the plot
plt.tight_layout()
plt.show()