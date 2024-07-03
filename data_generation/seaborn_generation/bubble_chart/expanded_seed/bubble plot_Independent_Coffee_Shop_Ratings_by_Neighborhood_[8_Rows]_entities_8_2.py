
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assuming the table data is a list of dictionaries as provided
data = [
    {'Neighborhood': 'Elmwood', 'Coffee Shop Name': 'Beans and Brews', 'Number of Reviews': 256, 'Average Rating': 4.5, 'Local Population': 23000},
    {'Neighborhood': 'Maple District', 'Coffee Shop Name': 'Grounds of Daybreak', 'Number of Reviews': 523, 'Average Rating': 4.2, 'Local Population': 18000},
    {'Neighborhood': 'River East', 'Coffee Shop Name': "Cup o' Joys", 'Number of Reviews': 392, 'Average Rating': 4.7, 'Local Population': 21000},
    {'Neighborhood': 'West End', 'Coffee Shop Name': 'The Coffee Nook', 'Number of Reviews': 145, 'Average Rating': 3.8, 'Local Population': 17000},
    {'Neighborhood': 'Downtown', 'Coffee Shop Name': 'Java Central', 'Number of Reviews': 918, 'Average Rating': 4.3, 'Local Population': 29000},
    {'Neighborhood': 'Old Town', 'Coffee Shop Name': 'Roasted Whispers', 'Number of Reviews': 487, 'Average Rating': 4.6, 'Local Population': 22000},
    {'Neighborhood': 'South Pointe', 'Coffee Shop Name': 'Morning Fuel Cafe', 'Number of Reviews': 354, 'Average Rating': 3.9, 'Local Population': 25000},
    {'Neighborhood': 'Lakefront', 'Coffee Shop Name': 'Café Lucente', 'Number of Reviews': 640, 'Average Rating': 4.4, 'Local Population': 27500}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Create a scatter plot using Seaborn where:
# x-axis represents 'Local Population'
# y-axis represents 'Average Rating'
# size of the bubble represents 'Number of Reviews'
# optional: color represents 'Average Rating'
plt.figure(figsize=(10, 6))
bubble_chart = sns.scatterplot(
    data=df, 
    x='Local Population', 
    y='Average Rating', 
    size='Number of Reviews', 
    hue='Average Rating',
    sizes=(100, 1000), # Control the range of bubble sizes
    alpha=0.6,
    palette='coolwarm' # Use a color palette that reflects the rating
)

# Customize the axes and layout
bubble_chart.set_title('Coffee Shop Popularity and Ratings by Neighborhood')
bubble_chart.set_xlabel('Local Population')
bubble_chart.set_ylabel('Average Rating')
bubble_chart.legend(title='Number of Reviews')

# Adjust the lower and upper bounds of the axes, if necessary
plt.xlim(df['Local Population'].min() - 1000, df['Local Population'].max() + 1000)
plt.ylim(df['Average Rating'].min() - 0.5, df['Average Rating'].max() + 0.5)

# Display the plot
plt.show()