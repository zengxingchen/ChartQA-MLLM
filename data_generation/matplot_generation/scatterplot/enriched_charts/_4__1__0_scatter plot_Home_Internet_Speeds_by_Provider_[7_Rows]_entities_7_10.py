
import matplotlib.pyplot as plt

species = ["African Elephant", "Amur Leopard", "Bengal Tiger", "Blue Whale", "Giant Panda", "Green Sea Turtle", "Mountain Gorilla", "Snow Leopard", "Sumatran Orangutan", "Vaquita", "Javan Rhino", "Hawksbill Turtle", "African Wild Dog", "Asian Elephant", "Borneo Pygmy Elephant", "Chimpanzee", "Ganges River Dolphin", "Saola", "Iberian Lynx", "Cross River Gorilla"]
population = [415000, 84, 2500, 10000, 1864, 8500, 1063, 4000, 14700, 10, 74, 23000, 6600, 50000, 1500, 170000, 1800, 750, 400, 250]
conservation_funding = [120000000, 12000000, 70000000, 150000000, 100000000, 50000000, 85000000, 30000000, 45000000, 20000000, 25000000, 40000000, 10000000, 30000000, 15000000, 55000000, 5000000, 8000000, 20000000, 10000000]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FFC300', '#DAF7A6', '#FF33D4', '#900C3F', '#581845', '#C70039', '#FF5733', '#33FF57', '#3357FF', '#FFC300', '#DAF7A6', '#FF33D4', '#900C3F', '#581845', '#C70039', '#FF5733', '#33FF57']

plt.figure(figsize=(14, 8))

for i in range(len(species)):
    plt.scatter(population[i], conservation_funding[i], color=colors[i], label=species[i])

plt.title('Wildlife Populations vs Conservation Funding', pad=20)
plt.xlabel('Population Size')
plt.ylabel('Conservation Funding (USD)')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))

plt.show()