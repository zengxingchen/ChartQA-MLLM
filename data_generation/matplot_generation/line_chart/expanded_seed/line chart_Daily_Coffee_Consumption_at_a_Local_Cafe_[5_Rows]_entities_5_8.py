
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter

# Your data
data = [
    {'Date': '2023-03-01', 'Espresso': 35, 'Americano': 47, 'Latte': 59},
    {'Date': '2023-03-02', 'Espresso': 41, 'Americano': 50, 'Latte': 63},
    {'Date': '2023-03-03', 'Espresso': 39, 'Americano': 45, 'Latte': 60},
    {'Date': '2023-03-04', 'Espresso': 44, 'Americano': 48, 'Latte': 66},
    {'Date': '2023-03-05', 'Espresso': 50, 'Americano': 53, 'Latte': 70}
]

# Convert to DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Start plotting
fig, ax = plt.subplots()

# Plotting each coffee type with a unique style
ax.plot(df['Date'], df['Espresso'], color='brown', marker='o', linestyle='-', linewidth=2, label='Espresso')
ax.plot(df['Date'], df['Americano'], color='black', marker='s', linestyle='--', linewidth=2, label='Americano')
ax.plot(df['Date'], df['Latte'], color='beige', marker='^', linestyle='-.', linewidth=2, label='Latte')

# Set the title and labels
ax.set_title('Coffee Sales Data')
ax.set_xlabel('Date')
ax.set_ylabel('Number of Cups Sold')

# Format the x-axis to display dates properly
date_form = DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_form)

# Rotate date labels to avoid overlap
plt.xticks(rotation=45)

# Adding a legend to differentiate each line
ax.legend()

# Adjust layout to prevent clipping of the tick-labels
plt.tight_layout()

# Show the plot
plt.show()