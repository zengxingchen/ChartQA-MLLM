
import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'History Books': [85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140],
    'Science Books': [120, 115, 125, 130, 140, 150, 155, 160, 165, 170, 175, 180],
    'Literature Books': [95, 100, 110, 120, 130, 140, 145, 150, 160, 165, 170, 175]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='Book Type', value_name='Sales')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(16, 9))

# History Books: #FFD700 (Gold), Science Books: #6A5ACD (Slate Blue), Literature Books: #FF69B4 (Hot Pink)
colors = ["#FFD700", "#6A5ACD", "#FF69B4"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Monthly Sales Data for Different Types of Books', fontsize=18, loc='center')
plt.ylabel('Number of Books Sold', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Book Type', loc='upper left')

# Annotation
for i, row in df.iterrows():
    total_sales = row['History Books'] + row['Science Books'] + row['Literature Books']
    plt.text(row['Month'], total_sales, f'{total_sales}', ha='center', va='bottom')

# Remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Show the plot
plt.tight_layout()
plt.show()