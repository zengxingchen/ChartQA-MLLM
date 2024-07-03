
import matplotlib.pyplot as plt
import squarify

# Data
topic = [
    'Reading', 'Writing', 'Exercise', 'Cooking', 'Gaming', 'Watching TV', 'Traveling', 'Socializing', 
    'Meditation', 'Gardening', 'Painting', 'Music', 'Shopping', 'Sleeping', 'Learning', 'Working', 
    'Cleaning', 'Sports', 'Volunteering'
]
hours_spent = [
    120, 100, 90, 80, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1
]
color_code = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22'
]

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=hours_spent, label=topic, color=color_code, alpha=0.8)
plt.title('How People Spend Their Free Time', fontsize=24, pad=40)
plt.axis('off')
plt.show()