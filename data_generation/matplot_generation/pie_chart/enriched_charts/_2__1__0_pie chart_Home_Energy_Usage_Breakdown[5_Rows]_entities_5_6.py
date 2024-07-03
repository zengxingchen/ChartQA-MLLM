
import matplotlib.pyplot as plt

# Data
conditions = ['Anxiety Disorders', 'Major Depressive Disorder', 'Bipolar Disorder', 'Eating Disorders', 
              'Obsessive-Compulsive Disorder', 'Post-Traumatic Stress Disorder', 'Schizophrenia', 
              'Attention Deficit Hyperactivity Disorder', 'Borderline Personality Disorder', 
              'Panic Disorder', 'Specific Phobias', 'Social Anxiety Disorder', 
              'Generalized Anxiety Disorder', 'Autism Spectrum Disorder', 'Dysthymia']
percentages = [18.1, 6.7, 2.8, 2.7, 1.0, 3.5, 1.1, 4.1, 1.6, 2.7, 8.7, 6.8, 3.1, 1.5, 1.5]

# Colors
colors = ['#FF6347', '#FFD700', '#8A2BE2', '#7FFF00', '#FF69B4', 
          '#1E90FF', '#D2691E', '#DC143C', '#00FA9A', '#FFDAB9', 
          '#FF4500', '#8B008B', '#FF00FF', '#3CB371', '#BA55D3']

# Pie chart
fig, ax = plt.subplots(figsize=(12, 8))  # Width, Height of the chart
ax.pie(percentages, labels=conditions, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Distribution of Mental Health Conditions', pad=20)
plt.show()