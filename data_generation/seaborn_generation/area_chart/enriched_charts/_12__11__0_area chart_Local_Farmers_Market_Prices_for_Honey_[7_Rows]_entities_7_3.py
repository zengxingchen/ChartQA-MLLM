
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [150, 160, 220, 280, 330, 390, 410, 430, 370, 300, 240, 190]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 10))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Visitors', sort=False, lw=2)
plt.fill_between(df.Month, df.Visitors, color="#87CEEB")

# Assign annotation
plt.text(df.Month[df.Visitors.idxmax()], df.Visitors.max(), 'Highest\nVisitors', horizontalalignment='center', verticalalignment='bottom', fontsize=12, color='black')

# Customize the plot with title, labels and limit
plt.title('Monthly Visitors to the Art Gallery', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Number of Visitors', fontsize=14)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()