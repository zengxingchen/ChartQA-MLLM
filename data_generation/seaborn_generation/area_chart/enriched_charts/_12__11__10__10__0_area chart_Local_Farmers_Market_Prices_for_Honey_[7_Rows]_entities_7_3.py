
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Book_Sales': [120, 135, 150, 145, 160, 175, 190, 185, 170, 155, 140, 160]
}
df = pd.DataFrame(data)

# Set the figure size
plt.figure(figsize=(14, 9))

# Create an area chart
sns.lineplot(data=df, x='Month', y='Book_Sales', sort=False, lw=1)
plt.fill_between(df.Month, df.Book_Sales, color="#3498db")

# Assign annotation
plt.text(df.Month[df.Book_Sales.idxmax()], df.Book_Sales.max(), 'Peak Sales\nMonth', horizontalalignment='center', verticalalignment='bottom', fontsize=12, color='black')

# Customize the plot with title, labels, and limit
plt.title('Monthly Book Sales in XYZ Bookstore', fontsize=18, loc='center')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Books Sold', fontsize=14)

# Customize x-axis
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()