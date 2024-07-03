
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
    'Page_Views': [150, 170, 220, 180, 250, 240, 270, 300, 320, 310,
                   360, 400, 420, 440, 460, 480, 500, 550, 570, 590, 
                   610, 650, 670, 700]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Define the area chart
plt.figure(figsize=(16, 8))  # Change width and height
ax = sns.lineplot(data=df, x='Month', y='Page_Views', color="#2E8B57")  # Specific color code
ax.fill_between(df['Month'], df['Page_Views'], color="#2E8B57", alpha=0.3)

# Rotate x-axis labels for better readability
for item in ax.get_xticklabels():
    item.set_rotation(45)

# Add a title and labels
ax.set_title('Website Page Views Over Two Years', fontsize=22, pad=20)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Page Views', fontsize=14)

# Annotate the chart with a sample text label
ax.annotate('Launch of New Feature', xy=('Jan-2022', 420), xytext=('Feb-2022', 500), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

# Show the plot
plt.tight_layout()
plt.show()