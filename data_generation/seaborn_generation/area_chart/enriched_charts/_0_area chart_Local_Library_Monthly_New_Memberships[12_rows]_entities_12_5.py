
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
    'EV_Sales': [450, 470, 520, 480, 500, 540, 570, 600, 630, 610,
                 620, 650, 670, 690, 710, 730, 750, 770, 790, 810, 
                 830, 850, 870, 900]
}

df = pd.DataFrame(data)

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")

# Define the area chart
plt.figure(figsize=(14, 6))  # Change width and height
ax = sns.lineplot(data=df, x='Month', y='EV_Sales', color="#33A1C9")  # Specific color code
ax.fill_between(df['Month'], df['EV_Sales'], color="#33A1C9", alpha=0.3)

# Rotate x-axis labels for better readability
for item in ax.get_xticklabels():
    item.set_rotation(45)

# Add a title and labels
ax.set_title('Electric Vehicle Sales Over Two Years', fontsize=20)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('EV Sales', fontsize=12)

# Annotate the chart with a sample text label
ax.annotate('Start of 2022', xy=('Jan-2022', 670), xytext=('Feb-2022', 740), fontsize=12,
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

# Show the plot
plt.tight_layout()
plt.show()