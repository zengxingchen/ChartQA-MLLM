
import matplotlib.pyplot as plt

labels = ['Books', 'Courses', 'Workshops', 'Online Resources', 'Community Events']
sizes = [180, 240, 160, 100, 70]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10,8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Education & Learning Resource Distribution', pad=40)
plt.axis('equal')
plt.show()