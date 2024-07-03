
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Average Daily Screen Time (hours)': [3.5, 4.2, 5.1, 4.8, 6.0, 7.5, 6.8],
    'Number of Social Media Posts': [50, 65, 78, 70, 85, 95, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(
    x='Average Daily Screen Time (hours)',
    y='Number of Social Media Posts',
    data=df,
    palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2'],
    s=100  # Define the size of the points
)

# Set the title
scatter.set_title('Daily Screen Time vs Social Media Activity')

# Show the plot
plt.show()