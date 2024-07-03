
import matplotlib.pyplot as plt
import squarify

# Data for AI and Technology activities
activities = [
    'Artificial Intelligence', 'Machine Learning', 'Natural Language Processing', 'Computer Vision', 
    'Robotics', 'Data Science', 'Neural Networks', 'Deep Learning', 
    'Big Data', 'Predictive Analytics', 'Reinforcement Learning', 'AI Ethics', 
    'AI in Healthcare', 'AI in Finance'
]
market_share = [20.0, 17.5, 15.0, 12.5, 10.0, 8.0, 7.0, 5.5, 4.0, 3.0, 2.5, 2.0, 1.5, 1.0]

# Custom color scheme
colors = [
    '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', 
    '#800000', '#808000', '#008080', '#800080', '#808080', '#FFA500', 
    '#A52A2A', '#5F9EA0'
]

# Treemap
plt.figure(figsize=(16, 12))  # Adjusting the size of the treemap
squarify.plot(sizes=market_share, label=activities, color=colors, alpha=0.8)
plt.title('Popularity of AI & Technology Activities', fontsize=20, pad=40)
plt.axis('off')  # No axes for a cleaner look

plt.show()