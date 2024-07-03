
import matplotlib.pyplot as plt
import squarify

# Data
topics = [
    'Mental Health', 'Nutrition', 'Exercise Science', 'Sleep Studies', 'Public Health', 
    'Cognitive Psychology', 'Developmental Psychology', 'Clinical Psychology', 'Neuropsychology', 
    'Sports Psychology', 'Behavioral Science', 'Health Education', 'Occupational Therapy', 
    'Substance Abuse', 'Social Psychology', 'Health Informatics', 'Community Health', 
    'Medical Ethics', 'Psychopharmacology', 'Rehabilitation'
]
pages = [
    520, 410, 300, 590, 570, 470, 620, 540, 510, 450, 430, 490, 360, 380, 
    400, 450, 420, 430, 460, 440
]

# Colors
colors = [
    '#FF4500', '#32CD32', '#1E90FF', '#FFD700', '#8A2BE2', '#FF6347', '#7FFF00', 
    '#DC143C', '#00CED1', '#FF1493', '#6495ED', '#FF69B4', '#7B68EE', '#00FA9A', 
    '#D2691E', '#9400D3', '#9370DB', '#48D1CC', '#ADFF2F', '#FFB6C1'
]

plt.figure(figsize=(20, 16))

# Treemap
squarify.plot(sizes=pages, label=topics, color=colors, alpha=0.85)

plt.title('Page Distribution of Topics in Health & Psychology', fontsize=26, pad=30)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()