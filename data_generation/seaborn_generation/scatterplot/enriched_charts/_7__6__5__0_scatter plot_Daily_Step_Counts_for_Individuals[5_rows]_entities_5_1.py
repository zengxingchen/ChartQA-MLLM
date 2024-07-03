
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data into a pandas DataFrame
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'HoursStudied': [3, 4, 2.5, 5, 4.2, 6, 7, 3.5, 4.8, 2.8, 5.5, 4.5, 6.2, 7.5, 3.7, 4.6, 2.7, 5.3, 4.3, 6.5, 7.2],
    'TestScores': [78, 85, 72, 88, 82, 90, 95, 80, 87, 75, 90, 83, 92, 97, 82, 88, 74, 89, 81, 93, 96]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Create the scatterplot
plt.figure(figsize=(16, 12))
scatter_plot = sns.scatterplot(x='HoursStudied', y='TestScores',
                               data=df, color="#FF6347", s=80)

# Customize the axes and title
scatter_plot.set_title('Study Hours vs. Test Scores', fontsize=24, y=1.05)
scatter_plot.set_xlabel('Hours Studied', fontsize=18)
scatter_plot.set_ylabel('Test Scores', fontsize=18)

# Show the plot
plt.show()