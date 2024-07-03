
import matplotlib.pyplot as plt

# Data
languages = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby', 'Swift', 'Go', 'Kotlin', 'Rust', 'TypeScript']
year = [2021] * len(languages)
job_postings = [15000, 18000, 13500, 5000, 4000, 3000, 4500, 3500, 2500, 7000]
average_salary = [110000, 105000, 115000, 95000, 120000, 130000, 125000, 115000, 130000, 100000]

# Size is proportional to job postings, and color represents average salary
size = [x / 100 for x in job_postings]
colors = ['#FF5733', '#33FF57', '#3357FF', '#57FF33', '#FF3357', '#FF33A4', '#A433FF', '#33FFF4', '#F4FF33', '#33FF83']

# Create a figure with specific width and height
fig, ax = plt.subplots(figsize=(12, 6))

# Bubble chart
sc = ax.scatter(languages, year, s=size, c=colors, alpha=0.6, edgecolors='w')

# Customize chart
ax.set_title('Programming Language Popularity and Salaries - 2021')
ax.set_xlabel('Programming Languages')
ax.set_ylabel('Year')
ax.set_yticks([2021])  # Only one year on the y-axis
ax.grid(True)

# Adding a color bar to indicate average salary
salary_tick_vals = range(90000, 135000, 5000)
salary_tick_labels = ['$' + str(val // 1000) + 'k' for val in salary_tick_vals]
sm = plt.cm.ScalarMappable(cmap=plt.cm.jet, norm=plt.Normalize(vmin=min(average_salary), vmax=max(average_salary)))
sm._A = []  # ScalarMappable expects an array of data values for colormap scaling; we provide a dummy
cbar = plt.colorbar(sm, ticks=salary_tick_vals)
cbar.ax.set_yticklabels(salary_tick_labels)
cbar.set_label('Average Salary')

# Show plot
plt.show()