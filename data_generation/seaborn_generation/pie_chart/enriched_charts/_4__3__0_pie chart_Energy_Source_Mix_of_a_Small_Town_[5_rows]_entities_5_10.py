
import matplotlib.pyplot as plt

# Data to plot
labels = 'Education', 'Healthcare', 'Defense', 'Social Security', 'Transportation', 'Other'
sizes = [22, 17, 15, 18, 10, 18]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Plot
plt.figure(figsize=(12,8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Government Budget Allocation', pad=20)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()