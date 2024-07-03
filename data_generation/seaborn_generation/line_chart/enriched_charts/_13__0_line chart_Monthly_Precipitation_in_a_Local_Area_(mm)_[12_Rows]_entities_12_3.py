
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Product A': [300, 320, 310, 290, 270, 260, 250, 240, 230, 220, 210, 200],
    'Product B': [150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370],
    'Product C': [250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Product', value_name='Sales')

# Create the line plot
plt.figure(figsize=(14, 7))
sns.lineplot(data=df_melted, x='Month', y='Sales', hue='Product',
             palette=['#FF0000', '#00FF00', '#0000FF'])

# Add annotations for the start and end of each line
for product in ['Product A', 'Product B', 'Product C']:
    plt.text(x=df['Month'][0], y=df[product][0], s=f"{df[product][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[product].iloc[-1],
             s=f"{df[product].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly Sales of Product Categories in 2024 (Units)', loc='left', fontsize=15)
plt.xlabel('Month')
plt.ylabel('Number of Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()