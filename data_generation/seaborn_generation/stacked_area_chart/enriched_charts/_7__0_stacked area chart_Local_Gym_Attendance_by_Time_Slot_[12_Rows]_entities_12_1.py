
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Science Fiction': [400, 450, 500, 520, 530, 550, 580, 600, 620, 650, 670, 700],
    'Romance': [600, 650, 700, 720, 750, 780, 800, 850, 870, 900, 920, 950],
    'Mystery': [500, 550, 600, 630, 670, 700, 730, 750, 770, 800, 820, 850],
    'Biography': [200, 210, 220, 230, 250, 260, 270, 280, 290, 300, 320, 350],
}

df = pd.DataFrame(data)

# Define a color palette
palette = ["#4c72b0","#55a868","#c44e52","#8172b3"]

# Melt DataFrame
df_melted = df.melt('Month', var_name='Category', value_name='Sales')

# Plot
plt.figure(figsize=(16, 8))

# Area plot
sns.set_style("whitegrid")
df.set_index('Month').plot(kind='area', stacked=True, color=palette, alpha=0.6, figsize=(16, 8))

# Customization
plt.title('Monthly Book Sales Data by Genre', fontsize=18, y=1.05)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Sales Amount', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Book Genres', bbox_to_anchor=(1.05, 1), loc='upper left')

# Annotations
for i, category in enumerate(df.columns[1:]):
    y = df[category].cumsum() - (0.5 * df[category])
    for x, value in enumerate(y):
        if x == len(df) - 1:
            plt.text(x, value, f'{category}', fontsize=10, ha='left', va='center')

plt.tight_layout()
plt.show()