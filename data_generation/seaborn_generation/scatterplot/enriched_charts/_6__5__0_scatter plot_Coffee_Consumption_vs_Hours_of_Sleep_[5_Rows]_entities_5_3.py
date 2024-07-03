
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December'],
    'StepsTaken': [12000, 15000, 21000, 30000, 35000, 42000, 50000, 48000, 40000, 38000, 32000, 29000],
    'CaloriesBurned': [360, 450, 630, 900, 1050, 1260, 1500, 1440, 1200, 1140, 960, 870]
}

df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(16, 9))

# Create scatterplot
scatter = sns.scatterplot(
    x='StepsTaken', 
    y='CaloriesBurned', 
    data=df, 
    s=150,  # size of points
    color='#FF5733'  # different color code for clarity
)

# Setting the title
plt.title('Steps Taken vs Calories Burned Over a Year', fontsize=16)

# Add labels to the axes
plt.xlabel('Steps Taken', fontsize=14)
plt.ylabel('Calories Burned', fontsize=14)

# Show the plot
plt.show()