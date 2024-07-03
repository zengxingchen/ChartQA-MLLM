
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a DataFrame from your data
data = [
    {'Month': 'January', 'Bus Ridership (Thousands)': 120, 'Subway Ridership (Thousands)': 200, 'Taxi Rides (Thousands)': 35, 'City Population (Thousands)': 1500},
    {'Month': 'February', 'Bus Ridership (Thousands)': 110, 'Subway Ridership (Thousands)': 190, 'Taxi Rides (Thousands)': 32, 'City Population (Thousands)': 1500},
    {'Month': 'March', 'Bus Ridership (Thousands)': 130, 'Subway Ridership (Thousands)': 220, 'Taxi Rides (Thousands)': 40, 'City Population (Thousands)': 1500},
    {'Month': 'April', 'Bus Ridership (Thousands)': 125, 'Subway Ridership (Thousands)': 210, 'Taxi Rides (Thousands)': 38, 'City Population (Thousands)': 1500},
    {'Month': 'May', 'Bus Ridership (Thousands)': 140, 'Subway Ridership (Thousands)': 230, 'Taxi Rides (Thousands)': 45, 'City Population (Thousands)': 1500},
    {'Month': 'June', 'Bus Ridership (Thousands)': 150, 'Subway Ridership (Thousands)': 240, 'Taxi Rides (Thousands)': 50, 'City Population (Thousands)': 1500},
    {'Month': 'July', 'Bus Ridership (Thousands)': 160, 'Subway Ridership (Thousands)': 250, 'Taxi Rides (Thousands)': 55, 'City Population (Thousands)': 1500},
    {'Month': 'August', 'Bus Ridership (Thousands)': 170, 'Subway Ridership (Thousands)': 260, 'Taxi Rides (Thousands)': 58, 'City Population (Thousands)': 1500},
    {'Month': 'September', 'Bus Ridership (Thousands)': 180, 'Subway Ridership (Thousands)': 270, 'Taxi Rides (Thousands)': 60, 'City Population (Thousands)': 1500},
    {'Month': 'October', 'Bus Ridership (Thousands)': 190, 'Subway Ridership (Thousands)': 280, 'Taxi Rides (Thousands)': 65, 'City Population (Thousands)': 1500},
    {'Month': 'November', 'Bus Ridership (Thousands)': 200, 'Subway Ridership (Thousands)': 290, 'Taxi Rides (Thousands)': 70, 'City Population (Thousands)': 1500},
    {'Month': 'December', 'Bus Ridership (Thousands)': 210, 'Subway Ridership (Thousands)': 300, 'Taxi Rides (Thousands)': 75, 'City Population (Thousands)': 1500}
]

df = pd.DataFrame(data)

# Convert 'Month' to a categorical type with proper ordering
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'],
    ordered=True)

# Define size scale for bubble sizes to ensure they are not too big
size_scale = 100

# Plot using seaborn
plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x='Month', 
    y='Bus Ridership (Thousands)',
    size='Subway Ridership (Thousands)', 
    sizes=(50, size_scale * df['Subway Ridership (Thousands)'].max()),
    hue='Taxi Rides (Thousands)',
    palette='viridis',
    edgecolor='gray',  # Use a static value for edgecolor since 'City Population' does not vary
    alpha=0.6
)

# Add a legend for sizes
bubble_chart.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Set axis labels and title
plt.xlabel('Month')
plt.ylabel('Bus Ridership (Thousands)')
plt.title('Public Transportation Ridership Bubble Chart')

# Adjust x-axis to show all months clearly
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()