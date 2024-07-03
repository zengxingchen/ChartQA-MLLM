
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = [
    {'MemberID': 1, 'Borrowed Books': 5},
    {'MemberID': 2, 'Borrowed Books': 7},
    {'MemberID': 3, 'Borrowed Books': 12},
    {'MemberID': 4, 'Borrowed Books': 3},
    {'MemberID': 5, 'Borrowed Books': 15},
    {'MemberID': 6, 'Borrowed Books': 9},
    {'MemberID': 7, 'Borrowed Books': 2},
    {'MemberID': 8, 'Borrowed Books': 18},
    {'MemberID': 9, 'Borrowed Books': 22},
    {'MemberID': 10, 'Borrowed Books': 0},
    {'MemberID': 11, 'Borrowed Books': 6},
    {'MemberID': 12, 'Borrowed Books': 9},
    {'MemberID': 13, 'Borrowed Books': 10},
    {'MemberID': 14, 'Borrowed Books': 7},
    {'MemberID': 15, 'Borrowed Books': 5}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Set the style and palette
sns.set(style="whitegrid")
palette = sns.color_palette("coolwarm", n_colors=15)

# Create the histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df,
             x='Borrowed Books',
             bins=8,  # select number of bins
             kde=False,  # no density plot
             color='skyblue',
             edgecolor='gray',
             palette=palette,
             alpha=0.8)

# Set titles and labels
plt.title('Histogram of Borrowed Books per Member')
plt.xlabel('Number of Borrowed Books')
plt.ylabel('Number of Members')

# Customize ticks, if necessary
plt.xticks(range(0, 25, 1))
plt.yticks(range(0, 5, 1))

# Show the plot
plt.show()