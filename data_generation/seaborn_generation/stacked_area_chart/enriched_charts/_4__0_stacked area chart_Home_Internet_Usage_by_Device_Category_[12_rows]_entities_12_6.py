
import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Electric Cars': [120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340],
    'Hybrid Cars': [180, 160, 190, 210, 220, 230, 250, 270, 290, 310, 330, 350],
    'Gasoline Cars': [250, 240, 230, 260, 270, 290, 300, 320, 340, 360, 380, 400]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data preparation for stacked area chart
df_melted = df.melt('Month', var_name='Car Type', value_name='Sales')

# Transformation of 'Month' to categorical type for proper ordering
df_melted['Month'] = pd.Categorical(df_melted['Month'],
                                    categories=data['Month'],
                                    ordered=True)

# Plotting
plt.figure(figsize=(14, 8))

# Electric Cars: #1E90FF (Dodger Blue), Hybrid Cars: #FF6347 (Tomato), Gasoline Cars: #32CD32 (Lime Green)
colors = ["#1E90FF", "#FF6347", "#32CD32"]

# Stackplot
plt.stackplot(df['Month'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=colors, alpha=0.8)

# Beautifying the plot
plt.title('Annual Sales Data for Different Types of Cars', fontsize=18)
plt.ylabel('Number of Cars Sold', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Car Type', loc='upper left')

# Annotation
for i, row in df.iterrows():
    total_sales = row['Electric Cars'] + row['Hybrid Cars'] + row['Gasoline Cars']
    plt.text(row['Month'], total_sales, f'{total_sales}', ha='center', va='bottom')

# Remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Show the plot
plt.tight_layout()
plt.show()