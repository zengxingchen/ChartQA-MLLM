
import matplotlib.pyplot as plt
import squarify

# Data points
countries = ['USA', 'Russia', 'China', 'India', 'Japan', 'France', 'Germany', 'Canada', 'Italy', 'UK', 
             'Brazil', 'Israel', 'Australia', 'Spain', 'Argentina', 'South Korea', 'Netherlands', 
             'Sweden', 'Ukraine', 'South Africa', 'Mexico']
space_missions = [135, 110, 90, 70, 50, 40, 35, 30, 28, 25, 22, 20, 18, 15, 13, 12, 10, 8, 6, 5, 3]
colors = ['#FF6347', '#FFD700', '#ADFF2F', '#00FF7F', '#4682B4', '#6A5ACD', '#FF69B4', '#8A2BE2', '#DC143C', 
          '#7FFF00', '#FF4500', '#2E8B57', '#8B008B', '#9932CC', '#FF1493', '#00CED1', '#FF6347', '#FFD700', 
          '#ADFF2F', '#00FF7F', '#4682B4']

# Plot Dimensions
plt.figure(figsize=(18, 14))

# Create a treemap
squarify.plot(sizes=space_missions, label=countries, color=colors, alpha=0.8)

# Title
plt.title('Number of Space Missions by Country', fontsize=22, pad=30)

# Remove axes
plt.axis('off')

# Show plot
plt.show()