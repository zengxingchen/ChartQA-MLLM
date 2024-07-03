
import matplotlib.pyplot as plt

# Given data
data = [
    {'Month': 'January', 'Precipitation (mm)': 112},
    {'Month': 'February', 'Precipitation (mm)': 89},
    {'Month': 'March', 'Precipitation (mm)': 60},
    {'Month': 'April', 'Precipitation (mm)': 74},
    {'Month': 'May', 'Precipitation (mm)': 50},
    {'Month': 'June', 'Precipitation (mm)': 35},
    {'Month': 'July', 'Precipitation (mm)': 22},
    {'Month': 'August', 'Precipitation (mm)': 45},
    {'Month': 'September', 'Precipitation (mm)': 95},
    {'Month': 'October', 'Precipitation (mm)': 110},
    {'Month': 'November', 'Precipitation (mm)': 130},
    {'Month': 'December', 'Precipitation (mm)': 145}
]

# Extracting months and precipitation values
months = [entry['Month'] for entry in data]
precipitation = [entry['Precipitation (mm)'] for entry in data]

# Creating a bar chart
plt.figure(figsize=(12, 6)) # Set the size of the figure
bars = plt.bar(months, precipitation, color='skyblue', edgecolor='black')

# Adding visual details
plt.title('Monthly Precipitation (mm)', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Precipitation (mm)', fontsize=14)
plt.xticks(rotation=45) # Rotate month labels to fit
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding the data labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, round(yval, 1), ha='center', va='bottom', fontsize=9)

# Show the plot
plt.tight_layout() # Adjusts the plot to ensure everything fits without overlapping
plt.show()