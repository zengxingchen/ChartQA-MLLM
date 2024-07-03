
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Average Daily Caloric Intake (kcal)': [2000, 2100, 1800, 2200, 1900, 2500, 2300],
    'Hours of Exercise': [1, 1.5, 0.5, 2, 1, 2.5, 1.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(
    x='Average Daily Caloric Intake (kcal)',
    y='Hours of Exercise',
    data=df,
    palette=['#4B0082', '#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#FF69B4', '#8A2BE2'],
    s=150  # Define the size of the points
)

# Set the title
scatter.set_title('Daily Caloric Intake vs Hours of Exercise')

# Show the plot
plt.show()