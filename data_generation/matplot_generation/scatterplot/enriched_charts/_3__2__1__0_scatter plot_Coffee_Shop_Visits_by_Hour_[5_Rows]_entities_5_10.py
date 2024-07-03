
import matplotlib.pyplot as plt

# Data for scatterplot
countries = ["USA", "China", "Japan", "Germany", "India", "Australia", "UK", 
             "Russia", "Brazil", "France", "Canada", "Italy", "Spain", 
             "South Korea", "Mexico", "Turkey", "Netherlands", "Greece", 
             "Argentina", "Nigeria"]
gold_medals = [45, 38, 27, 22, 20, 23, 18, 17, 16, 14, 12, 13, 11, 10, 9, 8, 7, 6, 5, 4]
average_cost_per_medal = [37.5, 28.4, 29.3, 32.7, 25.0, 31.5, 30.2, 27.8, 24.5, 33.1, 34.7, 26.9, 25.4, 35.0, 22.3, 23.6, 28.9, 24.1, 21.8, 22.0]

# Create scatterplot
plt.figure(figsize=(16, 12))
plt.scatter(gold_medals, average_cost_per_medal, c=[
    '#FF5733', '#33FF57', '#3357FF', '#57FFF3', '#F3FF57',
    '#FF33FB', '#33FFF8', '#B833FF', '#FF5733', '#33FF57',
    '#3357FF', '#57FFF3', '#F3FF57', '#FF33FB', '#33FF57',
    '#FFAB33', '#33ABFF', '#5733FF', '#FF5733', '#33FF57'], s=100)

# Customize plot
plt.title('Gold Medals vs. Average Cost per Medal in Major Countries', fontsize=18, pad=20)
plt.xlabel('Gold Medals', fontsize=14)
plt.ylabel('Average Cost per Medal (in million USD)', fontsize=14)

# Annotate data points
for i, country in enumerate(countries):
    plt.annotate(country, (gold_medals[i], average_cost_per_medal[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

# Show plot
plt.show()