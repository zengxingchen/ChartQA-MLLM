
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
math_scores = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
science_scores = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
art_scores = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(14, 10))
ax.stackplot(months, math_scores, science_scores, art_scores, colors=['#4682B4', '#32CD32', '#FF69B4'], labels=['Math', 'Science', 'Art'])

# Customizing the plot
ax.set_title('Monthly Student Performance in 2023', fontsize=16, pad=20)
ax.set_ylabel('Scores', fontsize=14)
ax.set_xlabel('Month', fontsize=14)
ax.margins(0, 0)  # Removes the default margins to use the entire space for plotting

# Adding annotation
ax.annotate('Math scores peak', xy=('December', 105), xytext=('October', 115),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Adding legend
ax.legend(loc='upper left', fontsize=12)

# Displaying the plot
plt.show()