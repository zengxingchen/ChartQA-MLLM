
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': [
        'China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Canada', 'Brazil', 
        'South Korea', 'France', 'United Kingdom', 'Italy', 'Australia', 'Spain', 'Mexico', 
        'South Africa', 'Saudi Arabia', 'Turkey', 'Indonesia', 'Egypt', 'Iran', 'Thailand', 
        'Vietnam', 'Argentina'
    ],
    'Electricity Generation (TWh)': [
        7500, 4500, 2000, 1100, 1000, 700, 600, 500, 
        600, 550, 450, 300, 250, 280, 200, 
        190, 180, 170, 160, 150, 140, 130, 
        120, 110
    ],
    'Renewable Sources': [
        3000, 1500, 800, 200, 150, 500, 400, 450, 
        100, 300, 250, 200, 150, 180, 100, 
        50, 20, 70, 40, 30, 10, 60, 
        50, 40
    ]
}
df = pd.DataFrame(data)

sns.set(style="whitegrid")
plt.figure(figsize=(14, 8))

barplot = sns.barplot(
    x="Country",
    y="Electricity Generation (TWh)",
    data=df,
    palette=[
        '#FF5733', '#33FF57', '#3357FF', '#F333FF', '#FF3333', 
        '#33FFF3', '#FFF333', '#FF8333', '#33FF83', '#8333FF', 
        '#FF33A3', '#33A3FF', '#A3FF33', '#FF5733', '#33FF57', 
        '#3357FF', '#F333FF', '#FF3333', '#33FFF3', '#FFF333', 
        '#FF8333', '#33FF83', '#8333FF', '#FF33A3'
    ],
    ci=None
)

barplot.set_title('Top Countries by Electricity Generation (2023)', fontsize=16, pad=20)
barplot.bar_label(barplot.containers[0], fmt='%.0f', fontsize=10)
barplot.set(xlabel="Country", ylabel="Electricity Generation (TWh)")
barplot.set_xticklabels(barplot.get_xticklabels(), rotation=45, ha="right")

for bar in barplot.containers[0]:
    bar.set_width(0.4)

plt.tight_layout()
plt.show()