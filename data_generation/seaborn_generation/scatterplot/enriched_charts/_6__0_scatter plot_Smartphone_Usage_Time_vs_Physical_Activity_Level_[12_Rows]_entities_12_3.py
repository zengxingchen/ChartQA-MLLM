
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Exercise Duration (minutes)': [30, 45, 60, 40, 55, 70, 50],
    'Calories Burned': [150, 200, 250, 180, 230, 280, 220]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(
    x='Exercise Duration (minutes)',
    y='Calories Burned',
    data=df,
    palette=['#1E90FF', '#32CD32', '#FFD700', '#FF4500', '#800080', '#FF1493', '#00CED1'],
    s=150  # Define the size of the points
)

# Set the title
scatter.set_title('Exercise Duration vs Calories Burned')

# Show the plot
plt.show()