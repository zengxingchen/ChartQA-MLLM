
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = {
    'Activity': [
        "Yoga for Stress Relief", "Mindfulness Meditation Sessions", "Nutrition and Diet Workshops",
        "Mental Health Awareness Campaign", "Physical Fitness Programs", "Sleep Improvement Techniques",
        "Community Support Groups", "Digital Detox Retreats", "Art Therapy Workshops", "Healthy Eating Campaign",
        "Exercise and Wellbeing Classes", "Outdoor Adventure Therapy", "Music Therapy Sessions",
        "Self-Care and Wellness Retreats", "Stress Management Seminars", "Holistic Health Fairs",
        "Healthy Lifestyle Coaching", "Emotional Intelligence Training", "Family Health Education",
        "Preventive Health Checkups"
    ],
    'Impact': [
        48000, 35000, 42000, 39000, 46000, 31000, 27000, 32000, 29000, 37000,
        34000, 41000, 30000, 33000, 45000, 28000, 36000, 40000, 38000, 43000
    ]
}

df = pd.DataFrame(data)

plt.figure(figsize=(18,14))

colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#9edae5', '#f7b6d2',
    '#c5b0d5', '#ffbb78', '#c49c94', '#dbdb8d', '#98df8a', '#ff9896',
    '#c7c7c7', '#c44e52'
]

squarify.plot(sizes=df['Impact'], label=df['Activity'], color=colors, alpha=0.8)

plt.title('Impact of Health & Wellness Activities', fontsize=20, pad=30)
plt.axis('off')
plt.show()