
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022', '2022',
             '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023', '2023'],
    "Category": ['Novels', 'Poetry', 'Drama', 'Essays', 'Biographies', 'Short Stories', 'Non-Fiction', 'Graphic Novels', 'Fantasy',
                 'Novels', 'Poetry', 'Drama', 'Essays', 'Biographies', 'Short Stories', 'Non-Fiction', 'Graphic Novels', 'Fantasy',
                 'Novels', 'Poetry', 'Drama', 'Essays', 'Biographies', 'Short Stories', 'Non-Fiction', 'Graphic Novels', 'Fantasy'],
    "Value": [12.5, 18.2, 15.4, 10.1, 9.3, 7.2, 5.6, 8.9, 6.4,
              13.0, 19.0, 16.0, 10.5, 9.7, 7.5, 6.0, 9.2, 6.7,
              13.5, 20.0, 17.0, 11.0, 10.0, 8.0, 6.5, 9.5, 7.0]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(20, 15))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FFD700', '#FF6F61', '#00CED1', '#8A2BE2']

# Treemap plot
squarify.plot(sizes=df["Value"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Literature Consumption (2021-2023)", fontsize=24, color='#333333', pad=30, loc='left')
plt.axis('off')
plt.show()