
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Product A': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    'Product B': [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
    'Product C': [20, 25, 30, 35, 30, 35, 40, 45, 50, 45, 40, 35]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Product', value_name='Sales (Units)')

# Create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_melted, x='Month', y='Sales (Units)', hue='Product',
             palette=['#D32F2F', '#1976D2', '#388E3C'])

# Add annotations for the start and end of each line
for product in ['Product A', 'Product B', 'Product C']:
    plt.text(x=df['Month'][0], y=df[product][0], s=f"{df[product][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[product].iloc[-1],
             s=f"{df[product].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly Sales of Different Products (Units)', pad=20)
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()