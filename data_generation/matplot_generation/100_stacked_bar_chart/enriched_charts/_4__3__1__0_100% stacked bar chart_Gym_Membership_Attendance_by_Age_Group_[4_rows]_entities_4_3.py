
import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Science', 'Mathematics', 'Engineering', 'Medicine', 'Social Sciences', 'Humanities', 'Law', 'Arts', 'Education', 'Business', 'Economics', 'Physics', 'Chemistry', 'Biology', 'Geology', 'Environmental Science', 'Computer Science', 'Statistics', 'Philosophy', 'Psychology']
undergraduate = [30, 35, 20, 15, 25, 20, 15, 20, 25, 30, 25, 30, 20, 35, 25, 30, 40, 20, 15, 30]
masters = [25, 20, 30, 25, 20, 25, 30, 25, 20, 20, 30, 25, 35, 25, 20, 25, 20, 25, 30, 25]
phd = [20, 25, 25, 35, 30, 30, 25, 35, 30, 25, 20, 25, 25, 30, 20, 25, 20, 35, 25, 30]
professional = [25, 20, 25, 25, 25, 25, 30, 20, 25, 25, 25, 20, 20, 20, 35, 20, 20, 20, 30, 15]

# Normalize data to percentages
total = np.array(undergraduate) + np.array(masters) + np.array(phd) + np.array(professional)
undergraduate = np.array(undergraduate) / total * 100
masters = np.array(masters) / total * 100
phd = np.array(phd) / total * 100
professional = np.array(professional) / total * 100

# Plot
fig, ax = plt.subplots(figsize=(12, 10))
width = 0.8

ax.bar(categories, undergraduate, color='#8B0000', edgecolor='white', width=width, label='Undergraduate')
ax.bar(categories, masters, bottom=undergraduate, color='#FF4500', edgecolor='white', width=width, label='Masters')
ax.bar(categories, phd, bottom=undergraduate + masters, color='#FFD700', edgecolor='white', width=width, label='PhD')
ax.bar(categories, professional, bottom=undergraduate + masters + phd, color='#32CD32', edgecolor='white', width=width, label='Professional')

# Add title and labels
ax.set_title('Distribution of Degrees Across Academic Fields', fontsize=20, pad=20)
ax.set_ylabel('Percentage', fontsize=14)
ax.set_xlabel('Field of Study', fontsize=14)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()