
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'AverageTemperature': [32, 35, 45, 55, 65, 75, 85, 85, 70, 60, 50, 38],
    'IceCreamsSold': [150, 180, 240, 300, 450, 600, 800, 790, 650, 500, 360, 190]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Create scatterplot
scatter = sns.scatterplot(
    x='AverageTemperature', 
    y='IceCreamsSold', 
    data=df, 
    s=100,  # size of points
    color='#FF6347'  # tomatored color
)

# Setting the title
plt.title('Average Temperature vs Ice Cream Sales')

# Add labels to the axes
plt.xlabel('Average Temperature (F)')
plt.ylabel('Ice Creams Sold')

# Show the plot
plt.show()