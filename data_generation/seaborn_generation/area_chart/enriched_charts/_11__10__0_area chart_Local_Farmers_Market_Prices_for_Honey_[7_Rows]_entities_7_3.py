
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Viewership': [8.1, 7.9, 7.6, 7.8, 8.4, 8.2, 8.7, 8.5, 8.3, 8.0, 7.8, 8.2]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 10))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Viewership', sort=False, lw=1.5)
plt.fill_between(df.Month, df.Viewership, color="#8B0000")

# Assign annotation
plt.text(df.Month[df.Viewership.idxmax()], df.Viewership.max(), 'Peak\nViewership', horizontalalignment='center', verticalalignment='bottom', fontsize=12, color='white')

# Customize the plot with title, labels, and limit
plt.title('Monthly Average TV Show Viewership in 2023', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Viewership (in millions)', fontsize=14)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()