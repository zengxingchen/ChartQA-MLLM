
import matplotlib.pyplot as plt

# Data setup
activities = ['Reading', 'Exercising', 'Social Media', 'Working', 'Sleeping', 'Other']
percentages = [25, 20, 15, 30, 5, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Plotting
fig, ax = plt.subplots(figsize=(8, 8))  # width and height of the chart
ax.pie(percentages, labels=activities, autopct='%1.1f%%', colors=colors, startangle=140)
ax.set_title('Daily Activity Distribution', pad=20)

# Show plot
plt.show()