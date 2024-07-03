
import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Electronics': [12000, 15000, 17000, 18000, 20000, 22000, 23000, 24000, 25000, 23000, 26000, 28000],
    'Clothing': [9000, 10000, 13000, 12000, 14000, 16000, 15000, 17000, 18000, 16000, 19000, 20000],
    'Groceries': [15000, 18000, 20000, 22000, 24000, 26000, 27000, 28000, 29000, 27000, 31000, 33000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='Category', value_name='Sales')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(18, 12))

# Colors for categories
colors = ["#6A5ACD", "#FF8C00", "#3CB371"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Monthly Average Sales Data for Different Product Categories', fontsize=24, pad=40)
plt.ylabel('Sales ($)', fontsize=18)
plt.xlabel('Month', fontsize=18)
plt.xticks(rotation=45, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(title='Product Category', loc='upper left', fontsize=14, title_fontsize=16)

# Annotation
for i, row in df.iterrows():
    total_sales = row['Electronics'] + row['Clothing'] + row['Groceries']
    plt.text(row['Month'], total_sales, f'${total_sales:,}', ha='center', va='bottom', fontsize=12)

# Remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Show the plot
plt.tight_layout()
plt.show()