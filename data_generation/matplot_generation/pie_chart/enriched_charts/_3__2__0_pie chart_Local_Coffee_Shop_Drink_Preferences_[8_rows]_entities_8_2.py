
import matplotlib.pyplot as plt

labels = 'Mathematics', 'Science', 'English', 'History', 'Geography', 'Physical Education', 'Art', 'Music'
sizes = [130, 95, 85, 75, 65, 55, 45, 35]
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FF6666', '#66FFB2', '#B266FF', '#FF66CC']

plt.figure(figsize=(10, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

plt.title('Distribution of Study Subjects in a High School', pad=20)
plt.axis('equal')
plt.show()