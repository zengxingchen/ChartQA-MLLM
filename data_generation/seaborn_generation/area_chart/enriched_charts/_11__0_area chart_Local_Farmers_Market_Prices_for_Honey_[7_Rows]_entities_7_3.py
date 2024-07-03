
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Visitors': [200, 180, 240, 300, 350, 400, 450, 420, 380, 310, 250, 220]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 8))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Visitors', sort=False, lw=1)
plt.fill_between(df.Month, df.Visitors, color="#FFA07A")

# Assign annotation
plt.text(df.Month[df.Visitors.idxmax()], df.Visitors.max(), 'Peak\nVisitors', horizontalalignment='center', verticalalignment='bottom', fontsize=10, color='black')

# Customize the plot with title, labels and limit
plt.title('Monthly Visitors to the National Museum', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Visitors', fontsize=12)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()