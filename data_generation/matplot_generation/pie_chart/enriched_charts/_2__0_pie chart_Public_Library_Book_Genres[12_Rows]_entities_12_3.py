
import matplotlib.pyplot as plt

learning_management_systems = ['Moodle', 'Blackboard', 'Canvas', 'Google Classroom', 'Schoology', 'Other']
market_shares = [40, 25, 20, 10, 3, 2]
colors = ['#3498DB', '#E74C3C', '#1ABC9C', '#9B59B6', '#F1C40F', '#95A5A6']

plt.figure(figsize=(10, 10))
plt.pie(market_shares, labels=learning_management_systems, autopct='%1.1f%%', colors=colors, startangle=90)

plt.title('Popular Learning Management Systems (LMS) Market Share in 2023', pad=20)
plt.axis('equal')

plt.show()