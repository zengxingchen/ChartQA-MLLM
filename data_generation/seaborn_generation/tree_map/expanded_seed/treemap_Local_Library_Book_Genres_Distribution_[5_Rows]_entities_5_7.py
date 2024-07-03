
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Define the dataset
data = [
    {'Genre': 'Mystery', 'Books Available': 320, 'Books Borrowed': 150},
    {'Genre': 'Science Fiction', 'Books Available': 280, 'Books Borrowed': 110},
    {'Genre': 'Romance', 'Books Available': 450, 'Books Borrowed': 210},
    {'Genre': 'Non-Fiction', 'Books Available': 700, 'Books Borrowed': 300},
    {'Genre': "Children's Literature", 'Books Available': 500, 'Books Borrowed': 450}
]

# Create a DataFrame
df = pd.DataFrame(data)

# Prepare data
sizes = df['Books Available']  # sizes for the squares
labels = df.apply(lambda x: f"{x['Genre']}\nAvailable: {x['Books Available']}\nBorrowed: {x['Books Borrowed']}", axis=1)
colors = sns.color_palette('pastel', len(data))  # get a color palette from seaborn

# Treemap plotting
sns.set(style="whitegrid")  # set seaborn style
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
plt.title('Library Genre Treemap')

# Remove axes
plt.axis('off')

# Optional: save the figure
# plt.savefig("treemap.png")

# Show plot
plt.show()