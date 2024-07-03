
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022'],
    "Category": ['Online Learning Platforms', 'Virtual Classrooms', 'E-books', 'Educational Software', 'Interactive Whiteboards',
                 'Online Learning Platforms', 'Virtual Classrooms', 'E-books', 'Educational Software', 'Interactive Whiteboards',
                 'Online Learning Platforms', 'Virtual Classrooms', 'E-books', 'Educational Software', 'Interactive Whiteboards',
                 'Online Learning Platforms', 'Virtual Classrooms', 'E-books', 'Educational Software', 'Interactive Whiteboards'],
    "Investment": [250.5, 190.3, 130.2, 120.7, 95.8,
                   290.4, 210.9, 140.7, 150.1, 105.4,
                   320.5, 225.6, 155.2, 165.3, 115.9,
                   350.7, 240.8, 170.3, 180.2, 125.5]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(20, 14))
colors = ['#3498DB', '#1ABC9C', '#E74C3C', '#9B59B6', '#F1C40F', 
          '#2ECC71', '#E67E22', '#34495E', '#D35400', '#C0392B']

# Treemap plot
squarify.plot(sizes=df["Investment"], label=df["Category"], color=colors, alpha=0.8)
plt.title("Investment in Education Technology (2019-2022)", fontsize=24, color='#333333', y=1.05)
plt.axis('off')
plt.show()