
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Product A': [105, 125, 155, 135, 165, 175, 185, 205, 195, 215, 225, 235],
    'Product B': [145, 135, 175, 185, 155, 165, 175, 185, 195, 205, 215, 225],
    'Product C': [195, 215, 185, 225, 235, 245, 265, 275, 285, 295, 305, 315]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='Product', value_name='Sales')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(14, 7))

# Product A: #FF6347 (Tomato), Product B: #4682B4 (Steel Blue), Product C: #9ACD32 (Yellow Green)
colors = ["#FF6347", "#4682B4", "#9ACD32"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Monthly Revenue from Three Products in 2023', fontsize=18)
plt.ylabel('Revenue in $1000s', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Product', loc='upper left')

# Annotation
for i, row in df.iterrows():
    total_sales = row['Product A'] + row['Product B'] + row['Product C']
    plt.text(row['Month'], total_sales, f'{total_sales}', ha='center', va='bottom')

sns.despine()

# Show the plot
plt.tight_layout()
plt.show()