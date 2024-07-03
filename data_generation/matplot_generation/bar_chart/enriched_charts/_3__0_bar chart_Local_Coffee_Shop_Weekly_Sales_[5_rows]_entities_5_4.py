
import matplotlib.pyplot as plt

# Data
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = [8000, 9500, 7000, 8500, 12000, 15000, 10000]

# Color scheme using color codes
colors = ['#1E90FF', '#32CD32', '#FF69B4', '#FFD700', '#FF6347', '#8A2BE2', '#00CED1']

# Create vertical bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(days, steps, color=colors, width=0.5)

# Adjusting the width and height of bars (no need here as it's vertical)

# Changing the layout and labels
plt.ylabel('Steps', fontsize=12)
plt.title('Weekly Step Count', fontsize=16)
plt.ylim(0, max(steps) * 1.1)  # Set y-axis limit higher to accommodate labels

# Adding value labels on top of each bar
for i, v in enumerate(steps):
    plt.text(i, v + 300, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()