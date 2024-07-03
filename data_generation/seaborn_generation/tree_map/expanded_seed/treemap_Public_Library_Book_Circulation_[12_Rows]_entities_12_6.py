
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Raw data
data = [
    {'Category': 'Fiction', 'Books_Loaned': 500, 'Month': 'January', 'Library_Branch': 'Main'},
    {'Category': 'Non-Fiction', 'Books_Loaned': 300, 'Month': 'January', 'Library_Branch': 'Main'},
    {'Category': "Children's Literature", 'Books_Loaned': 350, 'Month': 'January', 'Library_Branch': 'Main'},
    {'Category': 'Young Adult', 'Books_Loaned': 250, 'Month': 'January', 'Library_Branch': 'West End'},
    {'Category': 'Fiction', 'Books_Loaned': 400, 'Month': 'February', 'Library_Branch': 'Main'},
    {'Category': 'Non-Fiction', 'Books_Loaned': 220, 'Month': 'February', 'Library_Branch': 'Main'},
    {'Category': "Children's Literature", 'Books_Loaned': 370, 'Month': 'February', 'Library_Branch': 'Main'},
    {'Category': 'Young Adult', 'Books_Loaned': 290, 'Month': 'February', 'Library_Branch': 'West End'},
    {'Category': 'Fiction', 'Books_Loaned': 450, 'Month': 'March', 'Library_Branch': 'Main'},
    {'Category': 'Non-Fiction', 'Books_Loaned': 310, 'Month': 'March', 'Library_Branch': 'Main'},
    {'Category': "Children's Literature", 'Books_Loaned': 400, 'Month': 'March', 'Library_Branch': 'Main'},
    {'Category': 'Young Adult', 'Books_Loaned': 270, 'Month': 'March', 'Library_Branch': 'West End'}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Set Seaborn style
sns.set(style="whitegrid")

# Compute the treemap data
sizes = df['Books_Loaned'].values
labels = df.apply(lambda x: f"{x['Category']} ({x['Month']})\n{str(x['Books_Loaned'])}", axis=1)
colors = sns.color_palette('pastel', len(data))

# Create the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, alpha=0.8, color=colors)

# Additional plot configurations
plt.axis('off')
plt.title('Library Books Loaned by Category and Month')
plt.show()