
import matplotlib.pyplot as plt

countries = [
    "China", "United States", "India", "Japan", "Germany", "United Kingdom",
    "France", "Brazil", "Italy", "Canada", "South Korea", "Russia",
    "Australia", "Mexico", "Indonesia", "Netherlands", "Saudi Arabia", 
    "Turkey", "Spain", "Switzerland"
]
revenues = [
    1400, 1300, 800, 700, 600, 500, 450, 400, 350, 300, 280, 260, 250, 240, 
    230, 220, 210, 200, 190, 180
]

plt.figure(figsize=(16, 10))
plt.bar(countries, revenues, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#aec7e8', '#ffbb78',
    '#98df8a', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d2', '#c7c7c7',
    '#dbdb8d', '#9edae5'], width=0.6)

plt.ylabel('Revenue (Billion USD)', fontsize=14)
plt.title('Top 20 Countries by Company Revenue', fontsize=16, pad=20)
plt.ylim(0, 1500)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()