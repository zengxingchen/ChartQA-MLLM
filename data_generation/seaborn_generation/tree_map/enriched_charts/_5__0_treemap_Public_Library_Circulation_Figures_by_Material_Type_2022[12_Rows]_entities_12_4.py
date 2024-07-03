
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# Data for the treemap
data = {
    'Subject': ['Philosophy', 'Ethics', 'Science', 'Nature', 'History', 'Archaeology', 'Health', 
               'Psychology', 'Travel', 'Adventure', 'Fashion', 'Beauty', 'Sports', 'Fitness', 
               'Economics', 'Finance'],
    'Participants': [450, 350, 300, 250, 200, 150, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
    'Percentage': [0.18, 0.14, 0.12, 0.10, 0.08, 0.06, 0.04, 0.036, 0.032, 0.028, 0.024, 0.020, 0.016, 0.012, 0.008, 0.004]
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define color list
colors = ['#4B0082', '#FF4500', '#2E8B57', '#1E90FF', '#FFD700', '#FF69B4', '#8A2BE2', 
          '#FF6347', '#4682B4', '#DA70D6', '#32CD32', '#FF1493', '#6495ED', '#DC143C', 
          '#8B4513', '#7FFF00']

# Plot the Treemap
plt.figure(figsize=(14, 10))
squarify.plot(sizes=df['Percentage'], label=df['Subject'], color=colors, alpha=0.8)
plt.title('Interest in Various Subjects among Participants', fontsize=20)
plt.axis('off')
plt.show()