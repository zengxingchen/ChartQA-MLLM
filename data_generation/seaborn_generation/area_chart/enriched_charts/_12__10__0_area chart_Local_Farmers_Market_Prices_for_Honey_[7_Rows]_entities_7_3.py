
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'ExerciseMinutes': [30, 45, 40, 50, 55, 60, 65, 70, 75, 80, 85, 90]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 10))

# Create an area chart
sns.lineplot(data=df, x='Month', y='ExerciseMinutes', sort=False, lw=1, color='#1E90FF')
plt.fill_between(df.Month, df.ExerciseMinutes, color="#87CEFA")

# Assign annotation
plt.text(df.Month[df.ExerciseMinutes.idxmax()], df.ExerciseMinutes.max(), 'Highest\nExercise Minutes', horizontalalignment='center', verticalalignment='bottom', fontsize=10, color='black')

# Customize the plot with title, labels, and limit
plt.title('Monthly Exercise Minutes in 2024', fontsize=20)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Exercise Minutes', fontsize=14)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()