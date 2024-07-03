
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['USA', 'UK', 'Germany', 'Canada', 'Australia', 'India', 'China', 'Brazil']
education = [35, 30, 25, 40, 45, 20, 15, 10]
health = [45, 40, 35, 50, 55, 30, 25, 20]
technology = [55, 50, 45, 60, 65, 40, 35, 30]
arts = [25, 30, 35, 20, 15, 40, 45, 50]
travel = [15, 20, 25, 10, 5, 30, 35, 40]
finance = [60, 55, 50, 65, 70, 45, 40, 35]
entertainment = [50, 45, 40, 55, 60, 35, 30, 25]
science = [40, 35, 30, 45, 50, 25, 20, 15]

# Plotting
bar_width = 0.75
index = np.arange(len(categories))

fig, ax = plt.subplots(figsize=(12, 9))
ax.bar(index, education, bar_width, label='Education', color='#3498db')
ax.bar(index, health, bar_width, bottom=education, label='Health', color='#2ecc71')
ax.bar(index, technology, bar_width, bottom=np.array(education) + np.array(health), label='Technology', color='#e74c3c')
ax.bar(index, arts, bar_width, bottom=np.array(education) + np.array(health) + np.array(technology), label='Arts', color='#9b59b6')
ax.bar(index, travel, bar_width, bottom=np.array(education) + np.array(health) + np.array(technology) + np.array(arts), label='Travel', color='#f1c40f')
ax.bar(index, finance, bar_width, bottom=np.array(education) + np.array(health) + np.array(technology) + np.array(arts) + np.array(travel), label='Finance', color='#34495e')
ax.bar(index, entertainment, bar_width, bottom=np.array(education) + np.array(health) + np.array(technology) + np.array(arts) + np.array(travel) + np.array(finance), label='Entertainment', color='#1abc9c')
ax.bar(index, science, bar_width, bottom=np.array(education) + np.array(health) + np.array(technology) + np.array(arts) + np.array(travel) + np.array(finance) + np.array(entertainment), label='Science', color='#e67e22')

# Labels and Titles
ax.set_ylabel('Percentage')
ax.set_title('Percentage Allocation in Different Sectors Across Countries', pad=20)
ax.set_xticks(index)
ax.set_xticklabels(categories)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Display the plot
plt.tight_layout()
plt.show()