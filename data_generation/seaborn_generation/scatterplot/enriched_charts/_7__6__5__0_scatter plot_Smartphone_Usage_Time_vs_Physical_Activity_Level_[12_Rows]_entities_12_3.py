
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate the data points
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Daily Exercise Hours': [1.5, 2.0, 1.0, 2.5, 2.0, 3.0, 1.8],
    'Stress Level': [65, 60, 70, 55, 58, 50, 62]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize a seaborn scatterplot
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(
    x='Daily Exercise Hours',
    y='Stress Level',
    data=df,
    palette=['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff', '#ff8800'],
    s=150  # Define the size of the points
)

# Set the title
scatter.set_title('Effect of Daily Exercise on Stress Levels', fontsize=18, pad=20)

# Show the plot
plt.show()