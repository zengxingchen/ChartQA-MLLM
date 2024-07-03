
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Steps_Taken': [12000, 15000, 18000, 17000, 20000, 22000, 25000, 24000, 21000, 19000, 16000, 18000]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(12, 8))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Steps_Taken', sort=False, lw=1)
plt.fill_between(df.Month, df.Steps_Taken, color="#FF5733")

# Assign annotation
plt.text(df.Month[df.Steps_Taken.idxmax()], df.Steps_Taken.max(), 'Peak Activity\nMonth', horizontalalignment='center', verticalalignment='bottom', fontsize=12, color='black')

# Customize the plot with title, labels, and limit
plt.title('Average Monthly Steps Taken in City XYZ', fontsize=18, loc='left')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Steps Taken', fontsize=14)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()