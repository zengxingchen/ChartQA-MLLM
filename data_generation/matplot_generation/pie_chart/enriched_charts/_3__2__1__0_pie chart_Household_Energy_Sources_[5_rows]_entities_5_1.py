
import matplotlib.pyplot as plt

# Table data
category = ['Mindfulness', 'Exercise', 'Nutrition', 'Sleep', 'Hydration', 'Social Connections', 'Hobbies']
percentage = [25.0, 20.0, 15.0, 15.0, 10.0, 10.0, 5.0]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#4B0082', '#FF69B4', '#8A2BE2']

# Plot
fig, ax = plt.subplots(figsize=(12, 7))  # Change width and height of the chart
ax.pie(percentage, labels=category, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Healthy Lifestyle Components in 2023', pad=20)
plt.show()