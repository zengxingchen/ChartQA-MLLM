
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame for the table data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'],
    'Revenue': [10, 20, 30, 25, 35, 45, 40, 50, 55, 65, 60, 70]
}

df = pd.DataFrame(data)

# Convert 'Month' to a category so it can be properly sorted on the plot
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Set up the size of the figure
plt.figure(figsize=(12, 6))

# Create the line chart using seaborn
lineplot = sns.lineplot(x='Month', y='Revenue', data=df, color="#3498db", marker='o')

# Annotate each point on the line chart
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Revenue'][i] + 1, f"{df['Revenue'][i]}", 
             ha='center', va='bottom', fontsize=9, color='#333333')

# Set the title and labels
plt.title('Monthly Revenue of Small Business (in thousands)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (in thousands)', fontsize=12)

# Show the final plot
plt.show()