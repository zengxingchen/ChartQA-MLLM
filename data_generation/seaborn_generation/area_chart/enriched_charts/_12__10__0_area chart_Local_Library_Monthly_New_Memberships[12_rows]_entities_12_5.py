
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
    'Subscribers': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
                    300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 
                    400, 410, 420, 430]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Define the area chart
plt.figure(figsize=(14, 7))  # Change width and height
ax = sns.lineplot(data=df, x='Month', y='Subscribers', color="#0073E6")  # Specific color code
ax.fill_between(df['Month'], df['Subscribers'], color="#0073E6", alpha=0.3)

# Rotate x-axis labels for better readability
for item in ax.get_xticklabels():
    item.set_rotation(45)

# Add a title and labels
ax.set_title('Monthly Subscribers Growth Over Two Years', fontsize=20, pad=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Subscribers', fontsize=12)

# Annotate the chart with a sample text label
ax.annotate('Reached 300 Subscribers', xy=('Nov-2021', 300), xytext=('Jan-2022', 320), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05))

# Show the plot
plt.tight_layout()
plt.show()