
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import pandas as pd

# Prepare the data
data = [{'Date': '2023-04-01', 'Sales (in USD)': 425}, 
        {'Date': '2023-04-02', 'Sales (in USD)': 390},
        {'Date': '2023-04-03', 'Sales (in USD)': 410},
        {'Date': '2023-04-04', 'Sales (in USD)': 380},
        {'Date': '2023-04-05', 'Sales (in USD)': 430},
        {'Date': '2023-04-06', 'Sales (in USD)': 405},
        {'Date': '2023-04-07', 'Sales (in USD)': 495},
        {'Date': '2023-04-08', 'Sales (in USD)': 520},
        {'Date': '2023-04-09', 'Sales (in USD)': 470},
        {'Date': '2023-04-10', 'Sales (in USD)': 460},
        {'Date': '2023-04-11', 'Sales (in USD)': 480},
        {'Date': '2023-04-12', 'Sales (in USD)': 500}]

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Cast the Date field to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Fill the area under the line plot
ax.fill_between(df['Date'], df['Sales (in USD)'], color='skyblue', alpha=0.4)

# Also create a line on top of the area
ax.plot(df['Date'], df['Sales (in USD)'], color='SlateBlue', alpha=0.6, linewidth=2)

# Beautifying the tick labels
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Adding a title and labels
ax.set_title('Daily Sales in USD - April 2023', fontsize=16)
ax.set_ylabel('Sales (in USD)', fontsize=12)
ax.set_xlabel('Date', fontsize=12)

# Remove the top and right border
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Show grid for better readability
ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

# Show plot
plt.tight_layout()
plt.show()