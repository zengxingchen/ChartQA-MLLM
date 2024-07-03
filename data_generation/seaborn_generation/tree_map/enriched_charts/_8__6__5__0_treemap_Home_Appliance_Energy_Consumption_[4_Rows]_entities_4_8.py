
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Event': ['Mental Health Workshop', 'Nutrition Seminar', 'Fitness Bootcamp', 'Yoga Session', 'Mindfulness Retreat',
              'Health Screening', 'Stress Management Lecture', 'Wellness Fair', 'Psychology Conference', 'Diet & Exercise Workshop',
              'Therapy Session', 'Meditation Class', 'Sleep Health Seminar', 'Healthy Cooking Demo', 'Self-Care Day',
              'Holistic Health Expo', 'Physical Therapy Session', 'Mental Wellness Symposium', 'Alternative Medicine Fair', 'Life Coaching Seminar'],
    'Attendance': [2500, 4000, 6000, 7000, 8000,
                   9000, 10000, 11000, 12000, 13000,
                   14000, 15000, 16000, 17000, 18000,
                   19000, 20000, 21000, 22000, 23000]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18,14))

colors = ['#4A90E2', '#50E3C2', '#B8E986', '#F5A623', '#D0021B',
          '#8B572A', '#7ED321', '#417505', '#BD10E0', '#9013FE',
          '#F8E71C', '#D0011B', '#FF4A4A', '#8A9B0F', '#B78C2B',
          '#1A4876', '#0C0C0C', '#F0A4A3', '#C45153', '#7C9B64']

squarify.plot(sizes=df['Attendance'], label=df['Event'], color=colors, alpha=0.8)

plt.title('Event Attendance in Health & Psychology', fontsize=20, pad=30)
plt.axis('off')

plt.show()