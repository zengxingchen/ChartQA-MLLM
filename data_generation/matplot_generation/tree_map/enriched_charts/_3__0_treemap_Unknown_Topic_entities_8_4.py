
import matplotlib.pyplot as plt
import squarify

# Data
disorders = [
    'Anxiety Disorders', 'Major Depressive Disorder', 'Bipolar Disorder',
    'Obsessive-Compulsive Disorder', 'Schizophrenia', 'PTSD', 
    'Eating Disorders', 'ADHD', 'Borderline Personality Disorder', 
    'Other Disorders'
]
prevalence = [18.1, 7.1, 2.8, 1.2, 1.0, 3.6, 2.7, 4.4, 1.6, 7.5]
colors = [
    '#FF6347', '#4682B4', '#9ACD32', '#DAA520', '#87CEEB', '#8A2BE2', 
    '#FF1493', '#7FFF00', '#FF4500', '#00CED1'
]

# Create a figure with specified size
plt.figure(figsize=(12, 10))

# Create a treemap with the above data
squarify.plot(sizes=prevalence, label=disorders, color=colors, alpha=0.7)

# Title of the treemap
plt.title('Distribution of Mental Health Disorders in 2023', fontsize=20, y=1.05)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()