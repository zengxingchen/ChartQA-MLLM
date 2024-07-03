
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 
              'Jun-2021', 'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021',
              'Nov-2021', 'Dec-2021', 'Jan-2022', 'Feb-2022', 'Mar-2022',
              'Apr-2022', 'May-2022', 'Jun-2022', 'Jul-2022', 'Aug-2022',
              'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022'],
    'Running_Distance': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75,
                         80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 
                         130, 135, 140, 145]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Define the area chart
plt.figure(figsize=(16, 8))  # Change width and height
ax = sns.lineplot(data=df, x='Month', y='Running_Distance', color="#FF5733")  # Specific color code
ax.fill_between(df['Month'], df['Running_Distance'], color="#FF5733", alpha=0.3)

# Rotate x-axis labels for better readability
for item in ax.get_xticklabels():
    item.set_rotation(45)

# Add a title and labels
ax.set_title('Monthly Running Distance Over Two Years', fontsize=22)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Running Distance (km)', fontsize=14)

# Annotate the chart with a sample text label
ax.annotate('Start of 2022', xy=('Jan-2022', 90), xytext=('Feb-2022', 110), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

# Show the plot
plt.tight_layout()
plt.show()