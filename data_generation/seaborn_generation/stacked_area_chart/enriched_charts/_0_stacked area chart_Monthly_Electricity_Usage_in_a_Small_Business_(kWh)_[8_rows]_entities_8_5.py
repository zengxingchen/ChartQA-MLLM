
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Electronics': [2000, 2100, 1900, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000],
    'Books': [1500, 1600, 1700, 1650, 1750, 1600, 1550, 1500, 1650, 1700, 1800, 1900],
    'Clothing': [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100]
}

df = pd.DataFrame(data)

# Create a new DataFrame for plotting
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Sales')

# Convert month to categorical type to ensure correct order in plotting
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

colors = ["#FF5733", "#33FF57", "#3357FF"]  # Electronics, Books, Clothing

# Draw plot
sns.lineplot(data=df_melted, x='Month', y='Sales', hue='Category', palette=colors, 
             sort=False, lw=2)

# Fill area
plt.fill_between(data['Month'], df["Electronics"], color="#FF5733", alpha=0.5)
plt.fill_between(data['Month'], df["Electronics"], df["Electronics"] + df["Books"], color="#33FF57", alpha=0.5)
plt.fill_between(data['Month'], df["Electronics"] + df["Books"], df["Electronics"] + df["Books"] + df["Clothing"], color="#3357FF", alpha=0.5)

# Adding Text Labels
for idx, month in enumerate(data['Month']):
    if idx % 2 == 0:  # annotate every other month for clarity
        plt.text(x=idx, y=df.loc[idx, "Electronics"]/2, s=df.loc[idx, "Electronics"], ha='center', color='w')
        plt.text(x=idx, y=df.loc[idx, "Electronics"]+df.loc[idx, "Books"]/2, s=df.loc[idx, "Books"], ha='center', color='w')
        plt.text(x=idx, y=df.loc[idx, "Electronics"]+df.loc[idx, "Books"]+df.loc[idx, "Clothing"]/2, s=df.loc[idx, "Clothing"], ha='center', color='w')

# Customizing the labels and title
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales by Product Category')
plt.xticks(rotation=45)
plt.legend(loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()