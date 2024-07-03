
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame for the table data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'],
    'Visitors': [5, 10, 15, 20, 18, 25, 30, 28, 22, 24, 15, 10]
}

df = pd.DataFrame(data)

# Convert 'Month' to a category so it can be properly sorted on the plot
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Set up the size of the figure
plt.figure(figsize=(14, 7))

# Create the line chart using seaborn
lineplot = sns.lineplot(x='Month', y='Visitors', data=df, color="#2ecc71", marker='o')

# Annotate each point on the line chart
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Visitors'][i] + 1, f"{df['Visitors'][i]}", 
             ha='center', va='bottom', fontsize=9, color='#34495e')

# Set the title and labels
plt.title('Monthly Visitors to a National Park (in thousands)', fontsize=16)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Visitors (in thousands)', fontsize=12)

# Show the final plot
plt.show()