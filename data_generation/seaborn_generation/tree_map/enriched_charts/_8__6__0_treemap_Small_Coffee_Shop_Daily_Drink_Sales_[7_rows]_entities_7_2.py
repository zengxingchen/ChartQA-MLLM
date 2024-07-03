
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Data for treemap
data = {
    'Practice': [
        'Cognitive Behavioral Therapy', 'Mindfulness Meditation', 'Art Therapy', 'Music Therapy', 
        'Exercise Therapy', 'Dialectical Behavior Therapy', 'Psychodynamic Therapy', 'Narrative Therapy', 
        'Hypnotherapy', 'Biofeedback', 'Animal-Assisted Therapy', 'Electroconvulsive Therapy', 
        'Virtual Reality Therapy', 'Light Therapy', 'Transcranial Magnetic Stimulation', 
        'Acceptance and Commitment Therapy', 'Play Therapy', 'Gestalt Therapy', 
        'Existential Therapy', 'Somatic Therapy'
    ],
    'AdoptionRate': [
        300, 280, 220, 250, 270, 240, 230, 200, 190, 180, 
        170, 160, 150, 140, 130, 120, 110, 100, 90, 80
    ]
}

# Convert the data into DataFrame
df = pd.DataFrame(data)

# Define color palette
colors = [
    '#3498db', '#2ecc71', '#e74c3c', '#9b59b6', '#f1c40f',
    '#e67e22', '#1abc9c', '#ecf0f1', '#34495e', '#95a5a6',
    '#d35400', '#c0392b', '#2980b9', '#27ae60', '#8e44ad',
    '#f39c12', '#16a085', '#7f8c8d', '#2c3e50', '#bdc3c7'
]

# Create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(16, 10))

# Create a treemap
squarify.plot(sizes=df['AdoptionRate'], label=df['Practice'], alpha=0.8, color=colors, ax=ax)

# Remove the axes
plt.axis('off')

# Add a title
plt.title('Adoption Rates of Mental Health Practices', fontsize=24, pad=20)

# Show the plot
plt.show()