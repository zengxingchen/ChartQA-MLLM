
import matplotlib.pyplot as plt

# Data
countries = [
    "Finland", "Denmark", "Switzerland", "Iceland", "Netherlands",
    "Norway", "Sweden", "New Zealand", "Austria", "Luxembourg",
    "Canada", "Australia", "United Kingdom", "Israel", "Costa Rica",
    "Ireland", "Germany", "United States", "Czech Republic", "Belgium",
    "France", "Bahrain", "Slovenia", "Trinidad and Tobago", "Spain"
]
happiness_scores = [
    7.8, 7.6, 7.5, 7.5, 7.4,
    7.3, 7.2, 7.1, 7.0, 7.0,
    6.9, 6.9, 6.8, 6.8, 6.7,
    6.7, 6.6, 6.5, 6.5, 6.4,
    6.4, 6.3, 6.3, 6.2, 6.2
]

# Scatter plot
fig, ax = plt.subplots(figsize=(16, 10))
scatter = ax.scatter(
    range(len(happiness_scores)),
    happiness_scores,
    alpha=0.8,
    c=[
        '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1',
        '#A133FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A1',
        '#33FFA1', '#A133FF', '#FF5733', '#33FF57', '#3357FF',
        '#FF33A1', '#33FFA1', '#A133FF', '#FF5733', '#33FF57',
        '#3357FF', '#FF33A1', '#33FFA1', '#A133FF', '#FF5733'
    ],
    edgecolors='w'
)

# Customizing the looks of the plot
ax.set_title('Top 25 Happiest Countries by Happiness Score', pad=20)
ax.set_xlabel('Countries', labelpad=15)
ax.set_ylabel('Happiness Score', labelpad=15)

# Adding the country names as labels next to each point
for i, country in enumerate(countries):
    ax.annotate(country, (i, happiness_scores[i]), fontsize=8)

plt.xticks(range(len(happiness_scores)), countries, rotation=90)
plt.tight_layout()
plt.show()