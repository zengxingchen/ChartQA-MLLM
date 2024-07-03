
import matplotlib.pyplot as plt

# Data to plot
labels = ['Classical', 'Rock', 'Jazz', 'Hip-Hop', 'Pop', 'Country', 'Electronic']
sizes = [20, 25, 15, 18, 12, 7, 3]
colors = ['#f94144', '#f3722c', '#f8961e', '#f9844a', '#f9c74f', '#90be6d', '#43aa8b']

# Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Music Genres in 2023', pad=20)
plt.show()