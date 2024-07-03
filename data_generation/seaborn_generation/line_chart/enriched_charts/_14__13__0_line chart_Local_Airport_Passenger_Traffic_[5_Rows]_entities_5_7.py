
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame for the table data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'],
    'Revenue': [50, 55, 60, 65, 70, 80, 90, 85, 75, 60, 50, 45]
}

df = pd.DataFrame(data)

# Convert 'Month' to a category so it can be properly sorted on the plot
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Set up the size of the figure
plt.figure(figsize=(12, 6))

# Create the line chart using seaborn
lineplot = sns.lineplot(x='Month', y='Revenue', data=df, color="#1f77b4", marker='o')

# Annotate each point on the line chart
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Revenue'][i] + 2, f"{df['Revenue'][i]}", 
             ha='center', va='bottom', fontsize=9, color='#ff7f0e')

# Set the title and labels
plt.title('Monthly Revenue of a Tech Startup (in thousands)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (in thousands)', fontsize=12)

# Show the final plot
plt.show()