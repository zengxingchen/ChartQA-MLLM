
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Your data
data = [
    {'Date': '2023-06-01', 'Steps': 15000, 'Calories Burned': 500},
    {'Date': '2023-06-02', 'Steps': 14000, 'Calories Burned': 480},
    {'Date': '2023-06-03', 'Steps': 13000, 'Calories Burned': 460},
    {'Date': '2023-06-04', 'Steps': 12000, 'Calories Burned': 440},
    {'Date': '2023-06-05', 'Steps': 11000, 'Calories Burned': 420},
    {'Date': '2023-06-06', 'Steps': 10000, 'Calories Burned': 400},
    {'Date': '2023-06-07', 'Steps': 9000, 'Calories Burned': 380}
]

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Start plotting
fig, ax = plt.subplots(figsize=(14, 7))

# Plotting each data type with a unique style
ax.plot(df['Date'], df['Steps'], color='#1E90FF', marker='o', linestyle='-', linewidth=2, label='Steps')
ax.plot(df['Date'], df['Calories Burned'], color='#32CD32', marker='s', linestyle='--', linewidth=2, label='Calories Burned')

# Set the title and labels
ax.set_title('Weekly Fitness Activity', pad=20)
ax.set_xlabel('Date')
ax.set_ylabel('Count')

# Format the x-axis to display dates properly
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Rotate date labels to avoid overlap
plt.xticks(rotation=45)

# Adding a legend to differentiate each line
ax.legend(loc='upper right')

# Annotating specific points
for i, txt in enumerate(df['Steps']):
    ax.annotate(txt, (df['Date'][i], df['Steps'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df['Calories Burned']):
    ax.annotate(txt, (df['Date'][i], df['Calories Burned'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adjust layout to prevent clipping of the tick-labels
plt.tight_layout()

# Show the plot
plt.show()