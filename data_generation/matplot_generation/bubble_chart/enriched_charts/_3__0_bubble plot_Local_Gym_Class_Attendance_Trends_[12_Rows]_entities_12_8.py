
import matplotlib.pyplot as plt

countries = ["France", "Spain", "United States", "China", "Italy",
             "Turkey", "Mexico", "Thailand", "Germany", "United Kingdom",
             "Japan", "Austria", "Russia", "Canada", "Australia",
             "Netherlands", "Switzerland", "Greece", "Portugal", "India"]
tourist_arrivals = [89000, 82000, 77000, 65000, 62000, 
                    51000, 45000, 40000, 39000, 37000, 
                    35000, 30000, 29000, 28000, 27000,
                    22000, 21000, 20000, 19000, 17000]  # in thousands
population = [65, 47, 331, 1439, 60, 
              84, 129, 70, 83, 68, 
              126, 9, 146, 38, 25,
              17, 9, 10, 10, 1380]  # in millions
happiness_index = [6.5, 6.4, 6.9, 5.8, 6.0, 
                   5.2, 6.2, 6.0, 6.6, 6.8, 
                   6.0, 7.1, 5.5, 7.4, 7.3,
                   7.1, 7.5, 5.8, 6.0, 4.5]

sizes = [h * 100 for h in happiness_index]

plt.figure(figsize=(16, 12))
for i in range(len(countries)):
    plt.scatter(tourist_arrivals[i], population[i], s=sizes[i], alpha=0.6,
                c=['#FF6347' if happiness_index[i] >= 7 else '#4682B4'])

plt.title('Tourist Arrivals vs Population Size with Happiness Index as Bubble Size', pad=20)
plt.xlabel('Tourist Arrivals (in Thousands)')
plt.ylabel('Population (in Millions)')
plt.grid(True)

for i, country in enumerate(countries):
    plt.annotate(country, (tourist_arrivals[i], population[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center')

plt.show()