
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame with the provided data
data = {
    'City': ['London', 'New York', 'Los Angeles', 'Tokyo', 'Paris', 'Berlin', 'Moscow', 'Beijing', 'Sydney', 'Rio de Janeiro', 'Cairo', 'Mumbai'],
    'Average_Temperature_C': [15, 22, 19, 16, 14, 13, 5, 20, 17, 25, 30, 28],
    'Average_Humidity': [80, 65, 50, 63, 73, 75, 77, 55, 60, 85, 22, 70]
}

df = pd.DataFrame(data)

# Plotting the scatterplot
plt.figure(figsize=(10, 6))
scatterplot = sns.scatterplot(data=df, x='Average_Temperature_C', y='Average_Humidity', palette=['#FF6347', '#4682B4'])

scatterplot.set_title('Average Temperature and Humidity by City')
scatterplot.set_xlabel('Average Temperature (°C)')
scatterplot.set_ylabel('Average Humidity (%)')
plt.show()