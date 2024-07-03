
import matplotlib.pyplot as plt

# Table data
category = ['Mindfulness', 'Exercise', 'Nutrition', 'Sleep', 'Hydration', 'Social Connections', 'Hobbies', 'Education']
percentage = [22.0, 18.0, 16.0, 14.0, 12.0, 10.0, 8.0, 6.0]
colors = ['#FF4500', '#1E90FF', '#32CD32', '#FFD700', '#9400D3', '#FF69B4', '#8A2BE2', '#D2691E']

# Plot
fig, ax = plt.subplots(figsize=(10, 8))  # Change width and height of the chart
ax.pie(percentage, labels=category, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Health & Psychology: Key Areas of Focus in 2023', pad=20)
plt.show()