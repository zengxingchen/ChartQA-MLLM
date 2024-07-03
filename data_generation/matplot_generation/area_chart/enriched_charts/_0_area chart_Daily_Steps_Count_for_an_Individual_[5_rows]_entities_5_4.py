
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Sample data points (you would include all 365 days with their corresponding temperatures)
data = """
Date,Temperature
2023-01-01,5
2023-01-02,6
2023-01-03,7
...
2023-12-30,4
2023-12-31,5
"""

# Converting the string data to a pandas DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data), parse_dates=['Date'])

# Set the figure size and color scheme
sns.set(rc={'figure.figsize':(12,6)})
palette = sns.color_palette(["#3366CC"])

# Create the area chart
ax = sns.lineplot(x='Date', y='Temperature', data=df, color="#3366CC")
ax.fill_between(df.Date, df.Temperature, color="#3366CC", alpha=0.3)

# Set chart title and labels
ax.set_title('Average Daily Temperature in Region X - 2023')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')

# Format the x-axis to show months
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))
plt.xticks(rotation=45)

# Add annotation
ax.annotate('Peak Summer Temp', xy=('2023-07-15', df.loc[df['Date'] == '2023-07-15', 'Temperature'].values[0]),
             xytext=('2023-08-15', 25), arrowprops=dict(facecolor='#333333', arrowstyle='->'), 
             fontsize=12, color='#333333')

plt.tight_layout()
plt.show()