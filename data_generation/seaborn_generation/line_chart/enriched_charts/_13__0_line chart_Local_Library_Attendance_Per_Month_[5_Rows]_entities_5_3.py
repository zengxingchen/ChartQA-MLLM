
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8'],
    'AverageExerciseHours': [2, 3, 2.5, 4, 3.5, 5, 4.5, 6]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(12, 8))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Week', y='AverageExerciseHours', data=df, 
                          color='#1f77b4', marker='o')

# Annotate each point with its value
for x, y in zip(df['Week'], df['AverageExerciseHours']):
    plt.text(x=x, y=y, s=y, color='blue', va='bottom', ha='center')

# Set the title of the graph
plt.title('Average Weekly Exercise Hours')

# Adjust the labels and the legend
plt.xlabel('Week')
plt.ylabel('Avg Exercise Hours')

# Show the final result
plt.show()