
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
average_protein_intake = [65, 70, 75, 80, 85, 90, 100, 95, 85, 75, 70, 65]
average_fat_intake = [75, 80, 85, 90, 95, 100, 110, 105, 95, 85, 80, 75]

# Create the plot
plt.figure(figsize=(16, 10))
plt.plot(months, average_protein_intake, color='#2ca02c', marker='o', label="Average Protein Intake")
plt.plot(months, average_fat_intake, color='#d62728', marker='o', label="Average Fat Intake")

# Highlight Highest and Lowest Intakes
highest_protein = max(average_protein_intake)
lowest_fat = min(average_fat_intake)
highest_protein_month = months[average_protein_intake.index(highest_protein)]
lowest_fat_month = months[average_fat_intake.index(lowest_fat)]

plt.annotate(f'Highest Protein\n{highest_protein}g', xy=(highest_protein_month, highest_protein), xytext=(highest_protein_month, highest_protein + 5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')
plt.annotate(f'Lowest Fat\n{lowest_fat}g', xy=(lowest_fat_month, lowest_fat), xytext=(lowest_fat_month, lowest_fat - 5),
             arrowprops=dict(facecolor='black', shrink=0.05), ha='center')

# Customize the rest of the chart
plt.title("Monthly Average Nutrient Intake in City Y", y=1.05)
plt.xlabel("Month")
plt.ylabel("Intake (g)")
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()