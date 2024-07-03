
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data here
data = [
    {'Time': '6AM', 'Sales in USD': 75},
    {'Time': '7AM', 'Sales in USD': 150},
    {'Time': '8AM', 'Sales in USD': 300},
    {'Time': '9AM', 'Sales in USD': 200},
    {'Time': '10AM', 'Sales in USD': 190},
    {'Time': '11AM', 'Sales in USD': 210},
    {'Time': '12PM', 'Sales in USD': 230},
    {'Time': '1PM', 'Sales in USD': 250},
    {'Time': '2PM', 'Sales in USD': 220},
    {'Time': '3PM', 'Sales in USD': 180},
    {'Time': '4PM', 'Sales in USD': 160},
    {'Time': '5PM', 'Sales in USD': 120}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Ensure Sales in USD is numeric dtype for plotting
df['Sales in USD'] = pd.to_numeric(df['Sales in USD'])

# Create a lineplot using Seaborn
sns.set_theme(style="whitegrid")

# Since we don't have an area function in seaborn, we will create a lineplot and fill the area under the line.
# Define the lineplot
line = sns.lineplot(x='Time', y='Sales in USD', data=df, sort=False)

# Get current axis
ax = plt.gca()

# Use Matplotlib's fill_between function to fill the area under the line
ax.fill_between(x=df['Time'], y1=df['Sales in USD'], alpha=0.3)

# Customize the plot to make it more aesthetically pleasing
ax.set_title('Area Chart of Sales over Time')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Sales in USD')
plt.xticks(rotation=45)  # Rotate the x labels for better readability

# Show the final plot
plt.show()