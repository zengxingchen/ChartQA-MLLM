
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Popularity': [45, 60, 55, 70, 65, 80]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 8))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Month', y='Popularity', data=df, 
                          color='#FF4500', marker='o')

# Annotate each point with its value
for x, y in zip(df['Month'], df['Popularity']):
    plt.text(x=x, y=y, s=y, color='blue', va='bottom', ha='center')

# Set the title of the graph
plt.title('Monthly Music Popularity Index', pad=20)

# Adjust the labels and the legend
plt.xlabel('Month')
plt.ylabel('Popularity Index')

# Show the final result
plt.show()