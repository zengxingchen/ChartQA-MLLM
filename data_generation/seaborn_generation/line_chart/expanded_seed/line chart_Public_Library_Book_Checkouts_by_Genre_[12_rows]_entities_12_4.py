
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Provided chart table data
data = [
    {'Date': '2023-01-01', 'Non-Fiction': 75, 'Fiction': 120, 'Mystery': 90, 'Thriller': 85, 'Sci-Fi': 70, "Children's Books": 130},
    {'Date': '2023-01-08', 'Non-Fiction': 65, 'Fiction': 110, 'Mystery': 85, 'Thriller': 75, 'Sci-Fi': 65, "Children's Books": 140},
    # ... (other data points)
    {'Date': '2023-03-22', 'Non-Fiction': 130, 'Fiction': 190, 'Mystery': 135, 'Thriller': 115, 'Sci-Fi': 105, "Children's Books": 165}
]

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# Convert date strings to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Melt the DataFrame to have genres in a single column and counts in another column
df_melted = df.melt(id_vars='Date', var_name='Genre', value_name='Sales')

# Create the lineplot with seaborn
plt.figure(figsize=(14, 8)) # Customize the size of the plot
sns.lineplot(data=df_melted, x='Date', y='Sales', hue='Genre', style='Genre', markers=True, dashes=False)

# Enhance the plot with title, labels, and a legend
plt.title('Book Sales Over Time by Genre')
plt.xlabel('Date')
plt.ylabel('Number of Books Sold')
plt.legend(title='Book Genre', loc='upper left', bbox_to_anchor=(1, 1)) # Move the legend out of the plot

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show grid
plt.grid(True)

# Show the plot
plt.tight_layout() # Adjust layout to fit the figure neatly
plt.show()