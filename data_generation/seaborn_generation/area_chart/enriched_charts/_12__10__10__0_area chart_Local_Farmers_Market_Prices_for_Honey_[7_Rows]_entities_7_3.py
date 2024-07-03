
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Distance_Run': [50, 60, 80, 75, 85, 90, 95, 100, 85, 75, 65, 70]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(16, 8))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Distance_Run', sort=False, lw=1)
plt.fill_between(df.Month, df.Distance_Run, color="#FFA500")

# Assign annotation
plt.text(df.Month[df.Distance_Run.idxmax()], df.Distance_Run.max(), 'Peak Running\nMonth', horizontalalignment='center', verticalalignment='bottom', fontsize=12, color='black')

# Customize the plot with title, labels, and limit
plt.title('Monthly Running Distance in City XYZ', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Distance Run (km)', fontsize=14)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()