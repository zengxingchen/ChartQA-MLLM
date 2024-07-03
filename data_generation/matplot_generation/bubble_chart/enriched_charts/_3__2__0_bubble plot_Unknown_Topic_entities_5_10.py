
import matplotlib.pyplot as plt

countries = ["United States", "Germany", "Brazil", "Canada", "Australia", "Japan", 
             "United Kingdom", "China", "South Korea", "India", "Italy", "France", 
             "Spain", "Russia", "Mexico", "Indonesia", "South Africa", "Saudi Arabia", 
             "Turkey", "Argentina"]
num_books = [50000, 12000, 35000, 10000, 8000, 15000, 13000, 70000, 9000, 30000, 9000, 
             11000, 10000, 18000, 15000, 25000, 7000, 5000, 14000, 8000]
avg_price = [25, 18, 15, 22, 28, 20, 30, 12, 24, 10, 19, 21, 23, 14, 13, 11, 17, 26, 
             16, 15]
monthly_sales = [60000, 15000, 22000, 12000, 7000, 17000, 14000, 80000, 10000, 40000, 
                 6000, 8000, 7000, 12000, 10000, 20000, 5000, 4000, 9000, 6000]

fig, ax = plt.subplots(figsize=(14, 8))

colors = {
    "United States": "#FF5733", "Germany": "#33FF57", "Brazil": "#3357FF", 
    "Canada": "#FFFF33", "Australia": "#FF33FF", "Japan": "#57FFF3", 
    "United Kingdom": "#F357FF", "China": "#F3573C", "South Korea": "#3CF357", 
    "India": "#5733FF", "Italy": "#33FF95", "France": "#FF3357", "Spain": "#33F3FF", 
    "Russia": "#FF9533", "Mexico": "#3C57F3", "Indonesia": "#95FF33", 
    "South Africa": "#33F3F3", "Saudi Arabia": "#F333FF", "Turkey": "#FF3C57", 
    "Argentina": "#F39533"
}

for i, country in enumerate(countries):
    ax.scatter(num_books[i], avg_price[i], s=monthly_sales[i]*0.05, 
               c=colors[country], alpha=0.6, edgecolors="w", label=country)

ax.set_title('Book Distribution, Price, and Monthly Sales by Country', fontsize=18, pad=20)
ax.set_xlabel('Number of Books', fontsize=14)
ax.set_ylabel('Average Price in USD', fontsize=14)

ax.grid(True)

ax.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

plt.tight_layout()
plt.show()