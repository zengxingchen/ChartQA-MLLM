
import matplotlib.pyplot as plt

# Table data
activity = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Others']
market_share = [25.0, 20.0, 15.0, 10.0, 18.0, 12.0]
colors = ['#FF6347', '#4682B4', '#32CD32', '#8A2BE2', '#FF4500', '#DAA520']

# Plot
fig, ax = plt.subplots(figsize=(10, 6))  # Change width and height of the chart
ax.pie(market_share, labels=activity, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Market Share of Different Fitness Activities in 2023', pad=20)
plt.show()