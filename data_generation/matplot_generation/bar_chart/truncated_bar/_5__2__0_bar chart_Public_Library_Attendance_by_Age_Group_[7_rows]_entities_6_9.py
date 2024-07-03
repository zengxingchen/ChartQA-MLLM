
import matplotlib.pyplot as plt

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
students = [50, 60, 80, 90, 120, 150, 140, 130, 110, 100, 70, 55]

colors = ['#4B0082', '#8A2BE2', '#7B68EE', '#6A5ACD', '#483D8B', '#00CED1', '#48D1CC', '#20B2AA', '#5F9EA0', '#008080', '#2F4F4F', '#00FFFF']

plt.figure(figsize=(10, 8))
bar_height = 0.5
plt.barh(months, students, color=colors, height=bar_height)

plt.title('Average Number of Students per Class in a Year', pad=20)
plt.xlabel('Number of Students')
plt.ylabel('Month')

plt.xlim([40, max(students) + 20])

plt.tight_layout()
plt.show()