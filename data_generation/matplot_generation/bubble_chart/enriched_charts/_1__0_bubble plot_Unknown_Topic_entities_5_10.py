
import matplotlib.pyplot as plt

# Data points - Country research papers, funding, impact factor
countries = ["China", "United States", "India", "Russia", "Japan", "Germany", "Iran",
             "Saudi Arabia", "South Korea", "Canada", "Brazil", "Australia", "United Kingdom",
             "France", "Italy", "South Africa", "Mexico", "Indonesia", "Turkey", "Ukraine"]
research_papers = [15000, 18000, 12000, 8000, 11000, 9500, 6000, 4000, 8500, 7000, 9000, 5000, 10000, 9500, 7500, 3000, 4000, 2000, 5000, 2500]  # in thousands
funding = [2000000, 2500000, 500000, 400000, 1500000, 1300000, 300000, 600000, 800000, 1100000, 700000, 900000, 1400000, 1200000, 1000000, 200000, 300000, 100000, 400000, 150000]  # in USD
impact_factor = [50, 60, 45, 35, 55, 52, 28, 30, 40, 48, 38, 43, 53, 49, 42, 25, 33, 20, 34, 22]  # in impact factor units

# Create the bubble chart with a custom size
fig, ax = plt.subplots(figsize=(16, 9))

# Assign a color to each country
colors = {
    "China": "#FF5733",
    "United States": "#33FF57",
    "India": "#3357FF",
    "Russia": "#FFFF33",
    "Japan": "#FF33FF",
    "Germany": "#57FFF3",
    "Iran": "#F357FF",
    "Saudi Arabia": "#F3573C",
    "South Korea": "#3CF357",
    "Canada": "#5733FF",
    "Brazil": "#33FF95",
    "Australia": "#FF3357",
    "United Kingdom": "#33F3FF",
    "France": "#FF9533",
    "Italy": "#3C57F3",
    "South Africa": "#95FF33",
    "Mexico": "#33F3F3",
    "Indonesia": "#F333FF",
    "Turkey": "#FF3C57",
    "Ukraine": "#F39533"
}

# Plot each data point and assign it a label, size, and color
for i, country in enumerate(countries):
    ax.scatter(research_papers[i], funding[i], s=impact_factor[i]*10,  # Adjust size scaling factor as desired
               c=colors[country], alpha=0.6, edgecolors="w", label=country)

# Customize the chart
ax.set_title('Research Funding, Papers Published, and Impact Factor by Country', fontsize=18, pad=20)
ax.set_xlabel('Research Papers Published (in thousands)', fontsize=14)
ax.set_ylabel('Research Funding (in USD)', fontsize=14)

# Customize the grid
ax.grid(True)

# Add legend
ax.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Show plot with a tight layout
plt.tight_layout()
plt.show()