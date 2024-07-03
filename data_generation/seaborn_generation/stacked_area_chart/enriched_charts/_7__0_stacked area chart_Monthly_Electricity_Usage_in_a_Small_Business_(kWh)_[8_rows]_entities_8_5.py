
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Prepare the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'],
    'Fruits': [1200, 1300, 1250, 1350, 1400, 1500, 1600, 1700, 1650, 1750, 1800, 1900],
    'Vegetables': [1800, 1900, 1850, 1950, 2000, 2100, 2200, 2300, 2250, 2350, 2400, 2500],
    'Grains': [1400, 1500, 1450, 1550, 1600, 1700, 1800, 1900, 1850, 1950, 2000, 2100]
}

df = pd.DataFrame(data)

# Create a new DataFrame for plotting
df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Sales')

# Convert month to categorical type to ensure correct order in plotting
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=data['Month'], ordered=True)

# Plotting
plt.figure(figsize=(14, 10))
sns.set(style="whitegrid")

colors = ["#FFA07A", "#20B2AA", "#778899"]  # Fruits, Vegetables, Grains

# Draw plot
sns.lineplot(data=df_melted, x='Month', y='Sales', hue='Category', palette=colors, 
             sort=False, lw=2)

# Fill area
plt.fill_between(data['Month'], df["Fruits"], color="#FFA07A", alpha=0.5)
plt.fill_between(data['Month'], df["Fruits"], df["Fruits"] + df["Vegetables"], color="#20B2AA", alpha=0.5)
plt.fill_between(data['Month'], df["Fruits"] + df["Vegetables"], df["Fruits"] + df["Vegetables"] + df["Grains"], color="#778899", alpha=0.5)

# Adding Text Labels
for idx, month in enumerate(data['Month']):
    plt.text(x=idx, y=df.loc[idx, "Fruits"]/2, s=df.loc[idx, "Fruits"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Fruits"]+df.loc[idx, "Vegetables"]/2, s=df.loc[idx, "Vegetables"], ha='center', color='black')
    plt.text(x=idx, y=df.loc[idx, "Fruits"]+df.loc[idx, "Vegetables"]+df.loc[idx, "Grains"]/2, s=df.loc[idx, "Grains"], ha='center', color='black')

# Customizing the labels and title
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales by Food Category', pad=20)
plt.xticks(rotation=45)
plt.legend(loc='upper right')

# Show the plot
plt.tight_layout()
plt.show()