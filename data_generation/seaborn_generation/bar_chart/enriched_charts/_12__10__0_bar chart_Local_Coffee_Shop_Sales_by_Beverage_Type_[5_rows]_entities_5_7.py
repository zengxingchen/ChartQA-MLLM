
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating the data as a DataFrame
data = {
    'Category': ['Fruits', 'Vegetables', 'Grains', 'Dairy', 'Protein', 'Sugary Foods', 'Beverages', 'Snacks', 'Seafood', 'Spices'],
    'Average Rating': [8.7, 9.2, 7.5, 8.0, 9.1, 5.4, 8.3, 6.8, 9.0, 7.9]
}

df = pd.DataFrame(data)

# Sorting data to make the chart easier to read
df = df.sort_values('Average Rating', ascending=False)

# Set up the matplotlib figure with changed width and height
plt.figure(figsize=(8, 10))

# Create the bar plot
sns.barplot(
    y='Category',
    x='Average Rating',
    data=df,
    palette=[
        '#FF6347', '#32CD32', '#FFD700', '#4682B4', '#FF4500', 
        '#7FFF00', '#00BFFF', '#DA70D6', '#8A2BE2', '#6A5ACD'
    ],
    linewidth=1.5,
    edgecolor='black'
)

# Adjust the height of the bars
for bar in plt.gca().patches:
    bar.set_height(0.5)

# Adding chart labels and title
plt.xlabel('Average Rating')
plt.ylabel('Category')
plt.title('Average Ratings of Different Food Categories')

# Show the plot
plt.show()