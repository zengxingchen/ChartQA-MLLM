
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'RevenueGenerated': [12000, 15500, 20500, 31000, 37000, 42000, 50500, 49000, 40000, 38500, 33000, 29500],
    'CustomerSatisfaction': [76, 82, 89, 95, 90, 85, 91, 87, 88, 84, 86, 80]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(18, 10))

# Create scatterplot
scatter = sns.scatterplot(
    x='RevenueGenerated', 
    y='CustomerSatisfaction', 
    data=df, 
    s=150,  # size of points
    color='#1E90FF'  # different color code for clarity
)

# Setting the title
plt.title('Revenue Generated vs Customer Satisfaction Over a Year', fontsize=18, pad=20)

# Add labels to the axes
plt.xlabel('Revenue Generated ($)', fontsize=16)
plt.ylabel('Customer Satisfaction (%)', fontsize=16)

# Show the plot
plt.show()