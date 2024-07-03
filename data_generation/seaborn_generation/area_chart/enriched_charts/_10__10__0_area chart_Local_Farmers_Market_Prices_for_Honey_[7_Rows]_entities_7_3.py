
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Books_Read': [3, 5, 7, 6, 8, 9, 11, 10, 8, 6, 4, 5]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 10))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Books_Read', sort=False, lw=1)
plt.fill_between(df.Month, df.Books_Read, color="#4B0082")

# Assign annotation
plt.text(df.Month[df.Books_Read.idxmax()], df.Books_Read.max(), 'Peak Reading\nMonth', horizontalalignment='center', verticalalignment='bottom', fontsize=12, color='black')

# Customize the plot with title, labels, and limit
plt.title('Average Monthly Books Read in City XYZ', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Books Read', fontsize=14)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()