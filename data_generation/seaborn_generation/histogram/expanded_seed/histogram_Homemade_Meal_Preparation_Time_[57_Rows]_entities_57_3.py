
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data as provided
chart_data = [
    {'Day of the Week': 'Monday', ' Time Spent (minutes)': 30},
    {'Day of the Week': 'Monday', ' Time Spent (minutes)': 25},
    {'Day of the Week': 'Monday', ' Time Spent (minutes)': 45},
    {'Day of the Week': 'Tuesday', ' Time Spent (minutes)': 20},
    {'Day of the Week': 'Tuesday', ' Time Spent (minutes)': 35},
    {'Day of the Week': 'Tuesday', ' Time Spent (minutes)': 50},
    {'Day of the Week': 'Wednesday', ' Time Spent (minutes)': 60},
    {'Day of the Week': 'Wednesday', ' Time Spent (minutes)': 25},
    {'Day of the Week': 'Wednesday', ' Time Spent (minutes)': 30},
    {'Day of the Week': 'Thursday', ' Time Spent (minutes)': 50},
    {'Day of the Week': 'Thursday', ' Time Spent (minutes)': 40},
    {'Day of the Week': 'Thursday', ' Time Spent (minutes)': 45},
    {'Day of the Week': 'Friday', ' Time Spent (minutes)': 20},
    {'Day of the Week': 'Friday', ' Time Spent (minutes)': 30},
    {'Day of the Week': 'Friday', ' Time Spent (minutes)': 25}
]

# Turn the list of dictionaries into a DataFrame
df = pd.DataFrame(chart_data)

# Now let's plot a histogram with Seaborn

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

# Initialize the figure
plt.figure(figsize=(10, 6))

# We will create a histogram of the "Time Spent (minutes)" column using Seaborn's histplot
sns.histplot(data=df, x=' Time Spent (minutes)', bins=8, kde=True, color='skyblue',
             edgecolor='black', linewidth=1.5)

# Give titles and labels to the plot
plt.title('Histogram of Time Spent (minutes) across Days of the Week', fontsize=16)
plt.xlabel('Time Spent (minutes)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Show the histogram
plt.show()