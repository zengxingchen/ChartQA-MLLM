
import matplotlib.pyplot as plt

# Data to plot
labels = ['Keto Diet', 'Vegan Diet', 'Paleo Diet', 'Mediterranean Diet', 'Low-Carb Diet', 'Intermittent Fasting', 'Other']
sizes = [30.1, 20.4, 18.7, 15.2, 10.6, 4.5, 0.5]
colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a8', '#33a8ff', '#a8ff33', '#a833ff']

# Plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Distribution of Popular Diet Types in 2023', pad=20)
plt.show()