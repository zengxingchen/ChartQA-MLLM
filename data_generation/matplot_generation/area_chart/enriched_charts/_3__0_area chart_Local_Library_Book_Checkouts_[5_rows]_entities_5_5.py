
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Revenue': [10000, 12000, 15000, 13000, 16000, 18000, 22000, 21000, 17000, 14000, 13000, 16000]
}

df = pd.DataFrame(data)

# Converting 'Month' to a categorical type for proper ordering
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Initialize the figure
plt.figure(figsize=(14, 7))
sns.set(style="whitegrid")

# Create an area chart
sns.lineplot(data=df, x='Month', y='Revenue', color="#FF5733")
plt.fill_between(data=df, x='Month', y1='Revenue', alpha=0.3, color="#FF5733")

# Annotating the maximum revenue
max_revenue = df['Revenue'].max()
max_revenue_month = df.loc[df['Revenue'] == max_revenue, 'Month'].iloc[0]
plt.text(x=max_revenue_month, y=max_revenue, s='Peak\n${:,}'.format(max_revenue), color="black",
         horizontalalignment='left', size='medium', style='italic')

# Customize the axes and the title
plt.title("Monthly Revenue for Company XYZ", pad=20)
plt.xlabel("Month")
plt.ylabel("Revenue ($)")

# Show the plot
plt.show()