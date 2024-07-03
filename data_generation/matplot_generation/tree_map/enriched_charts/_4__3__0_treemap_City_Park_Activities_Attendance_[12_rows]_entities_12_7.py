
import matplotlib.pyplot as plt
import squarify

# Data points
conditions = ['Anxiety', 'Depression', 'Bipolar Disorder', 'Schizophrenia', 'PTSD', 'OCD', 
              'Eating Disorders', 'ADHD', 'Autism Spectrum Disorder', 'Social Anxiety Disorder', 
              'Generalized Anxiety Disorder', 'Panic Disorder', 'Phobias', 'Borderline Personality Disorder', 
              'Dissociative Disorders']
prevalence_in_millions = [264, 322, 45, 20, 85, 60, 70, 129, 75, 200, 68, 52, 250, 14, 23]
colors = ['#FF7F50', '#6495ED', '#FF69B4', '#CD5C5C', '#FFA500', '#8A2BE2', '#7FFF00', 
          '#DC143C', '#00FFFF', '#00008B', '#B8860B', '#A9A9A9', '#006400', '#8B0000', '#2F4F4F']

# Plot Dimensions
plt.figure(figsize=(16, 12))

# Create a treemap
squarify.plot(sizes=prevalence_in_millions, label=conditions, color=colors, alpha=0.8)

# Title
plt.title('Prevalence of Mental Health Conditions (in Millions)', fontsize=22)

# Remove axes
plt.axis('off')

# Show plot
plt.show()