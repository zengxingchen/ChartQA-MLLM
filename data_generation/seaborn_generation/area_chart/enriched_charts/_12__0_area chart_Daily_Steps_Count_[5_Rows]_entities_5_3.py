
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Books_Sold': [450, 510, 620, 580, 690, 720, 810, 750, 680, 770, 850, 910]
}

df = pd.DataFrame(data)

# Define the color palette as an array of hex color codes
colors = ["#1F77B4"]

# Plotting the area chart
plt.figure(figsize=(12, 7))  # Changed the width and height of the chart
ax = sns.lineplot(x='Month', y='Books_Sold', data=df, color=colors[0])
ax.fill_between(df['Month'], df['Books_Sold'], color=colors[0], alpha=0.3)

# Annotations
for i, point in df.iterrows():
    ax.text(point['Month'], point['Books_Sold'], str(point['Books_Sold']), 
            ha='center', va='bottom')

# Customizing with a title and labels
ax.set_title('Monthly Book Sales in 2023', fontsize=16)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Number of Books Sold', fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()