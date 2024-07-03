
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
breakfast = [300, 350, 320, 330, 310, 400, 370]
lunch = [700, 650, 680, 690, 720, 750, 730]
dinner = [600, 650, 630, 610, 620, 650, 640]
snacks = [200, 150, 180, 190, 170, 250, 220]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(10, 14))

# Plotting the bar chart
bar_width = 0.2
ax.bar(days, breakfast, color='#FF5733', width=bar_width, label='Breakfast')
ax.bar([d + bar_width for d in range(len(days))], lunch, color='#33FF57', width=bar_width, label='Lunch')
ax.bar([d + 2 * bar_width for d in range(len(days))], dinner, color='#3357FF', width=bar_width, label='Dinner')
ax.bar([d + 3 * bar_width for d in range(len(days))], snacks, color='#F1C40F', width=bar_width, label='Snacks')

# Customizing the plot (labels, title, etc.)
ax.set_xlabel('Days')
ax.set_ylabel('Calories')
ax.set_title('Average Daily Calorie Intake for Different Meals', pad=20)
ax.set_ylim([0, 1000])
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout
plt.tight_layout()
plt.show()