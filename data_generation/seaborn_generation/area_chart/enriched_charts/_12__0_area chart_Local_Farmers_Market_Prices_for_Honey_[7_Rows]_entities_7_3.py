
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Pages_Read': [50, 75, 100, 130, 160, 190, 220, 210, 180, 150, 100, 60]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 7))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Pages_Read', sort=False, lw=1)
plt.fill_between(df.Month, df.Pages_Read, color="#FF5733")

# Assign annotation
plt.text(df.Month[df.Pages_Read.idxmax()], df.Pages_Read.max(), 'Highest\nPages Read', horizontalalignment='center', verticalalignment='bottom', fontsize=10, color='black')

# Customize the plot with title, labels and limit
plt.title('Monthly Reading Progress in 2024', fontsize=16, pad=20)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Pages Read', fontsize=12)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()