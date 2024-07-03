
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'AverageGymAttendance': [150, 145, 160, 155, 170, 165, 175, 180, 170, 165, 160, 155]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Initialize the matplotlib figure
plt.figure(figsize=(16, 10))

# Plotting the line chart with a Seaborn palette
line_chart = sns.lineplot(x='Month', y='AverageGymAttendance', data=df, 
                          color='#1f77b4', marker='o')

# Annotate each point with its value
for x, y in zip(df['Month'], df['AverageGymAttendance']):
    plt.text(x=x, y=y, s=y, color='black', va='bottom', ha='center')

# Set the title of the graph
plt.title('Average Monthly Gym Attendance', fontsize=20)

# Adjust the labels and the legend
plt.xlabel('Month', fontsize=16)
plt.ylabel('Average Gym Attendance', fontsize=16)

# Show the final result
plt.show()