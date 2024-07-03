
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'AverageTemperature': [4, 6, 10, 15, 20, 25]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(10, 6))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Month', y='AverageTemperature', data=df, 
                          palette=['#FF5733', '#C70039', '#900C3F', '#571845'],
                          marker='o')

# Annotate each point with its value
for x, y in zip(df['Month'], df['AverageTemperature']):
    plt.text(x=x, y=y, s=y, color='blue', va='bottom', ha='center')

# Set the title of the graph
plt.title('Average Monthly Temperature (°C)')

# Adjust the labels and the legend
plt.xlabel('Month')
plt.ylabel('Avg Temperature (°C)')

# Show the final result
plt.show()