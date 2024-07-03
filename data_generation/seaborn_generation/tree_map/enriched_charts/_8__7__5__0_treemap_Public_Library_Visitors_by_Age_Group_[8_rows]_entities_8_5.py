
import matplotlib.pyplot as plt
import squarify

conditions = [
    'Depression', 'Anxiety', 'Bipolar Disorder', 'PTSD', 'OCD', 'Schizophrenia', 'Eating Disorders', 
    'ADHD', 'Autism', 'Panic Disorder', 'Social Anxiety', 'Specific Phobias', 'Substance Abuse', 
    'Borderline Personality Disorder', 'Dissociative Disorders', 'Paranoia', 'Delusional Disorder', 
    'Hoarding Disorder', 'Body Dysmorphic Disorder', 'Somatic Symptom Disorder'
]
count = [
    1500, 1300, 1100, 950, 800, 750, 700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50
]

color_palette = [
    '#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', 
    '#bc80bd', '#ccebc5', '#ffed6f', '#e5c494', '#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99', 
    '#e31a1c', '#fdbf6f'
]

plt.figure(figsize=(24, 14))

squarify.plot(sizes=count, label=conditions, color=color_palette, alpha=0.8)

plt.title('Distribution of Various Mental Health Conditions', fontsize=24, fontweight='bold', pad=30)
plt.axis('off')

plt.show()