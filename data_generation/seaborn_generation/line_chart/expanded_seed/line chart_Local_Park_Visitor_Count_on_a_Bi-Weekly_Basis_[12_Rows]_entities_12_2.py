
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given chart table data
data = [
    {'Date': '2023-01-01', 'Park A': 280, 'Park B': 350, 'Park C': 400, 'Park D': 230},
    {'Date': '2023-01-15', 'Park A': 260, 'Park B': 340, 'Park C': 420, 'Park D': 250},
    {'Date': '2023-02-01', 'Park A': 290, 'Park B': 360, 'Park C': 405, 'Park D': 240},
    {'Date': '2023-02-15', 'Park A': 275, 'Park B': 330, 'Park C': 415, 'Park D': 255},
    {'Date': '2023-03-01', 'Park A': 300, 'Park B': 370, 'Park C': 430, 'Park D': 265},
    {'Date': '2023-03-15', 'Park A': 310, 'Park B': 380, 'Park C': 425, 'Park D': 270},
    {'Date': '2023-04-01', 'Park A': 320, 'Park B': 390, 'Park C': 440, 'Park D': 280},
    {'Date': '2023-04-15', 'Park A': 330, 'Park B': 400, 'Park C': 450, 'Park D': 290},
    {'Date': '2023-05-01', 'Park A': 340, 'Park B': 410, 'Park C': 455, 'Park D': 300},
    {'Date': '2023-05-15', 'Park A': 350, 'Park B': 420, 'Park C': 460, 'Park D': 310},
    {'Date': '2023-06-01', 'Park A': 360, 'Park B': 430, 'Park C': 465, 'Park D': 320},
    {'Date': '2023-06-15', 'Park A': 370, 'Park B': 440, 'Park C': 470, 'Park D': 330}
]

# Transform data into a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Melting the DataFrame so that it can be used with Seaborn easily
df_melted = df.melt(id_vars='Date', var_name='Park', value_name='Visitors')

# Create a figure and axis for the plot
plt.figure(figsize=(14, 8))

# Line plot using Seaborn
lineplot = sns.lineplot(
    data=df_melted, 
    x='Date', 
    y='Visitors', 
    hue='Park',  # Color lines differently for each park
    style='Park', # Different line styles for each park
    markers=True, # Add markers to each data point
    dashes=False, # No dashed line, solid lines for all
    palette='tab10', # Color palette for differentiation
    markersize=8, # Marker size
    linewidth=2.5 # Line width
)

# Enhancing the plot
plt.title('Park Attendance Over Time', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Display the legend
plt.legend(title='Parks', fontsize='12', title_fontsize='14', loc='upper left')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show grid
plt.grid(True)

# Save the plot as a file
plt.savefig("park_attendance_trends.png", bbox_inches='tight')

# Display the plot
plt.show()