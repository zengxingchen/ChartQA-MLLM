
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Creating the data as a DataFrame
data = {
    'Subject': ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Physical Education', 'Art', 'Music'],
    'Average Grade': [88, 92, 85, 90, 78, 82, 87, 95, 80, 83]
}

df = pd.DataFrame(data)

# Sorting data to make the chart easier to read
df = df.sort_values('Average Grade', ascending=False)

# Set up the matplotlib figure with changed width and height
plt.figure(figsize=(12, 6))

# Create the bar plot
sns.barplot(
    x='Subject',
    y='Average Grade',
    data=df,
    palette=[
        '#6A5ACD', '#00BFFF', '#7FFF00', '#FF4500', '#FF6347', 
        '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#DA70D6'
    ],
    linewidth=1.5,
    edgecolor='black'
)

# Adjust the width of the bars
for bar in plt.gca().patches:
    bar.set_width(0.6)

# Adding chart labels and title
plt.ylabel('Average Grade')
plt.xlabel('Subject')
plt.title('Average Grades of Students in Different Subjects')

# Show the plot
plt.show()