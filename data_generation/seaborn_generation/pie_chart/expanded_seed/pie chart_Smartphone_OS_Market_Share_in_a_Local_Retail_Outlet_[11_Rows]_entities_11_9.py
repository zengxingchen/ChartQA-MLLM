
import pandas as pd
import matplotlib.pyplot as plt

# Table data provided
data = [
    {'Operating System': 'iOS 15', 'Units Sold': 220},
    {'Operating System': 'iOS 14', 'Units Sold': 180},
    {'Operating System': 'Android 12', 'Units Sold': 300},
    {'Operating System': 'Android 11', 'Units Sold': 250},
    {'Operating System': 'Android 10', 'Units Sold': 150},
    {'Operating System': 'Android 9', 'Units Sold': 70},
    {'Operating System': 'iOS 13', 'Units Sold': 110},
    {'Operating System': 'Windows Phone', 'Units Sold': 20},
    {'Operating System': 'Android 8', 'Units Sold': 40},
    {'Operating System': 'Android 7', 'Units Sold': 10},
    {'Operating System': 'Other', 'Units Sold': 5}
]

# Convert table data into a pandas DataFrame
df = pd.DataFrame(data)

# Create the pie chart
plt.figure(figsize=(10, 8))  # Set the figure size
plt.pie(df['Units Sold'], labels=df['Operating System'], autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Title for the pie chart
plt.title('Units Sold by Operating System')

# Display the chart
plt.show()