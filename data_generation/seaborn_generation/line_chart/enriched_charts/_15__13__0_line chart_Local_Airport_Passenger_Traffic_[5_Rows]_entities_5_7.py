
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame for the table data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'],
    'Visitors': [12, 15, 18, 22, 25, 28, 30, 32, 35, 38, 40, 45]
}

df = pd.DataFrame(data)

# Convert 'Month' to a category so it can be properly sorted on the plot
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

# Set up the size of the figure
plt.figure(figsize=(16, 8))

# Create the line chart using seaborn
lineplot = sns.lineplot(x='Month', y='Visitors', data=df, color="#3498db", marker='o')

# Annotate each point on the line chart
for i in range(df.shape[0]):
    plt.text(df['Month'][i], df['Visitors'][i] + 1, f"{df['Visitors'][i]}", 
             ha='center', va='bottom', fontsize=10, color='#2c3e50')

# Set the title and labels
plt.title('Monthly Gym Attendance (in hundreds)', fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Visitors (in hundreds)', fontsize=14)

# Show the final plot
plt.show()