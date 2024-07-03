
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'DistanceTraveled': [3, 5, 4.2, 6, 7.5, 8, 9, 4, 5.5, 6.5, 7.2, 8.8, 9.5, 10],
    'MilesWalked': [2, 3.5, 3, 4.5, 5.2, 5.5, 6, 3, 4, 4.8, 5.3, 6, 6.3, 7]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create the scatterplot
plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(x='DistanceTraveled', y='MilesWalked',
                               data=df, color="#3498DB", s=70)

# Customize the axes and title
scatter_plot.set_title('Daily Travel Distance vs. Miles Walked', fontsize=20, y=1.05)
scatter_plot.set_xlabel('Distance Traveled (km)', fontsize=16)
scatter_plot.set_ylabel('Miles Walked', fontsize=16)

# Show the plot
plt.show()