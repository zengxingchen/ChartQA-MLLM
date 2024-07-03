
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create data
data = {
    'Month': ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"],
    'Gym A': [100, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310],
    'Gym B': [150, 160, 180, 200, 220, 240, 260, 270, 280, 290, 300, 310],
    'Gym C': [200, 190, 220, 250, 280, 300, 310, 320, 330, 340, 350, 360]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame
df_melted = df.melt('Month', var_name='Gym', value_name='Signups')

# Create the line plot
plt.figure(figsize=(18, 10))
sns.lineplot(data=df_melted, x='Month', y='Signups', hue='Gym',
             palette=['#FF6F61', '#6B5B95', '#88B04B'])

# Add annotations for the start and end of each line
for gym in ['Gym A', 'Gym B', 'Gym C']:
    plt.text(x=df['Month'][0], y=df[gym][0], s=f"{df[gym][0]} (Start)",
             color='black', ha='center', va='bottom')
    plt.text(x=df['Month'].iloc[-1], y=df[gym].iloc[-1],
             s=f"{df[gym].iloc[-1]} (End)", color='black', ha='center', va='bottom')

plt.title('Monthly Gym Membership Signups in 2024', loc='center', fontsize=20)
plt.xlabel('Month')
plt.ylabel('Number of Signups')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()