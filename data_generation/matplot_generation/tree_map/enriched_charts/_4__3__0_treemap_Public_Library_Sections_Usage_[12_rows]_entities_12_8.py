
import matplotlib.pyplot as plt
import squarify

# Data for scientific fields' research funding
fields = ['Physics', 'Biology', 'Chemistry', 'Mathematics', 'Earth Sciences', 'Astronomy', 'Materials Science', 'Environmental Science', 'Computer Science', 'Engineering', 'Medicine', 'Psychology', 'Agricultural Science', 'Social Sciences', 'Economics', 'Geography', 'Other']
funding_percentage = [18.5, 16.3, 14.1, 9.8, 8.4, 7.9, 7.1, 6.2, 5.8, 4.7, 3.9, 2.7, 2.4, 2.1, 1.8, 1.5, 6.8]

# Custom color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF5', '#FF8333', '#F533FF', '#33FF95', '#33D1FF', '#FF5733', '#5733FF', '#FF3377', '#33FFBB', '#D1FF33', '#FF5733', '#FF3333', '#339FFF']

# Treemap
plt.figure(figsize=(16, 12))  # Adjusting the size of the treemap
squarify.plot(sizes=funding_percentage, label=fields, color=colors, alpha=0.8)
plt.title('Scientific Fields Research Funding 2021', fontsize=20, pad=20)
plt.axis('off')  # No axes for a cleaner look

plt.show()