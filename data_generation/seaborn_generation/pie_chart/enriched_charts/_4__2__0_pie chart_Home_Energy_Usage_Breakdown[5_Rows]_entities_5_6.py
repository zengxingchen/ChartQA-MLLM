
import matplotlib.pyplot as plt

# Data
fields = ['Depression', 'Anxiety', 'Bipolar Disorder', 'Schizophrenia', 'PTSD',
          'OCD', 'ADHD', 'Eating Disorders', 'Autism Spectrum', 'Dementia',
          'Substance Abuse', 'Sleep Disorders', 'Stress', 'Suicide Prevention', 'Phobias']
values = [400, 350, 300, 250, 200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 20]

# Colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8F33',
          '#33FFF4', '#FF3333', '#A133FF', '#33FF99', '#FFD333',
          '#33FF77', '#FF5733', '#33D4FF', '#FF33D4', '#33FF57']

# Pie chart
fig, ax = plt.subplots(figsize=(12, 8))  # Width, Height of the chart
ax.pie(values, labels=fields, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Mental Health Research Funding (Millions USD)', pad=20)
plt.show()