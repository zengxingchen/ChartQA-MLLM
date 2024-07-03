
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sketching = [2, 3, 2.5, 3.5, 4, 5, 4.5]  # Average hours spent on sketching
painting = [1, 1.5, 2, 2.5, 3, 3.5, 4]   # Average hours spent on painting
digital_art = [2, 2.5, 3, 3.5, 4, 4.5, 5]  # Average hours spent on digital art
photography = [1, 1.5, 2, 2.5, 3, 3.5, 4]  # Average hours spent on photography

# Plot setting (adjusting width and height)
plt.figure(figsize=(18, 10))

# Bubble chart
for i in range(len(days)):
    plt.scatter(days[i], sketching[i], s=sketching[i]*40, alpha=0.6, color='#003f5c', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], painting[i], s=painting[i]*40, alpha=0.6, color='#bc5090', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], digital_art[i], s=digital_art[i]*40, alpha=0.6, color='#ffa600', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], photography[i], s=photography[i]*40, alpha=0.6, color='#58508d', edgecolors='w', linewidth=0.5)

# Customizing the plot
plt.title('Average Time Spent on Art Activities (Hours) - Weekly Overview', pad=30)
plt.xlabel('Day of the Week')
plt.ylabel('Average Hours')
plt.xticks(rotation=45)

# Custom legend
for activity, color in zip(["Sketching", "Painting", "Digital Art", "Photography"], ['#003f5c', '#bc5090', '#ffa600', '#58508d']):
    plt.scatter([], [], alpha=0.6, s=160, label=activity, color=color, edgecolors='w', linewidth=0.5)
plt.legend(scatterpoints=1, frameon=False, labelspacing=1.2, loc='upper left', title="Art Activities")

plt.tight_layout()
plt.show()