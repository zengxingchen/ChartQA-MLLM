
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
cardio = [12000, 15000, 17000, 16000, 18000, 20000, 22000, 23000, 24000, 25000, 26000, 27000]
strength = [9000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000]
yoga = [7000, 8000, 9000, 9500, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000]
swimming = [5000, 4000, 6000, 7000, 8000, 9000, 10000, 9500, 11000, 12000, 13000, 14000]

fig, ax = plt.subplots(figsize=(12, 8)) # change width and height of the chart

bar_width = 0.5 # change width of bars

# Plotting data
p1 = ax.bar(months, cardio, bar_width, color='#1f77b4', label='Cardio')
p2 = ax.bar(months, strength, bar_width, bottom=cardio, color='#ff7f0e', label='Strength')
p3 = ax.bar(months, yoga, bar_width, bottom=[i+j for i,j in zip(cardio, strength)], color='#2ca02c', label='Yoga')
p4 = ax.bar(months, swimming, bar_width, bottom=[i+j+k for i,j,k in zip(cardio, strength, yoga)], color='#d62728', label='Swimming')

ax.set_ylabel('Number of Workouts')
ax.set_title('Monthly Distribution of Workout Types')
ax.set_xticks([i for i in range(len(months))])  # Modify tick position
ax.set_xticklabels(months, rotation=45)
ax.legend()

# Adding numerical labels
for rect in p1 + p2 + p3 + p4:
    height = rect.get_height() + (rect.get_y() if rect.get_y() else 0)
    ax.text(rect.get_x() + rect.get_width() / 2., height,
            '%d' % int(height),
            ha='center', va='bottom')

# Customize the grid
plt.grid(which='major', linestyle='--', linewidth='0.5', color='black')
plt.tight_layout()  # Adjust layout to make room for labels
plt.show()