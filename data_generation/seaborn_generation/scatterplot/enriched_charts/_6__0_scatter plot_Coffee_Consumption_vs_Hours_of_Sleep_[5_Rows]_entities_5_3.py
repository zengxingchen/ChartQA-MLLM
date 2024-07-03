
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'BookSales': [50, 70, 90, 100, 150, 200, 220, 210, 170, 140, 100, 80],
    'ScreenTime': [120, 110, 130, 150, 180, 200, 250, 230, 190, 170, 140, 130]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 8))

# Create scatterplot
scatter = sns.scatterplot(
    x='BookSales', 
    y='ScreenTime', 
    data=df, 
    s=100,  # size of points
    color='#1E90FF'  # dodgerblue color
)

# Setting the title
plt.title('Monthly Book Sales vs Screen Time', fontsize=16)

# Add labels to the axes
plt.xlabel('Book Sales')
plt.ylabel('Screen Time (minutes)')

# Show the plot
plt.show()