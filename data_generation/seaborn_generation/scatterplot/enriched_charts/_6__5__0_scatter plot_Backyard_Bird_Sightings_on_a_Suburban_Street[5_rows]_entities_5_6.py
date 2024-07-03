
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Practice_Hours': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    'Performance_Scores': [55, 60, 65, 68, 70, 72, 74, 76, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(12, 7))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Practice_Hours', y='Performance_Scores', data=df, color="#1f77b4")

# Set title and labels for axes
plt.title('Practice Hours vs Performance Scores', fontsize=16, pad=20)
plt.xlabel('Practice Hours')
plt.ylabel('Performance Scores')

# Show the plot
plt.show()