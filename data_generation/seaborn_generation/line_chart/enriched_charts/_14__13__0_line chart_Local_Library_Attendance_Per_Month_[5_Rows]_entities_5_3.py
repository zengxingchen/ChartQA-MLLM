
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'AverageTemperatureC': [5, 7, 10, 13, 18, 21, 25, 24, 20, 15, 10, 6]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(14, 9))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Month', y='AverageTemperatureC', data=df, 
                          color='#ff6347', marker='o')

# Annotate each point with its value
for x, y in zip(df['Month'], df['AverageTemperatureC']):
    plt.text(x=x, y=y, s=y, color='black', va='bottom', ha='center')

# Set the title of the graph
plt.title('Average Monthly Temperature (°C)', fontsize=16)

# Adjust the labels and the legend
plt.xlabel('Month', fontsize=14)
plt.ylabel('Avg Temperature (°C)', fontsize=14)

# Show the final result
plt.show()