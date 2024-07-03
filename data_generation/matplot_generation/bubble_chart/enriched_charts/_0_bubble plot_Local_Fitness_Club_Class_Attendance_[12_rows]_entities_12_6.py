
import matplotlib.pyplot as plt

# Data
age_groups = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80']
average_hours = [2.5, 3.0, 2.0, 1.5, 1.0, 0.5, 0.3]
population = [1500, 2000, 1800, 1600, 1400, 1200, 800]
colors = ['#FF5733', '#FFC300', '#7ED957', '#5797ED', '#B457ED', '#ED579E', '#57EDE3']
sizes = [i / 10 for i in population]  # Making the population numbers work for bubble sizes

fig, ax = plt.subplots(figsize=(10, 6))  # Modify width and height of the chart

# Bubble chart
for i in range(len(age_groups)):
    ax.scatter(age_groups[i], average_hours[i], s=sizes[i], alpha=0.5, color=colors[i])

# Title and labels
ax.set_title('Average Hours of Social Media Usage Per Age Group', pad=20)
ax.set_xlabel('Age Group')
ax.set_ylabel('Average Hours')

plt.show()