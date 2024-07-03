
import seaborn as sns
import matplotlib.pyplot as plt

# Your data provided in a list of dictionaries
data = [
    {'Day': 'Monday', 'Visitor Count': 120, 'Average Time Spent (hours)': 1.5, 'Temperature (Fahrenheit)': 68},
    {'Day': 'Tuesday', 'Visitor Count': 95, 'Average Time Spent (hours)': 1.2, 'Temperature (Fahrenheit)': 70},
    {'Day': 'Wednesday', 'Visitor Count': 140, 'Average Time Spent (hours)': 1.8, 'Temperature (Fahrenheit)': 65},
    {'Day': 'Thursday', 'Visitor Count': 110, 'Average Time Spent (hours)': 1.4, 'Temperature (Fahrenheit)': 75},
    {'Day': 'Friday', 'Visitor Count': 180, 'Average Time Spent (hours)': 2.0, 'Temperature (Fahrenheit)': 77},
    {'Day': 'Saturday', 'Visitor Count': 250, 'Average Time Spent (hours)': 2.5, 'Temperature (Fahrenheit)': 80},
    {'Day': 'Sunday', 'Visitor Count': 230, 'Average Time Spent (hours)': 2.4, 'Temperature (Fahrenheit)': 78}
]

# Convert the data to a Pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Create a bubble chart using seaborn
plt.figure(figsize=(10, 6))  # Set the figure size
bubble_size = df['Average Time Spent (hours)'] * 100  # Scale up sizes for better visibility

# Create a scatterplot with 'Day' on x-axis and 'Visitor Count' on y-axis
# Size of bubbles represents 'Average Time Spent (hours)'
# The colormap 'coolwarm' represents the 'Temperature (Fahrenheit)'
bubble = sns.scatterplot(data=df, x='Day', y='Visitor Count', size=bubble_size, 
                         sizes=(50, 1000),  # Control the range of bubble sizes
                         hue='Temperature (Fahrenheit)', palette='coolwarm',
                         legend=False, alpha=0.6)  # Adjust transparency

# Adjust the x-axis labels if necessary to prevent overlap
plt.xticks(rotation=45)

# Include a color bar to represent the temperature scale
norm = plt.Normalize(df['Temperature (Fahrenheit)'].min(), df['Temperature (Fahrenheit)'].max())
sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)
sm.set_array([])

# Add the color bar to the chart with the label for temperature
cbar = plt.colorbar(sm)
cbar.set_label('Temperature (Fahrenheit)')

# Adding chart title and labels for axes
plt.title('Visitor Count vs. Day (Bubble Size represents Average Time Spent)')
plt.xlabel('Day of the Week')
plt.ylabel('Visitor Count')

# Show plot
plt.show()