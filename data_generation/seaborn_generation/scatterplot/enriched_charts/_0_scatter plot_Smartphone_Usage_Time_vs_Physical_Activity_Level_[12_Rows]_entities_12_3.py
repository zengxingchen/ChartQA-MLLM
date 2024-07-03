
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Average Daily Temperature (°C)': [22, 24, 28, 30, 27, 26, 25],
    'Ice Cream Sales': [120, 150, 200, 230, 180, 170, 160]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    x='Average Daily Temperature (°C)',
    y='Ice Cream Sales',
    data=df,
    palette=['#FF6347', '#4682B4', '#32CD32', '#FF8C00', '#6A5ACD', '#FFD700', '#DC143C'],
    s=100  # Define the size of the points
)

# Set the title
scatter.set_title('Daily Temperature vs Ice Cream Sales')

# Show the plot
plt.show()