
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
electronics = [20, 18, 25, 10, 15, 20, 18, 22, 25, 10, 15, 20]
fashion = [15, 20, 15, 25, 20, 20, 15, 23, 10, 30, 20, 18]
home_living = [25, 22, 20, 30, 25, 20, 25, 20, 25, 30, 20, 28]
books = [10, 15, 10, 5, 15, 10, 10, 5, 15, 10, 20, 12]
sports_outdoors = [20, 15, 20, 20, 15, 20, 20, 20, 15, 10, 15, 12]
beauty_health = [10, 10, 10, 10, 10, 10, 12, 10, 10, 10, 10, 10]

bar_height = 0.8

fig, ax = plt.subplots(figsize=(14, 8))

# Bottom values for stacking
bar_fashion = list(electronics)
bar_home = [i + j for i, j in zip(bar_fashion, fashion)]
bar_books = [i + j for i, j in zip(bar_home, home_living)]
bar_sports = [i + j for i, j in zip(bar_books, books)]
bar_beauty = [i + j for i, j in zip(bar_sports, sports_outdoors)]

# Stacked bars
plt.barh(months, electronics, color='#1f77b4', edgecolor='white', height=bar_height)
plt.barh(months, fashion, left=bar_fashion, color='#ff7f0e', edgecolor='white', height=bar_height)
plt.barh(months, home_living, left=bar_home, color='#2ca02c', edgecolor='white', height=bar_height)
plt.barh(months, books, left=bar_books, color='#d62728', edgecolor='white', height=bar_height)
plt.barh(months, sports_outdoors, left=bar_sports, color='#9467bd', edgecolor='white', height=bar_height)
plt.barh(months, beauty_health, left=bar_beauty, color='#8c564b', edgecolor='white', height=bar_height)

# Labels
plt.xlabel('Percentage (%)')
plt.title('Monthly Sales Distribution Across Different Product Categories')
plt.yticks(months)
plt.xticks(range(0, 101, 10))

# Show percentages on the bars
for i in range(len(months)):
    plt.text(electronics[i] / 2, i, str(electronics[i]) + '%', ha = 'center', va= 'center', color='white', fontsize=8)
    plt.text(bar_fashion[i] + fashion[i] / 2, i, str(fashion[i]) + '%', ha = 'center', va= 'center', color='white', fontsize=8)
    plt.text(bar_home[i] + home_living[i] / 2, i, str(home_living[i]) + '%', ha = 'center', va= 'center', color='white', fontsize=8)
    plt.text(bar_books[i] + books[i] / 2, i, str(books[i]) + '%', ha = 'center', va= 'center', color='white', fontsize=8)
    plt.text(bar_sports[i] + sports_outdoors[i] / 2, i, str(sports_outdoors[i]) + '%', ha = 'center', va= 'center', color='white', fontsize=8)
    plt.text(bar_beauty[i] + beauty_health[i] / 2, i, str(beauty_health[i]) + '%', ha = 'center', va= 'center', color='white', fontsize=8)

# Show the plot
plt.show()