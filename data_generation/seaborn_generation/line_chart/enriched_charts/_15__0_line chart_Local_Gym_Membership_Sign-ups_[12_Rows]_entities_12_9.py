
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Average_Book_Sales': [50, 55, 70, 90, 100, 120, 110, 105, 95, 85, 75, 60]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the order of the months
df['Month'] = pd.Categorical(df['Month'], categories=[
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September',
    'October', 'November', 'December'], ordered=True)

# Plot the data
plt.figure(figsize=(14, 8))
ax = sns.lineplot(x='Month', y='Average_Book_Sales', data=df, 
                  marker='o', color='#3498db')

# Annotations and labels
for x, y in zip(df['Month'], df['Average_Book_Sales']):
    ax.text(x, y, f'{y}', color='red', ha='right', va='bottom')

# Customize appearance
ax.set_title('Monthly Average Book Sales in 2023', pad=20)
ax.set_xlabel('Month')
ax.set_ylabel('Book Sales')
sns.set_style('whitegrid')

plt.show()