
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Language': ['Python', 'JavaScript', 'Java', 'C#', 'PHP', 'C++', 'Ruby'],
    'Developers': [1500, 1300, 950, 700, 500, 450, 100],
    'Share': [0.27, 0.24, 0.17, 0.13, 0.09, 0.08, 0.02]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700', '#FFA07A', '#8A2BE2']

# Plot the Treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=df['Share'], label=df['Language'], color=colors, alpha=0.7)
plt.title('Programming Language Popularity in a Developer Community', fontsize=18)
plt.axis('off')
plt.show()