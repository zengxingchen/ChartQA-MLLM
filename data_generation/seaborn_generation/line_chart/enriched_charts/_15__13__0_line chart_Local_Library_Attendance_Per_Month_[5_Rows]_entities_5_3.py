
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8'],
    'AverageFruitIntake': [1.5, 2, 2.8, 3, 2.7, 3.5, 4, 3.8]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(14, 10))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Week', y='AverageFruitIntake', data=df, 
                          color='#FF5733', marker='o')

# Annotate each point with its value
for x, y in zip(df['Week'], df['AverageFruitIntake']):
    plt.text(x=x, y=y, s=y, color='darkred', va='bottom', ha='center')

# Set the title of the graph
plt.title('Average Weekly Fruit Intake', fontsize=16)

# Adjust the labels and the legend
plt.xlabel('Week')
plt.ylabel('Avg Fruit Intake (servings)')

# Show the final result
plt.show()