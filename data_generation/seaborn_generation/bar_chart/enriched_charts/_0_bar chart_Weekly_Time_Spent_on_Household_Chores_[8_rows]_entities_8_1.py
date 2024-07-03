
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'City': ['Helsinki', 'Oslo', 'Stockholm', 'Reykjavik', 'Moscow', 'Berlin', 'London', 'Paris', 
             'New York', 'San Francisco', 'Rome', 'Madrid', 'Cairo', 'Bangkok', 'Singapore', 
             'Jakarta', 'Nairobi', 'Sydney', 'Rio de Janeiro', 'Cape Town'],
    'AverageTemperature': [-1, 1, 2, 2, 4, 9, 11, 12, 14, 15, 16, 16, 20, 28, 27, 27, 19, 18, 23, 17]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 8))  # Width and height modification
sns.barplot(x="AverageTemperature", y="City", data=df,
            palette=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0','#ffb3e6', '#c4e17f', '#76d7c4', '#f7dc6f',
                     '#6fa8dc', '#c9a0dc', '#E39191', '#a5a5a5', '#58D68D', '#D68910', '#52BE80', '#1F618D', '#2ECC71', '#E59866', '#5DADE2'],
            dodge=False)  # Color modification using specific color codes

# Set the bars' width
for bar in plt.gca().patches:
    bar.set_height(0.8)  # Width of bars when horizontal (actually controls the height of horizontal bars)

plt.xlabel('Average Temperature (°C)')
plt.ylabel('City')
plt.title('Average Temperatures of World Cities')
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()