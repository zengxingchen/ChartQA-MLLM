
import matplotlib.pyplot as plt

# Data
age_group = ['0-2 years', '3-5 years', '6-12 years', '13-18 years', '19-25 years',
             '26-40 years', '41-60 years', '61-75 years', '76+ years']
average_sleep_duration = [14, 12, 10, 9, 8, 7.5, 7, 7, 6.5]
population_percentage = [5.0, 4.5, 10.0, 8.0, 12.0, 25.0, 20.0, 10.0, 5.0]
surveyed_people = [300, 250, 500, 450, 600, 800, 700, 500, 300]

# Bubble sizes, normalizing surveyed_people to suitable sizes for bubbles
sizes = [people / 1.5 for people in surveyed_people]

# Color codes
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#40E0D0', '#1E90FF', '#BA55D3', '#FF69B4', '#8A2BE2', '#00FF7F']

# Create plot
plt.figure(figsize=(16, 9))  # Modify width and height
plt.scatter(average_sleep_duration, population_percentage, s=sizes, c=colors, alpha=0.6)
plt.title('Average Sleep Duration by Age Group (2023)')
plt.xlabel('Average Sleep Duration (hours)')
plt.ylabel('Population Percentage (%)')

# Annotate age groups
for i, txt in enumerate(age_group):
    plt.annotate(txt, (average_sleep_duration[i], population_percentage[i]), ha='center')

plt.grid(True)
plt.tight_layout()
plt.show()