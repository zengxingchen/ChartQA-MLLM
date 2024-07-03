
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the new data
data = {
    'Hours_Slept': [5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 4, 3, 3.5, 4.5, 2, 2.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 17],
    'Mental_Alertness_Score': [60, 65, 70, 75, 80, 85, 83, 80, 75, 70, 68, 65, 60, 55, 50, 45, 48, 52, 40, 43, 50, 48, 45, 43, 40, 38, 35, 30]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(12, 8))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Hours_Slept', y='Mental_Alertness_Score', data=df, color="#2ecc71")

# Set title and labels for axes
plt.title('Effect of Sleep Hours on Mental Alertness')
plt.xlabel('Hours Slept')
plt.ylabel('Mental Alertness Score')

# Show the plot
plt.show()