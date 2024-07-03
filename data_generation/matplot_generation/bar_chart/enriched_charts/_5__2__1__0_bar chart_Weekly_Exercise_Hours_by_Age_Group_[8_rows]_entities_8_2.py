
import matplotlib.pyplot as plt

categories = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
technology_spending = [180, 175, 190, 185, 200, 195, 210, 205, 220, 215, 230, 225]
education_spending = [210, 205, 220, 215, 230, 225, 240, 235, 250, 245, 260, 255]
healthcare_spending = [230, 225, 240, 235, 250, 245, 260, 255, 270, 265, 280, 275]

fig, ax = plt.subplots(figsize=(10, 12))

bar_width = 0.3
bar_locations_tech = range(len(technology_spending))
bar_locations_edu = [x + bar_width for x in bar_locations_tech]
bar_locations_health = [x + bar_width for x in bar_locations_edu]

bars1 = ax.bar(bar_locations_tech, technology_spending, bar_width, label="Technology Spending", color='#FF5733')
bars2 = ax.bar(bar_locations_edu, education_spending, bar_width, label="Education Spending", color='#33FF57')
bars3 = ax.bar(bar_locations_health, healthcare_spending, bar_width, label="Healthcare Spending", color='#3357FF')

ax.set_xticks([r + bar_width for r in range(len(technology_spending))])
ax.set_xticklabels(categories)

plt.ylabel('Spending ($)')
plt.title("Monthly Spending on Technology, Education, and Healthcare")
ax.legend(loc='upper right')

ax.set_ylim(150, 300)

plt.tight_layout()
plt.show()