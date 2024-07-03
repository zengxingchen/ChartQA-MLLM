
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Product A': [120, 140, 160, 180, 210, 240, 250, 270, 300, 330, 340, 350],
    'Product B': [200, 180, 220, 190, 240, 200, 210, 230, 250, 220, 240, 210],
    'Product C': [300, 290, 280, 260, 235, 215, 200, 180, 160, 150, 130, 120]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Product', value_name='Sales')

# Create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_melted, x='Month', y='Sales', hue='Product',
             palette=['#FF5733', '#33FF57', '#3357FF'])

# Add annotations for the start and end of each line
for product in ['Product A', 'Product B', 'Product C']:
    plt.text(x=df['Month'][0], y=df[product][0], s=f"{df[product][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[product].iloc[-1],
             s=f"{df[product].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly Sales of Product Categories (Units)')
plt.xlabel('Month')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()