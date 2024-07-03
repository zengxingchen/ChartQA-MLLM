
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022',
             '2023', '2023', '2023', '2023', '2023', '2023'],
    "Genre": ['Fiction', 'Non-Fiction', 'Mystery', 'Romance', 'Science Fiction', 'Fantasy',
              'Fiction', 'Non-Fiction', 'Mystery', 'Romance', 'Science Fiction', 'Fantasy',
              'Fiction', 'Non-Fiction', 'Mystery', 'Romance', 'Science Fiction', 'Fantasy'],
    "Market Share": [45.12, 20.34, 10.56, 8.23, 5.67, 10.08,
                     47.23, 21.14, 9.45, 8.56, 5.45, 8.17,
                     48.87, 22.04, 8.34, 9.56, 5.23, 6.67]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(16, 10))
colors = ['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f', '#edc948']

# Treemap plot
squarify.plot(sizes=df["Market Share"], label=df["Genre"], color=colors, alpha=0.8)
plt.title("Book Genre Market Share (2021-2023)", fontsize=18, color='#333333')
plt.axis('off')
plt.show()