
import matplotlib.pyplot as plt
import squarify

# Data
research_topics = ['Quantum Mechanics', 'Evolutionary Biology', 'Climate Change', 'Artificial Intelligence', 'Neuroscience', 'Renewable Energy', 'Astrophysics', 'Genetic Engineering', 'Marine Biology', 'Cybersecurity', 'Organic Chemistry', 'Sustainable Agriculture', 'Space Exploration', 'Nanotechnology', 'Robotics', 'Environmental Science', 'Biotechnology', 'Theoretical Physics', 'Geology', 'Material Science']
pages = [480, 380, 290, 620, 530, 450, 610, 420, 330, 510, 370, 340, 590, 440, 480, 380, 560, 510, 430, 470]

# Colors
colors = ['#66CDAA', '#FF7F50', '#8A2BE2', '#FFD700', '#7FFF00', '#6495ED', '#FF69B4', '#1E90FF', '#DC143C', '#00CED1', '#FF1493', '#7B68EE', '#D2691E', '#00FA9A', '#9400D3', '#FFB6C1', '#9370DB', '#48D1CC', '#ADFF2F', '#FF6347']

plt.figure(figsize=(18, 14))

# Treemap
squarify.plot(sizes=pages, label=research_topics, color=colors, alpha=0.85)

plt.title('Page Distribution of Research Topics in Science & Nature', fontsize=26, pad=20)

# Removing axes
plt.axis('off')

# Display the plot
plt.show()