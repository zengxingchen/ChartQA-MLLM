
import matplotlib.pyplot as plt

# Data to plot
labels = ['Innovation', 'Startups', 'Funding', 'Marketing', 'Management', 'Networking', 'Other']
sizes = [30.0, 25.0, 10.0, 12.0, 8.0, 10.0, 5.0]
colors = ['#FF5733', '#33FF57', '#3357FF', '#F39C12', '#8E44AD', '#2ECC71', '#E74C3C']

# Plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Business & Entrepreneurship Topics in 2023', pad=20)
plt.show()