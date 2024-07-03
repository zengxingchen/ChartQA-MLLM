
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

# Data points
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 'Fort Worth', 'Indianapolis', 'Charlotte', 'Seattle', 'Denver', 'Washington'],
    'Average_Temperature': [15.2, 22.5, 12.6, 25.4, 28.3, 14.8, 24.5, 20.6, 23.6, 19.4, 24.1, 22.8, 17.5, 12.9, 23.2, 11.5, 16.9, 13.1, 14.3, 14.7],
    'Average_Humidity': [67, 49, 71, 74, 22, 65, 64, 61, 65, 60, 68, 75, 72, 70, 65, 73, 66, 75, 52, 69]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set up the matplotlib figure
plt.figure(figsize=(12, 8))

# Draw a seaborn scatter plot
sb.scatterplot(data=df, x="Average_Temperature", y="Average_Humidity", palette=['#FF6347', '#4682B4'], s=100)

# Additional customizations
plt.title('Average Temperature and Humidity in U.S. Cities')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Average Humidity (%)')
plt.grid(True)

# Show the plot
plt.show()