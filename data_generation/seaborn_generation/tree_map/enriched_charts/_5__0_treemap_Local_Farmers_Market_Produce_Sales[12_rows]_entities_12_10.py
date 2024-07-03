
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Define the data
data = {
    'Condition': [
        'Anxiety Disorders', 'Depressive Disorders', 'Bipolar Disorder', 'Schizophrenia', 
        'Eating Disorders', 'Obsessive-Compulsive Disorder', 'Post-Traumatic Stress Disorder', 
        'Attention Deficit Hyperactivity Disorder', 'Autism Spectrum Disorders', 
        'Substance Use Disorders', 'Dementia', 'Intellectual Disabilities', 
        'Sleep Disorders', 'Phobias'
    ],
    'Prevalence (Millions)': [
        264, 322, 45, 20, 70, 50, 44, 129, 75, 180, 50, 150, 150, 100
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a color palette
colors = [
    '#FF6347', '#FFD700', '#FF4500', '#ADFF2F', '#00FA9A', '#00CED1', 
    '#1E90FF', '#BA55D3', '#FF69B4', '#FF6347', '#FFD700', '#FF4500', 
    '#ADFF2F', '#00FA9A'
]

# Define size of the figure
plt.figure(figsize=(18, 10))

# Plot the treemap with the specified colors and data
squarify.plot(sizes=df['Prevalence (Millions)'], label=df['Condition'], color=colors, alpha=0.8)

plt.title('Global Mental Health Conditions by Prevalence (in Millions)', fontsize=22)
plt.axis('off')
plt.show()