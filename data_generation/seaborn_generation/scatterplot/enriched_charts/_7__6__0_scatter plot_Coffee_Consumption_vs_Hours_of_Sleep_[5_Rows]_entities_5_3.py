
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Attendance': [300, 320, 340, 350, 370, 380, 400, 420, 440, 460, 480, 500],
    'TestScores': [75, 78, 82, 85, 88, 90, 93, 95, 97, 99, 100, 98]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(16, 9))

# Create scatterplot
scatter = sns.scatterplot(
    x='Attendance', 
    y='TestScores', 
    data=df, 
    s=150,  # size of points
    color='#FF6347'  # tomato color
)

# Setting the title
plt.title('Monthly Attendance vs Test Scores', fontsize=18)

# Add labels to the axes
plt.xlabel('Monthly Attendance')
plt.ylabel('Test Scores')

# Show the plot
plt.show()