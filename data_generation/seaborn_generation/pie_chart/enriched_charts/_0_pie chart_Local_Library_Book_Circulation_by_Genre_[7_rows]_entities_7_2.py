
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data
data = {
    'Mode': ['Walking', 'Bicycling', 'Car', 'Public Transport', 'Motorcycle', 'Electric Scooter', 'Remote Work'],
    'Percentage': [25, 15, 40, 10, 5, 3, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Colors for the pie chart
colors = ['#FFD700', '#FF8C00', '#1E90FF', '#32CD32', '#FF6347', '#9400D3', '#A9A9A9']

# Create the pie chart
plt.figure(figsize=(10, 6))
plt.pie(df['Percentage'], labels=df['Mode'], autopct='%1.1f%%', colors=colors, startangle=140)

# Set the title
plt.title('Transportation Mode Usage Distribution')

# Show the plot
plt.show()