
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data: City climate details
data = {
    'City': [
        'London','Berlin','Paris','Madrid','Rome',
        'Amsterdam','Brussels','Vienna','Oslo',
        'Stockholm','Copenhagen','Lisbon','Prague',
        'Warsaw','Athens','Helsinki','Dublin'
    ],
    'Average Temperature (°C)': [
        7,8,10,15,13,
        6,7,6,1,
        2,5,15,5,
        6,16,1,5
    ],
    'Humidity (%)': [
        81,75,77,65,73,
        88,85,78,85,
        84,86,70,76,
        79,60,90,83
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set the width and height of the plot
plt.figure(figsize=(12, 8))

# Create Seaborn scatterplot
sns.scatterplot(
    x='Average Temperature (°C)', y='Humidity (%)',
    hue='City', palette=[
        '#FF6347', '#4682B4', '#3CB371', '#FFD700', '#FFA07A',
        '#20B2AA', '#778899', '#DA70D6', '#C71585', '#FF4500',
        '#2E8B57', '#DAA520', '#CD853F', '#5F9EA0', '#9ACD32',
        '#1E90FF', '#BDB76B'
    ],
    data=df,
    s=100  # Marker size
)

# Add labels and title
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('Climate Details for Various Cities')

# Display plot
plt.show()