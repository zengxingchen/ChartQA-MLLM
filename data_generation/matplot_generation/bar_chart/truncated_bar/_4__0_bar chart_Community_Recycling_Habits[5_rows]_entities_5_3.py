
import matplotlib.pyplot as plt

# Data
exercises = ['Running', 'Cycling', 'Yoga', 'Swimming', 'Hiking', 'Weightlifting', 'Pilates', 'Rowing', 'Dancing', 'Boxing']
participants = [15000, 12000, 10000, 8000, 7500, 7000, 6500, 6000, 5500, 5000]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#76d7c4','#ff6f61','#6b5b95']

# Figure size
plt.figure(figsize=(12, 6))

# Vertical bar chart
plt.bar(exercises, participants, color=colors, width=0.5)

# Labeling
plt.ylabel('Number of Participants')
plt.title('Top 10 Popular Fitness Activities')
plt.ylim(4000, 16000)  # Truncate y-axis to start from 4000

# Show and save plot
plt.tight_layout()
plt.show()