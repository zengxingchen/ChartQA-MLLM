
import matplotlib.pyplot as plt

# Data
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'San Francisco', 'Seattle', 'Boston', 'Austin', 'Denver', 'Washington', 'Miami', 'Atlanta']
gyms = [500, 350, 230, 180, 150, 200, 140, 130, 170, 120, 110, 115, 105, 130, 125, 140, 160, 150]
membership_cost = [45, 42, 38, 35, 40, 44, 34, 46, 39, 47, 50, 48, 49, 41, 42, 43, 46, 44]
city_population = [8.4, 3.9, 2.7, 2.3, 1.6, 1.6, 1.5, 1.4, 1.3, 1.0, 0.9, 0.8, 0.7, 1.0, 0.7, 0.7, 0.5, 0.5]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#A533FF', '#33FFD5', '#FFD533', '#FF5733', '#33A5FF', '#FF3380', '#3380FF', '#FF5733', '#FF3333', '#33A533', '#A53333', '#FFD533', '#33D5FF', '#33FF57']

# Bubble chart
plt.figure(figsize=(16, 12))
for idx, city in enumerate(cities):
    plt.scatter(city_population[idx], gyms[idx], s=membership_cost[idx]*30, c=colors[idx], label=city, alpha=0.6, edgecolors='w')

# Add titles and labels
plt.title('Number of Gyms and Average Membership Cost in Major US Cities', fontsize=20, pad=20)
plt.xlabel('City Population (Millions)', fontsize=16)
plt.ylabel('Number of Gyms', fontsize=16)

# Additional settings
plt.grid(True)
plt.legend(loc='upper right', title='Cities', bbox_to_anchor=(1.25, 1))
plt.xlim(0.3, 9)
plt.ylim(90, 550)

# Show plot
plt.tight_layout()
plt.show()