
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December'],
    'BookSales': [250, 300, 450, 600, 750, 800, 950, 850, 700, 650, 500, 400]
}
df = pd.DataFrame(data)

# Ensure that the Month column is treated as categorical with the correct order
df['Month'] = pd.Categorical(df['Month'], categories=data['Month'], ordered=True)

# Set the aesthetic style of the plots
sns.set_theme()

# Create the area chart
plt.figure(figsize=(16, 8))
area_chart = sns.lineplot(data=df, x='Month', y='BookSales', sort=False, color='#1f77b4')
area_chart.fill_between(df['Month'], df['BookSales'], alpha=0.4, color='#aec7e8')

# Assign an annotation/text label on the chart for the highest number of book sales
plt.text(x='July', y=950, s='Peak Sales (950)', color='red', va='bottom', ha='center')

# Set chart title and labels
plt.title('Monthly Book Sales', fontsize=18)
plt.xlabel('Month')
plt.ylabel('Number of Book Sales')

# Finalize and show the plot
plt.tight_layout()
plt.show()