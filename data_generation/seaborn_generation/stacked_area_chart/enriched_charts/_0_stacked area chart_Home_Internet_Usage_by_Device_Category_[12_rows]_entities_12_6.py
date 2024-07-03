
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Product A': [100, 120, 150, 130, 160, 170, 180, 200, 190, 210, 220, 230],
    'Product B': [150, 130, 170, 180, 150, 160, 170, 180, 190, 200, 210, 220],
    'Product C': [200, 210, 190, 220, 230, 240, 260, 270, 280, 290, 300, 310]
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
plt.figure(figsize=(12, 6))

# Product A: #1E90FF (Dodger Blue), Product B: #FFD700 (Gold), Product C: #32CD32 (Lime Green)
colors = ["#1E90FF", "#FFD700", "#32CD32"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Hypothetical Monthly Sales Data for Three Products', fontsize=16)
plt.ylabel('Sales', fontsize=14)
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