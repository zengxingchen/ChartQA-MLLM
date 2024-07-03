
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data = {
    'Activity': ['Yoga', 'Running', 'Cycling', 'Swimming', 'Hiking', 'Meditation', 'Gym', 'Dancing', 'Pilates', 'Walking', 
                 'TeamSports', 'MartialArts', 'RockClimbing', 'Gardening', 'Boxing', 'Crossfit', 'TaiChi', 'Zumba', 
                 'Basketball', 'Tennis'],
    'MentalWellbeingScore': [80, 70, 85, 60, 90, 95, 75, 65, 88, 55, 78, 82, 92, 58, 67, 73, 83, 69, 76, 74],
    'PhysicalActivityHours': [5, 8, 7, 4, 9, 3, 6, 7, 5, 2, 8, 6, 7, 4, 6, 7, 5, 6, 8, 7]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create the scatterplot
plt.figure(figsize=(14, 10))
scatter_plot = sns.scatterplot(x='MentalWellbeingScore', y='PhysicalActivityHours',
                               data=df, color="#3498DB", s=100)

# Customize the axes and title
scatter_plot.set_title('Mental Well-being vs. Physical Activity Hours', fontsize=22)
scatter_plot.set_xlabel('Mental Well-being Score', fontsize=18)
scatter_plot.set_ylabel('Physical Activity Hours', fontsize=18)

# Show the plot
plt.show()