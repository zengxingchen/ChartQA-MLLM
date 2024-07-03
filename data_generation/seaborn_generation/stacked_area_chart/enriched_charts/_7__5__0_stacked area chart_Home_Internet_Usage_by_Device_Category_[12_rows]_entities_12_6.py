
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Product A': [300, 320, 340, 360],
    'Product B': [280, 290, 310, 330],
    'Product C': [260, 270, 290, 310],
    'Product D': [240, 250, 270, 290]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Quarter', var_name='Product', value_name='Sales')

# Transformation of 'Quarter' to categorical type for proper ordering
df_melted['Quarter'] = pd.Categorical(df_melted['Quarter'],
                                    categories=data['Quarter'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(16, 9))

# Product A: #1f77b4, Product B: #ff7f0e, Product C: #2ca02c, Product D: #d62728
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# Stackplot
plt.stackplot(df['Quarter'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Quarterly Sales Revenue of Different Products in 2023', fontsize=20)
plt.ylabel('Revenue in $1000s', fontsize=16)
plt.xlabel('Quarter', fontsize=16)
plt.xticks(rotation=0)
plt.legend(title='Product', loc='upper left')

# Annotation
for i, row in df.iterrows():
    total_sales = row['Product A'] + row['Product B'] + row['Product C'] + row['Product D']
    plt.text(row['Quarter'], total_sales, f'{total_sales}', ha='center', va='bottom')

sns.despine()

# Show the plot
plt.tight_layout()
plt.show()