
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Average Daily Sleep Hours': [6.5, 7.2, 6.8, 7.0, 5.5, 8.0, 7.5],
    'Productivity Score': [75, 80, 78, 82, 70, 85, 88]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    x='Average Daily Sleep Hours',
    y='Productivity Score',
    data=df,
    palette=['#FF6347', '#4682B4', '#8A2BE2', '#FFD700', '#32CD32', '#FF4500', '#6A5ACD'],
    s=150  # Define the size of the points
)

# Set the title
scatter.set_title('Average Daily Sleep Hours vs Productivity Score')

# Show the plot
plt.show()