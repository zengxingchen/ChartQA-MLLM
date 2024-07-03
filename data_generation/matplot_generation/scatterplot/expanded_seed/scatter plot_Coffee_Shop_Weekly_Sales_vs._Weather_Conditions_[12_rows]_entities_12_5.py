
import matplotlib.pyplot as plt

# The table data provided by you
data = [
    {'Week': 1, 'Sales (USD)': 1250, 'Average Temperature (°F)': 70, 'Weather Condition': 'Sunny'},
    {'Week': 2, 'Sales (USD)': 900, 'Average Temperature (°F)': 58, 'Weather Condition': 'Cloudy'},
    {'Week': 3, 'Sales (USD)': 1350, 'Average Temperature (°F)': 64, 'Weather Condition': 'Partly Cloudy'},
    {'Week': 4, 'Sales (USD)': 1100, 'Average Temperature (°F)': 71, 'Weather Condition': 'Sunny'},
    {'Week': 5, 'Sales (USD)': 950, 'Average Temperature (°F)': 55, 'Weather Condition': 'Rainy'},
    {'Week': 6, 'Sales (USD)': 1200, 'Average Temperature (°F)': 60, 'Weather Condition': 'Partly Cloudy'},
    {'Week': 7, 'Sales (USD)': 1300, 'Average Temperature (°F)': 76, 'Weather Condition': 'Sunny'},
    {'Week': 8, 'Sales (USD)': 980, 'Average Temperature (°F)': 52, 'Weather Condition': 'Windy'},
    {'Week': 9, 'Sales (USD)': 1025, 'Average Temperature (°F)': 59, 'Weather Condition': 'Overcast'},
    {'Week': 10, 'Sales (USD)': 1150, 'Average Temperature (°F)': 73, 'Weather Condition': 'Sunny'},
    {'Week': 11, 'Sales (USD)': 1080, 'Average Temperature (°F)': 50, 'Weather Condition': 'Rainy'},
    {'Week': 12, 'Sales (USD)': 925, 'Average Temperature (°F)': 49, 'Weather Condition': 'Windy'}
]

# Extracting separate lists from the data
weeks = [item['Week'] for item in data]
sales = [item['Sales (USD)'] for item in data]
avg_temps = [item['Average Temperature (°F)'] for item in data]
weather_conditions = [item['Weather Condition'] for item in data]

# Define the colors corresponding to different weather conditions
weather_colors = {
    'Sunny': 'orange',
    'Cloudy': 'gray',
    'Partly Cloudy': 'lightgray',
    'Rainy': 'blue',
    'Windy': 'purple',
    'Overcast': 'darkgray'
}

# Define marker symbols corresponding to different weather conditions
weather_markers = {
    'Sunny': 'o',  # Circle
    'Cloudy': 's',  # Square
    'Partly Cloudy': 'D',  # Diamond
    'Rainy': '^',  # Triangle Up
    'Windy': '>',  # Triangle Right
    'Overcast': 'X'  # X (filled)
}

# Create a new figure and axis for the plot
fig, ax = plt.subplots()

# Loop over data to create scatter plot with different colors and markers
for i, condition in enumerate(weather_conditions):
    ax.scatter(
        weeks[i],
        sales[i],
        s=avg_temps[i] * 3,  # Scale the size based on temperature
        c=weather_colors[condition],  # Use color based on weather
        marker=weather_markers[condition],  # Use marker based on weather
        label=condition if condition not in ax.get_legend_handles_labels()[1] else ""
    )

# Provide a legend, but avoid duplicate legend entries
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys())

# Set axis labels and the chart title
ax.set_xlabel('Week')
ax.set_ylabel('Sales (USD)')
ax.set_title('Weekly Sales by Weather Condition')

# Show the plot
plt.show()