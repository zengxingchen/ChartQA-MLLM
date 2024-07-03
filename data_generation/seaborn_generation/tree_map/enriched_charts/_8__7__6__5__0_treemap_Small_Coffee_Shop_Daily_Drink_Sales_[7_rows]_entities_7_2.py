
import pandas as pd
import matplotlib.pyplot as plt
import squarify

data = {
    'Category': [
        'Cognitive Behavioral Therapy', 'Mindfulness', 'Psychodynamic Therapy', 'Art Therapy',
        'Music Therapy', 'Occupational Therapy', 'Speech Therapy', 'Physical Therapy',
        'Sports Psychology', 'Neuropsychology', 'Clinical Psychology', 'Counseling Psychology',
        'Educational Psychology', 'Forensic Psychology', 'Health Psychology', 
        'Human Factors Psychology', 'Industrial-Organizational Psychology', 
        'Developmental Psychology', 'School Psychology', 'Community Psychology'
    ],
    'Values': [
        210, 180, 190, 160, 170, 185, 175, 195, 155, 145, 
        165, 135, 125, 115, 105, 95, 85, 75, 65, 155
    ]
}

df = pd.DataFrame(data)

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

fig, ax = plt.subplots(1, figsize=(24, 18))

squarify.plot(sizes=df['Values'], label=df['Category'], alpha=0.8, color=colors)

plt.axis('off')

plt.title('Health & Psychology Topics and Their Importance', fontsize=26, pad=30)

plt.show()