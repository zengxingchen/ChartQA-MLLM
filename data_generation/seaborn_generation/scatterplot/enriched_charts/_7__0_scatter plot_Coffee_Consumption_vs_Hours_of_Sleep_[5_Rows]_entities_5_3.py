
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'ConcertAttendance': [1200, 1500, 1800, 2200, 2800, 3200, 3500, 3400, 3100, 2700, 2000, 1700],
    'RevenueGenerated': [24000, 30000, 36000, 44000, 56000, 64000, 70000, 68000, 62000, 54000, 40000, 34000]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 8))

# Create scatterplot
scatter = sns.scatterplot(
    x='ConcertAttendance', 
    y='RevenueGenerated', 
    data=df, 
    s=150,  # size of points
    color='#4B0082'  # indigo color
)

# Setting the title
plt.title('Concert Attendance vs Revenue Generated', fontsize=16)

# Add labels to the axes
plt.xlabel('Concert Attendance')
plt.ylabel('Revenue Generated ($)')

# Show the plot
plt.show()