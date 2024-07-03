
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the dataset
data = {
    'Type': ['Anxiety', 'Depression', 'Bipolar Disorder', 'Schizophrenia', 
             'Obsessive-Compulsive Disorder', 'Panic Disorder', 'Post-Traumatic Stress Disorder', 
             'Eating Disorders', 'Attention Deficit Hyperactivity Disorder', 'Autism Spectrum Disorders', 
             'Substance Use Disorders', 'Personality Disorders', 'Dissociative Disorders', 'Somatic Symptom Disorder'],
    'Prevalence': [18.1, 6.7, 2.6, 1.1, 1.2, 2.7, 3.6, 5.7, 4.4, 1.7, 7.2, 9.1, 1.5, 2.0]
}

df = pd.DataFrame(data)

# Define the color scheme
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
          '#bcbd22', '#17becf', '#9edae5', '#dbdb8d', 
          '#c7c7c7', '#ffbb78']

# Create the figure with specified figure size
fig = plt.figure(figsize=(16, 12))
ax = fig.add_subplot(111, aspect="auto")

# Create a treemap
squarify.plot(sizes=df['Prevalence'], label=df['Type'], color=colors, alpha=0.7)

# Set the title of the plot
plt.title('Prevalence of Mental Health Disorders', fontsize=24)

# Remove the axes
plt.axis('off')

# Show the plot
plt.show()