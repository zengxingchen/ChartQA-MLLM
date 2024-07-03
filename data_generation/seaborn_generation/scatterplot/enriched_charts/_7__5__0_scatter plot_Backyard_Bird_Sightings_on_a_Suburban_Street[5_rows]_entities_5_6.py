
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the data
data = {
    'Distance_km': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200],
    'Duration_hr': [1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0, 2.1, 2.3, 2.5, 2.7, 2.8, 3.0, 3.2, 3.4, 3.6, 3.7, 3.9, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.5]
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Create the scatterplot with custom figure size (width & height)
plt.figure(figsize=(16, 10))

# Plot the scatterplot with a specific color scheme
sns.scatterplot(x='Distance_km', y='Duration_hr', data=df, color="#4287f5")

# Set title and labels for axes
plt.title('Travel Distance vs Duration: An Adventurer\'s Log', fontsize=18, pad=20)
plt.xlabel('Distance (km)', fontsize=14)
plt.ylabel('Duration (hr)', fontsize=14)

# Show the plot
plt.show()