
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset in a dictionary
data = {
    'Country': ['USA', 'USA', 'USA', 'USA', 'USA', 'Canada', 'Canada', 'Canada', 'Canada', 'Canada', 
                'UK', 'UK', 'UK', 'UK', 'UK', 'Germany', 'Germany', 'Germany', 'Germany', 'Germany', 
                'France', 'France', 'France', 'France', 'France'],
    'Technology': ['Smartphones', 'Laptops', 'Tablets', 'Smartwatches', 'Desktop Computers', 
                   'Smartphones', 'Laptops', 'Tablets', 'Smartwatches', 'Desktop Computers', 
                   'Smartphones', 'Laptops', 'Tablets', 'Smartwatches', 'Desktop Computers', 
                   'Smartphones', 'Laptops', 'Tablets', 'Smartwatches', 'Desktop Computers', 
                   'Smartphones', 'Laptops', 'Tablets', 'Smartwatches', 'Desktop Computers'],
    'Usage (Hours per Week)': [20, 18, 12, 10, 15, 18, 17, 11, 9, 14, 19, 16, 10, 8, 13, 17, 15, 9, 7, 12, 16, 14, 8, 6, 11]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Create a vertical bar plot
plt.figure(figsize=(10, 12))
sns.barplot(
    x='Technology', 
    y='Usage (Hours per Week)', 
    hue='Country', 
    data=df,
    palette=['#8E44AD', '#2980B9', '#27AE60', '#E67E22', '#E74C3C'],
    dodge=True,
    edgecolor='.2',
    linewidth=.6
)

# Adjusting the bar width (by adjusting the distance between the bars)
plt.xticks(rotation=45)
plt.legend(title='Country')

# Set the title and the labels of the plot
plt.title('Weekly Usage of Technology Across Different Countries')
plt.xlabel('Technology')
plt.ylabel('Usage (Hours per Week)')

# Show the plot
plt.show()