
import matplotlib.pyplot as plt

# Data to plot
labels = ['Nutrition', 'Mental Health', 'Physical Fitness', 'Sleep', 'Hydration', 'Social Interaction', 'Hobbies', 'Work-Life Balance', 'Stress Management', 'Recreation']
sizes = [20, 12, 15, 18, 10, 8, 5, 12, 10, 5]
colors = ['#FF5733', '#33FFBD', '#3385FF', '#FF33A8', '#8D33FF', '#33FF57', '#FF8D33', '#FFD433', '#A833FF', '#33FF99']

# Plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Health & Psychology Distribution by Category', pad=20)
plt.show()