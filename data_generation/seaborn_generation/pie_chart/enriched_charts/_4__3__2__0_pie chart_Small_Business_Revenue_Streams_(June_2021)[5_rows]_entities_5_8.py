
import matplotlib.pyplot as plt

# Data to plot
labels = ['Hospitals & Clinics', 'Medical Equipment', 'Pharmaceuticals', 'Public Health Programs', 'Mental Health Services', 'Research & Development', 'Health Education', 'Preventive Care', 'Administration', 'Others']
sizes = [25, 15, 20, 10, 8, 12, 5, 3, 2, 1]
colors = ['#ff6347', '#4682b4', '#32cd32', '#ff7f50', '#6a5acd', '#40e0d0', '#ff69b4', '#ffa500', '#87ceeb', '#dda0dd']

# Plot
fig1, ax1 = plt.subplots(figsize=(12, 8))
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Draw circle for donut chart
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')

plt.title('Health Expenditure Allocation', pad=40)
plt.show()