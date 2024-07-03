
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data Frame
data = {
    "Year": ['2019', '2019', '2019', '2019', '2019', '2019', '2019',
             '2020', '2020', '2020', '2020', '2020', '2020', '2020',
             '2021', '2021', '2021', '2021', '2021', '2021', '2021',
             '2022', '2022', '2022', '2022', '2022', '2022', '2022'],
    "Company": ['Harvard', 'MIT', 'Stanford', 'Oxford', 'Cambridge', 'Columbia', 'Princeton',
                'Harvard', 'MIT', 'Stanford', 'Oxford', 'Cambridge', 'Columbia', 'Princeton',
                'Harvard', 'MIT', 'Stanford', 'Oxford', 'Cambridge', 'Columbia', 'Princeton',
                'Harvard', 'MIT', 'Stanford', 'Oxford', 'Cambridge', 'Columbia', 'Princeton'],
    "Students": [31.5, 22.3, 18.7, 23.1, 19.8, 17.4, 15.6,
                 32.8, 24.1, 19.9, 25.0, 20.4, 18.9, 16.8,
                 34.5, 25.7, 21.3, 26.5, 22.1, 20.0, 18.2,
                 36.2, 27.4, 22.8, 28.1, 23.7, 21.2, 19.6]
}
df = pd.DataFrame(data)

# Settings
plt.figure(figsize=(18, 12))
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5', '#FFC300', '#DAF7A6']

# Treemap plot
squarify.plot(sizes=df["Students"], label=df["Company"], color=colors, alpha=0.8)
plt.title("Top Universities' Student Enrollment (2019-2022)", fontsize=20, color='#555555', y=1.05)
plt.axis('off')
plt.show()