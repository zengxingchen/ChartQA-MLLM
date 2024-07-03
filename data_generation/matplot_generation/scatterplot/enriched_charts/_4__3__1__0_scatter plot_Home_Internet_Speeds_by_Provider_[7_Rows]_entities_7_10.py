
import matplotlib.pyplot as plt

country = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy", "Spain", "Australia", "Brazil", "Argentina", "China", "Japan", "South Korea", "India", "Russia", "South Africa", "Egypt", "Saudi Arabia", "Nigeria"]
happiness_index = [7.2, 7.5, 6.5, 7.0, 7.1, 6.9, 6.7, 6.8, 7.3, 6.2, 5.8, 5.4, 5.9, 6.0, 4.8, 5.6, 4.7, 4.2, 6.1, 4.5]
gdp_per_capita = [60000, 48000, 18000, 42000, 46000, 43000, 35000, 30000, 50000, 15000, 11000, 16000, 38000, 33000, 7000, 12000, 6000, 3000, 21000, 2000]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#8A2BE2', '#FF4500', '#DA70D6', '#40E0D0', '#F08080', '#20B2AA', '#778899', '#87CEEB', '#FFB6C1', '#6A5ACD', '#708090', '#DB7093', '#CD5C5C', '#6495ED', '#B0C4DE', '#FF69B4']

plt.figure(figsize=(16, 9))

for i in range(len(country)):
    plt.scatter(happiness_index[i], gdp_per_capita[i], color=colors[i], label=country[i])

plt.title('Happiness Index vs GDP Per Capita in Various Countries', pad=20)
plt.xlabel('Happiness Index')
plt.ylabel('GDP Per Capita (USD)')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.show()