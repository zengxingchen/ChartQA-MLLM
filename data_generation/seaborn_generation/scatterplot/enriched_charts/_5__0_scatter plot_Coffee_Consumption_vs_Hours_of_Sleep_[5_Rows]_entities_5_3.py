
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'BooksSold': [120, 150, 210, 300, 350, 420, 500, 480, 400, 380, 320, 290],
    'Revenue': [360, 450, 630, 900, 1050, 1260, 1500, 1440, 1200, 1140, 960, 870]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 8))

# Create scatterplot
scatter = sns.scatterplot(
    x='BooksSold', 
    y='Revenue', 
    data=df, 
    s=120,  # size of points
    color='#1f77b4'  # different blue color
)

# Setting the title
plt.title('Books Sold vs Revenue Generated')

# Add labels to the axes
plt.xlabel('Books Sold')
plt.ylabel('Revenue ($)')

# Show the plot
plt.show()