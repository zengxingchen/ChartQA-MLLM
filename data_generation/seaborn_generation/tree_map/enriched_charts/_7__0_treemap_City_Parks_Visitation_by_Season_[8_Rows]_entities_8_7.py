
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Let's define our dataframe
data = {
    'Topic': ['Reading', 'Writing', 'Poetry', 'Fiction', 'Non-fiction', 'Biography', 'Essays', 'Drama', 'Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Memoir', 'History'],
    'Percentage': [20, 15, 10, 18, 12, 8, 5, 4, 3, 5, 6, 3, 7, 4]
}

df = pd.DataFrame(data)

# Define color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#A833FF', '#33FFF0', '#F0FF33', '#FF8333', '#33FFA8', '#A8FF33', '#33A8FF', '#FF5733', '#57FF33', '#5733FF']

# Plot
plt.figure(figsize=(18, 9))
squarify.plot(sizes=df['Percentage'], label=df['Topic'], color=colors, alpha=0.8)

plt.title('Interest in Different Literary Genres in 2023', fontsize=16)
plt.axis('off')

plt.show()