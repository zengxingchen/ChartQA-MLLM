
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Your data
data = [
    {'Date': '2023-06-01', 'Steps': 10234, 'Calories Burned': 345},
    {'Date': '2023-06-02', 'Steps': 9756, 'Calories Burned': 330},
    {'Date': '2023-06-03', 'Steps': 11045, 'Calories Burned': 360},
    {'Date': '2023-06-04', 'Steps': 9001, 'Calories Burned': 310},
    {'Date': '2023-06-05', 'Steps': 11567, 'Calories Burned': 375},
    {'Date': '2023-06-06', 'Steps': 12345, 'Calories Burned': 390},
    {'Date': '2023-06-07', 'Steps': 9876, 'Calories Burned': 335}
]

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Start plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting each data type with a unique style
ax.plot(df['Date'], df['Steps'], color='#FF5733', marker='o', linestyle='-', linewidth=2, label='Steps')
ax.plot(df['Date'], df['Calories Burned'], color='#33FFCE', marker='s', linestyle='--', linewidth=2, label='Calories Burned')

# Set the title and labels
ax.set_title('Daily Steps and Calories Burned', pad=20)
ax.set_xlabel('Date')
ax.set_ylabel('Count')

# Format the x-axis to display dates properly
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Rotate date labels to avoid overlap
plt.xticks(rotation=45)

# Adding a legend to differentiate each line
ax.legend(loc='upper left')

# Annotating specific points
for i, txt in enumerate(df['Steps']):
    ax.annotate(txt, (df['Date'][i], df['Steps'][i]), textcoords="offset points", xytext=(0,10), ha='center')

for i, txt in enumerate(df['Calories Burned']):
    ax.annotate(txt, (df['Date'][i], df['Calories Burned'][i]), textcoords="offset points", xytext=(0,10), ha='center')

# Adjust layout to prevent clipping of the tick-labels
plt.tight_layout()

# Show the plot
plt.show()