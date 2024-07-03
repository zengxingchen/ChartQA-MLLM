
import matplotlib.pyplot as plt
import squarify

# Data
sports = [
    'Soccer', 'Badminton', 'Field Hockey', 'Volleyball', 'Basketball', 
    'Tennis', 'Cricket', 'Table Tennis', 'Baseball', 'Golf', 
    'Cycling', 'Swimming', 'Running', 'Boxing', 'Skiing', 
    'Skateboarding', 'Surfing', 'Weightlifting', 'Martial Arts'
]
participants = [
    4000, 2200, 2000, 900, 450, 300, 300, 300, 500, 450, 
    130, 260, 250, 70, 120, 85, 20, 100, 50
]
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', 
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22'
]

# Plot
plt.figure(figsize=(16, 12))
squarify.plot(sizes=participants, label=sports, color=colors, alpha=0.7)
plt.title('Most Popular Sports by Estimated Number of Participants Worldwide (in Millions)', fontsize=20, pad=20)
plt.axis('off')
plt.show()