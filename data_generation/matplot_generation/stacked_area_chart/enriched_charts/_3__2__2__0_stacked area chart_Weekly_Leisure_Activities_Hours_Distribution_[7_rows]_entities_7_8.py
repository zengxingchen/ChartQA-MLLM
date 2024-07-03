
import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
introduction = [500, 550, 620, 700, 780, 820, 850, 870, 900, 950, 1000, 1050]
ethics = [200, 210, 250, 300, 350, 380, 400, 420, 450, 470, 500, 550]
machine_learning = [800, 850, 870, 900, 950, 970, 990, 1000, 1010, 1030, 1040, 1060]
research = [300, 330, 350, 370, 400, 420, 430, 450, 470, 490, 510, 530]

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(months, introduction, ethics, machine_learning, research, 
             labels=['Introduction to AI', 'AI Ethics', 'Machine Learning', 'AI Research'], 
             colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

ax.legend(loc='upper left')
ax.set_title('Monthly Attendance in AI Courses', pad=20)
ax.annotate('Highest in Dec', xy=('Dec', 1050), xytext=('Oct', 1200),
             arrowprops=dict(facecolor='black', shrink=0.05))

ax.set_xlabel('Month')
ax.set_ylabel('Number of Students')

plt.show()