
import matplotlib.pyplot as plt

# Data points - Country, Athletes, Funding, Success Rate
countries = ["China", "United States", "India", "Russia", "Japan", "Germany", "Brazil", 
             "Australia", "United Kingdom", "France", "Italy", "South Africa", 
             "Canada", "Mexico", "South Korea", "Saudi Arabia", "Turkey", 
             "Argentina", "Spain", "Netherlands"]
athletes = [3200, 4100, 2200, 2800, 2400, 2700, 2600, 3000, 2500, 2300, 2100, 
            1500, 2000, 1700, 1800, 1200, 1600, 1300, 2000, 1500]
funding = [1800000, 2500000, 900000, 1200000, 1500000, 1400000, 800000, 1300000, 
           1600000, 1100000, 1000000, 500000, 900000, 600000, 700000, 400000, 
           450000, 500000, 1000000, 800000]
success_rate = [70, 85, 60, 75, 68, 72, 65, 80, 77, 69, 66, 55, 73, 52, 63, 50, 
                58, 54, 64, 67]

# Create the bubble chart with a custom size
fig, ax = plt.subplots(figsize=(18, 10))

# Assign a color to each country
colors = {
    "China": "#FF5733",
    "United States": "#33FF57",
    "India": "#3357FF",
    "Russia": "#FFFF33",
    "Japan": "#FF33FF",
    "Germany": "#57FFF3",
    "Brazil": "#FF33A1",
    "Australia": "#33FFA1",
    "United Kingdom": "#FF3380",
    "France": "#3380FF",
    "Italy": "#80FF33",
    "South Africa": "#FF8033",
    "Canada": "#8033FF",
    "Mexico": "#33FF80",
    "South Korea": "#FF3380",
    "Saudi Arabia": "#33FFB2",
    "Turkey": "#FF33D1",
    "Argentina": "#33FFD1",
    "Spain": "#D133FF",
    "Netherlands": "#33D1FF"
}

# Plot each data point and assign it a label, size, and color
for i, country in enumerate(countries):
    ax.scatter(athletes[i], funding[i], s=success_rate[i]*10,  # Adjust size scaling factor as desired
               c=colors[country], alpha=0.6, edgecolors="w", label=country)

# Customize the chart
ax.set_title('Athlete Participation, Funding, and Success Rate by Country', fontsize=18, pad=20)
ax.set_xlabel('Number of Athletes', fontsize=14)
ax.set_ylabel('Funding (in USD)', fontsize=14)

# Customize the grid
ax.grid(True)

# Add legend
ax.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Show plot with a tight layout
plt.tight_layout()
plt.show()