
import matplotlib.pyplot as plt

countries = ["United States", "China", "Germany", "United Kingdom", "Japan", "France", 
             "South Korea", "India", "Canada", "Australia", "Italy", "Spain", 
             "Netherlands", "Russia", "Brazil", "Sweden", "Switzerland", 
             "South Africa", "Mexico", "Argentina"]
institutions = [3500, 3000, 2500, 2200, 2100, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 
                1200, 1100, 1000, 900, 800, 700, 600, 500]
funding = [5000000, 4800000, 3500000, 3400000, 3200000, 3100000, 3000000, 2800000, 
           2700000, 2600000, 2500000, 2400000, 2300000, 2200000, 2100000, 2000000, 
           1900000, 1800000, 1700000, 1600000]
impact_factor = [85, 80, 78, 76, 74, 72, 71, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 
                 58, 57]

fig, ax = plt.subplots(figsize=(20, 12))

colors = {
    "United States": "#1f77b4",
    "China": "#ff7f0e",
    "Germany": "#2ca02c",
    "United Kingdom": "#d62728",
    "Japan": "#9467bd",
    "France": "#8c564b",
    "South Korea": "#e377c2",
    "India": "#7f7f7f",
    "Canada": "#bcbd22",
    "Australia": "#17becf",
    "Italy": "#9edae5",
    "Spain": "#c7c7c7",
    "Netherlands": "#ff9896",
    "Russia": "#dbdb8d",
    "Brazil": "#c49c94",
    "Sweden": "#f7b6d2",
    "Switzerland": "#c5b0d5",
    "South Africa": "#ffbb78",
    "Mexico": "#98df8a",
    "Argentina": "#ffbb78"
}

for i, country in enumerate(countries):
    ax.scatter(institutions[i], funding[i], s=impact_factor[i]*10, c=colors[country], 
               alpha=0.6, edgecolors="w", label=country)

ax.set_title('Research Institutions, Funding, and Impact Factor by Country', fontsize=20, pad=30)
ax.set_xlabel('Number of Research Institutions', fontsize=16)
ax.set_ylabel('Funding (in USD)', fontsize=16)

ax.grid(True)
ax.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

plt.tight_layout()
plt.show()