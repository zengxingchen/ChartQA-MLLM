
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Days_Travelled': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Cost_USD': [300, 450, 500, 550, 700, 800, 850, 900, 1000, 1050, 1100, 1200, 1250, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(14, 7))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Days_Travelled', y='Cost_USD', data=df, color="#e74c3c")

# Set title and labels for axes
plt.title('Travel Cost Based on Number of Days Traveled')
plt.xlabel('Days Traveled')
plt.ylabel('Cost (USD)')

# Show the plot
plt.show()