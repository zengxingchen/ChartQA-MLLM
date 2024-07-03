
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Sleep_Hours': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43],
    'Happiness_Scores': [30, 40, 45, 50, 52, 55, 58, 60, 62, 64, 66, 67, 68, 70, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(14, 9))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Sleep_Hours', y='Happiness_Scores', data=df, color="#FF6347")

# Set title and labels for axes
plt.title('Sleep Hours vs Happiness Scores', fontsize=18, pad=20)
plt.xlabel('Sleep Hours')
plt.ylabel('Happiness Scores')

# Show the plot
plt.show()