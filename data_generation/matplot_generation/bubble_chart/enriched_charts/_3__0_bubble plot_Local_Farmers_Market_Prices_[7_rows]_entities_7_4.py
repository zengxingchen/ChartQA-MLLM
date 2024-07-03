
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
math = [2, 3, 2.5, 3.5, 4, 1, 1.5]        # Average hours spent on Math
science = [3, 3.5, 4, 4.5, 3, 2, 1.5]     # Average hours spent on Science
history = [2.5, 2, 3, 3.5, 2.5, 2, 2.5]   # Average hours spent on History
art = [1.5, 2, 2.5, 2.5, 3, 3, 4]         # Average hours spent on Art

# Plot setting (adjusting width and height)
plt.figure(figsize=(16, 10))

# Bubble chart
for i in range(len(days)):
    plt.scatter(days[i], math[i], s=math[i]*30, alpha=0.5, color='#FF5733', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], science[i], s=science[i]*30, alpha=0.5, color='#33FF57', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], history[i], s=history[i]*30, alpha=0.5, color='#3357FF', edgecolors='w', linewidth=0.5)
    plt.scatter(days[i], art[i], s=art[i]*30, alpha=0.5, color='#FF33A1', edgecolors='w', linewidth=0.5)

# Customizing the plot
plt.title('Average Study Time in Different Subjects (Hours) - Weekly Overview', pad=20)
plt.xlabel('Day of the Week')
plt.ylabel('Average Hours')
plt.xticks(rotation=45)

# Custom legend
for subject, color in zip(["Math", "Science", "History", "Art"], ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']):
    plt.scatter([], [], alpha=0.5, s=100, label=subject, color=color, edgecolors='w', linewidth=0.5)
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper right', title="Subjects")

plt.tight_layout()
plt.show()