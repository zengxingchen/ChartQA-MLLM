
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Average Sleep Hours': [6.8, 7.1, 6.5, 7.3, 7.0, 8.2, 7.8],
    'Productivity Score': [70, 75, 68, 78, 74, 85, 80]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(14, 10))
scatter = sns.scatterplot(
    x='Average Sleep Hours',
    y='Productivity Score',
    data=df,
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'],
    s=150  # Define the size of the points
)

# Set the title
scatter.set_title('Impact of Sleep on Productivity', fontsize=20)

# Show the plot
plt.show()