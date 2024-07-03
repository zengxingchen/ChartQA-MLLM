
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Topic': ['Art', 'Music', 'Literature', 'Fashion', 'Travel', 'Food', 'Tech Gadgets', 'Home Decor',
              'Wellness', 'Fitness', 'Photography', 'Outdoor Gear', 'Games', 'Beauty', 'Crafts', 'Pets',
              'Entertainment', 'Gifts'],
    'Total Sales (USD)': [30000, 50000, 20000, 45000, 35000, 60000, 55000, 40000, 25000, 48000, 32000, 36000, 52000, 41000, 28000, 44000, 47000, 37000],
    'Number of Items': [120, 150, 80, 130, 110, 180, 160, 140, 100, 135, 125, 115, 170, 145, 105, 150, 155, 130],
    'Popularity': [8, 10, 6, 9, 7, 10, 9, 8, 7, 9, 8, 7, 10, 9, 7, 9, 9, 8]
}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
bubble_chart = sns.scatterplot(
    data=df,
    x="Number of Items",
    y="Total Sales (USD)",
    size="Popularity",
    sizes=(100, 1000),
    hue="Popularity",
    palette=["#ff5733", "#33ff57", "#3357ff", "#ff33a6", "#33fff7", "#f7ff33", "#8c33ff", "#33ff83",
             "#5733ff", "#a633ff"],
    alpha=0.7,
    legend='full'
)

bubble_chart.set_title("Sales Analysis by Topic: Items vs Sales vs Popularity")
bubble_chart.set_xlabel("Number of Items")
bubble_chart.set_ylabel("Total Sales (USD)")

plt.show()