
import matplotlib.pyplot as plt

sports = ['Soccer', 'Cricket', 'Basketball', 'Baseball', 'Rugby', 'Tennis', 'Badminton', 'Volleyball', 'Table Tennis', 'Golf', 'Hockey', 'Swimming']
participants = [265, 125, 450, 500, 10, 75, 220, 800, 300, 60, 2, 28]

colors = ['#FF6347', '#FFD700', '#8A2BE2', '#5F9EA0', '#D2691E', '#DC143C', '#00FFFF', '#008B8B', '#B8860B', '#006400', '#B22222', '#FF4500']

plt.figure(figsize=(10, 12))
plt.bar(sports, participants, color=colors, edgecolor='black', width=0.6)

plt.ylabel('Number of Participants (in millions)', fontsize=12)
plt.xlabel('Sport', fontsize=12)
plt.title('Number of Participants in Various Sports', fontsize=16)
plt.ylim(0, 850)

plt.tight_layout()
plt.show()