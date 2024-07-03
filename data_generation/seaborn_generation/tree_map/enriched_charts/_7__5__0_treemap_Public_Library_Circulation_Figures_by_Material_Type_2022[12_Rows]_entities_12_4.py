
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Subject': ['Fiction', 'Non-Fiction', 'Poetry', 'Drama', 'Fantasy', 'Romance', 'Thriller', 
               'Mystery', 'Biography', 'Autobiography', 'Classic', 'Adventure', 'Horror', 
               'Science Fiction', 'Historical', 'Memoir', 'Anthology'],
    'Participants': [500, 400, 350, 300, 250, 200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
    'Percentage': [0.20, 0.16, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.036, 0.032, 0.028, 0.024, 0.020, 0.016, 0.012, 0.008, 0.004]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', '#8D33FF', '#33FFF7', 
          '#FF3380', '#C70039', '#581845', '#900C3F', '#FFC300', '#DAF7A6', '#FF5733', 
          '#FFBD33', '#33FFBD', '#FF5733']

# Plot the Treemap
plt.figure(figsize=(16, 12))
squarify.plot(sizes=df['Percentage'], label=df['Subject'], color=colors, alpha=0.8)
plt.title('Popularity of Literature Genres among Readers', fontsize=22)
plt.axis('off')
plt.show()