
import matplotlib.pyplot as plt

# Data for plotting
countries = ["Australia", "Brazil", "Canada", "China", "France",
             "Germany", "India", "Indonesia", "Italy", "Japan",
             "Mexico", "Netherlands", "Russia", "Saudi Arabia", "South Korea",
             "Spain", "Switzerland", "Turkey", "United Kingdom", "United States",
             "Nigeria", "Argentina", "Egypt", "Pakistan", "Vietnam"]
investment_renewable = [40, 30, 50, 200, 60,
                        80, 100, 25, 55, 90,
                        20, 35, 40, 50, 70,
                        45, 25, 30, 85, 150,
                        15, 20, 10, 18, 22]  # in billions USD
rnd_spending = [30, 18, 35, 500, 45,
                60, 60, 20, 40, 80,
                15, 25, 30, 10, 70,
                30, 20, 25, 70, 450,
                5, 10, 8, 12, 15]  # in billions USD
sustainability_index = [0.85, 0.70, 0.90, 0.75, 0.92,
                        0.94, 0.65, 0.68, 0.88, 0.91,
                        0.72, 0.93, 0.77, 0.60, 0.89,
                        0.87, 0.95, 0.74, 0.90, 0.85,
                        0.55, 0.66, 0.60, 0.58, 0.67]

# Convert Sustainability Index to a size for the plot, with an arbitrary scale factor
sizes = [s * 1000 for s in sustainability_index]

# Create the Bubble Chart
plt.figure(figsize=(18, 14))
for i in range(len(countries)):
    plt.scatter(rnd_spending[i], investment_renewable[i], s=sizes[i], alpha=0.6,
                c=[f'#{int((1-sustainability_index[i])*255):02x}{int(sustainability_index[i]*255):02x}33'],
                edgecolors='w', linewidth=0.5)

plt.title('Investment in Renewable Energy vs R&D Spending with Sustainability Index as Bubble Size', pad=20)
plt.xlabel('R&D Spending in Billions USD')
plt.ylabel('Investment in Renewable Energy in Billions USD')
plt.grid(True)

# Add country labels to bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (rnd_spending[i], investment_renewable[i]), textcoords="offset points", 
                 xytext=(0, 10), ha='center', fontsize=8, color='#444444')

plt.show()