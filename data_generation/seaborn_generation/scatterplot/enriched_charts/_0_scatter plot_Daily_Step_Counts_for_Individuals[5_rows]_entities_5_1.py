
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Temperature': [21, 24, 19, 22, 25, 27, 23, 20, 28, 26, 29, 18, 30, 31],
    'IceCreamsSold': [87, 121, 79, 93, 130, 144, 99, 85, 152, 139, 167, 74, 172, 180]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create the scatterplot
plt.figure(figsize=(10, 6))
scatter_plot = sns.scatterplot(x='Temperature', y='IceCreamsSold',
                               data=df, color="#3498DB", s=50)

# Customize the axes and title
scatter_plot.set_title('Daily Temperature vs. Ice Creams Sold', fontsize=16)
scatter_plot.set_xlabel('Temperature (°C)', fontsize=14)
scatter_plot.set_ylabel('Ice Creams Sold', fontsize=14)

# Show the plot
plt.show()