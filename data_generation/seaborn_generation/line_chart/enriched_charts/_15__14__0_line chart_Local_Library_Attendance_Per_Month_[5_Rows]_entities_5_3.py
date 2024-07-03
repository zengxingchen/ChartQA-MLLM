
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Temperature': [30, 32, 45, 55, 65, 75, 85, 83, 70, 60, 48, 35]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(14, 8))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Month', y='Average_Temperature', data=df, 
                          color='#FF5733', marker='o')

# Annotate each point with its value
for x, y in zip(df['Month'], df['Average_Temperature']):
    plt.text(x=x, y=y, s=f"{y}°F", color='darkgreen', va='bottom', ha='center')

# Set the title of the graph
plt.title('Monthly Average Temperature for 2023 in Fictional City', fontsize=16)

# Adjust the labels and the legend
plt.xlabel('Month', fontsize=14)
plt.ylabel('Average Temperature (°F)', fontsize=14)

# Show the final result
plt.show()