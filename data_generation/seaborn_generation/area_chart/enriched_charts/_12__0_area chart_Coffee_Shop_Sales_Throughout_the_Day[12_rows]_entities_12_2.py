
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'Book Sales': [200, 250, 300, 500, 600, 800, 900, 850, 750, 600, 400, 300]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(14, 8))
area_chart = sns.lineplot(data=df, x='Month', y='Book Sales', sort=False)
area_chart.fill_between(df['Month'], df['Book Sales'], alpha=0.3, color='#FF6347')

# Assign an annotation/text label on the chart for the highest book sales
plt.text(x='July', y=900, s='Peak Sales (900 units)', color='blue', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Book Sales Trend in a Bookstore')
plt.xlabel('Month')
plt.ylabel('Number of Books Sold')

# Finalize and show the plot
plt.tight_layout()
plt.show()