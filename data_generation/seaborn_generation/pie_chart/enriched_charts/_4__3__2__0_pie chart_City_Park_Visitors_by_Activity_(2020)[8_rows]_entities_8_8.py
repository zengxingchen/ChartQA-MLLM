
import matplotlib.pyplot as plt

# Data to plot
categories = ['Instrumental', 'Vocals', 'Sound Engineering', 'Production', 'Marketing', 'Album Artwork', 'Promotion', 'Merchandising']
values = [220, 180, 140, 160, 130, 100, 150, 120]
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', '#FF9133', '#9133FF', '#33FF91']

# Create pie chart
plt.figure(figsize=(12, 9))
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Music & Performing Arts Budget Allocation for 2023', pad=30)
plt.show()