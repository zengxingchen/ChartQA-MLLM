
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Performance_Score': [85, 88, 90, 92, 95, 89, 93, 97, 84, 86, 80, 91, 94, 96, 98, 83, 87, 81, 99, 100],
    'Study_Hours': [10, 11, 10.5, 12, 13, 11.5, 12.5, 14, 9, 10, 8, 11.8, 12.3, 13.7, 14.2, 9.5, 10.2, 8.5, 14.5, 15]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(14, 8))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Study_Hours', y='Performance_Score', data=df, color="#e74c3c")

# Set title and labels for axes
plt.title('Correlation Between Study Hours and Performance Score')
plt.xlabel('Study Hours')
plt.ylabel('Performance Score')

# Show the plot
plt.show()