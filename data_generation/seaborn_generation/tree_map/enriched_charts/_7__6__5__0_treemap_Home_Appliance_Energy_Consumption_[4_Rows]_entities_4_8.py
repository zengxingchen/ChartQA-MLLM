
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Event': ['Mathematics Workshop', 'Physics Lecture', 'Chemistry Experiment Day', 'Biology Field Trip', 'History Seminar', 
              'Geography Fair', 'Computer Science Coding Bootcamp', 'Literature Reading Session', 'Art History Presentation', 'Philosophy Debate', 
              'Language Learning Meetup', 'Psychology Group Discussion', 'Music Theory Class', 'Economics Game', 'Business Plan Competition', 
              'Engineering Robotics Challenge', 'Environmental Science Workshop', 'Political Science Talk', 'Sociology Research Project', 'Creative Writing Contest'],
    'Attendance': [4500, 13000, 9500, 12500, 7800, 
                   11200, 17000, 15500, 9100, 5200,
                   10500, 8900, 9400, 14200, 16000,
                   20000, 13500, 7500, 11800, 16800]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18,14))

colors = ['#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#f1c40f', 
          '#e67e22', '#1abc9c', '#34495e', '#f39c12', '#c0392b',
          '#8e44ad', '#2980b9', '#27ae60', '#d35400', '#7f8c8d',
          '#2c3e50', '#16a085', '#bdc3c7', '#c7ecee', '#d1ccc0']

squarify.plot(sizes=df['Attendance'], label=df['Event'], color=colors, alpha=0.8)

plt.title('Event Attendance in Education & Learning', fontsize=20, pad=30)
plt.axis('off')

plt.show()