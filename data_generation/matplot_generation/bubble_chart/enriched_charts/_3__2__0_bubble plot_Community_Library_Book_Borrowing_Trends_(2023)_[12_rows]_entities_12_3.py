
import matplotlib.pyplot as plt

# Data
diet = ['Vegan', 'Vegetarian', 'Keto', 'Paleo', 'Mediterranean', 'Low-Carb', 'High-Protein', 'DASH', 'Flexitarian', 'Gluten-Free', 'Organic', 'Pescatarian', 'Whole30', 'Carnivore', 'Fruitarian']
nutrient_intake = [70, 65, 80, 75, 85, 60, 82, 72, 68, 62, 78, 73, 77, 55, 50]
monthly_cost = [150, 130, 180, 170, 160, 140, 175, 155, 145, 165, 200, 190, 185, 120, 100]
popularity_index = [320, 280, 350, 290, 330, 270, 310, 300, 295, 250, 240, 260, 270, 220, 210]

# Bubble sizes, normalizing popularity_index to suitable sizes for bubbles
sizes = [index / 1.5 for index in popularity_index]

# Color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FF8C33', '#33FFF3', '#A633FF', '#FF3364', '#33FFBD', '#C7FF33', '#5733FF', '#FF9E33', '#33FFF5', '#C733FF', '#FF3370']

# Create plot
plt.figure(figsize=(18, 10))
plt.scatter(monthly_cost, nutrient_intake, s=sizes, c=colors, alpha=0.6)
plt.title('Impact of Various Diets on Nutrient Intake and Cost', pad=20)
plt.xlabel('Monthly Cost (USD)')
plt.ylabel('Nutrient Intake (Index)')

# Annotate diet names
for i, txt in enumerate(diet):
    plt.annotate(txt, (monthly_cost[i], nutrient_intake[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()