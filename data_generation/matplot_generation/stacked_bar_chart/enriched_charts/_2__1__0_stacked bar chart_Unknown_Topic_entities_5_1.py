
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
books_published = [120, 130, 110, 140, 150, 160, 170, 180, 190, 200, 210, 220]
authors = [25, 30, 22, 28, 35, 38, 40, 42, 45, 50, 55, 60]
sales = [450, 470, 430, 480, 500, 520, 540, 560, 580, 600, 620, 640]
awards_won = [5, 8, 6, 7, 9, 10, 11, 12, 14, 15, 16, 18]

plt.figure(figsize=(14, 8))  
bar_width = 0.6  

plt.barh(months, books_published, color='#1f77b4', edgecolor='white', height=bar_width, label='Books Published')
plt.barh(months, authors, left=books_published, color='#ff7f0e', edgecolor='white', height=bar_width, label='Authors')
plt.barh(months, sales, left=[i+j for i,j in zip(books_published, authors)], color='#2ca02c', edgecolor='white', height=bar_width, label='Sales (in Thousands)')
plt.barh(months, awards_won, left=[i+j+k for i,j,k in zip(books_published, authors, sales)], color='#d62728', edgecolor='white', height=bar_width, label='Awards Won')

for i, (b, a, s, aw) in enumerate(zip(books_published, authors, sales, awards_won)):
    plt.text(b/2, i, str(b), ha='center', va='center', color='white', fontweight='bold')
    plt.text(b+a/2, i, str(a), ha='center', va='center', color='white', fontweight='bold')
    plt.text(b+a+s/2, i, str(s), ha='center', va='center', color='white', fontweight='bold')
    plt.text(b+a+s+aw/2, i, str(aw), ha='center', va='center', color='white', fontweight='bold')

plt.xlabel('Metrics')  
plt.title('Monthly Book Publishing Metrics', pad=20)  
plt.yticks(rotation=0)  
plt.legend(loc='upper right')

plt.show()