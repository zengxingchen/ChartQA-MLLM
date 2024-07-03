
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [5000, 7000, 6500, 8500, 8000, 9000, 11000, 9500, 10500, 11500, 12000, 13000]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 7))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Month', y='Revenue', data=df, 
                          color='#2E86C1', marker='o')

# Annotate each point with its value
for x, y in zip(df['Month'], df['Revenue']):
    plt.text(x=x, y=y, s=f"${y}", color='darkred', va='bottom', ha='center')

# Set the title of the graph
plt.title('Monthly Revenue for 2023')

# Adjust the labels and the legend
plt.xlabel('Month')
plt.ylabel('Revenue (USD)')

# Show the final result
plt.show()