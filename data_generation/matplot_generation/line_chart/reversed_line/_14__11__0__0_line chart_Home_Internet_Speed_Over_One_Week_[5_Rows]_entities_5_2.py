
import matplotlib.pyplot as plt

# Data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
happiness_score = [6.5, 6.8, 7.1, 7.5, 7.9, 8.3, 8.7, 8.9, 8.5, 8.0, 7.4, 6.9]
stress_score = [7.2, 6.8, 6.3, 6.0, 5.8, 5.6, 5.7, 5.8, 5.9, 6.2, 6.6, 7.1]

# Create the plot
plt.figure(figsize=(14, 8))
plt.plot(months, happiness_score, color='#1f77b4', marker='o', label="Happiness Score")
plt.plot(months, stress_score, color='#ff7f0e', marker='o', label="Stress Score")

# Highlight Highest and Lowest Scores
highest_happiness = max(happiness_score)
lowest_stress = min(stress_score)
highest_month_happiness = months[happiness_score.index(highest_happiness)]
lowest_month_stress = months[stress_score.index(lowest_stress)]

plt.annotate(f'Highest Happiness\n{highest_happiness}', xy=(highest_month_happiness, highest_happiness), xytext=(highest_month_happiness, highest_happiness+0.5),
             arrowprops=dict(facecolor='green', shrink=0.05), ha='center')
plt.annotate(f'Lowest Stress\n{lowest_stress}', xy=(lowest_month_stress, lowest_stress), xytext=(lowest_month_stress, lowest_stress-0.5),
             arrowprops=dict(facecolor='red', shrink=0.05), ha='center')

# Customize rest of the chart
plt.title("Monthly Happiness and Stress Scores", y=1.03)
plt.xlabel("Month")
plt.ylabel("Score")
plt.legend(loc='upper left')
plt.grid(True)
plt.gca().invert_yaxis()
plt.tight_layout()

# Show the plot
plt.show()