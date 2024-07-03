
import matplotlib.pyplot as plt

days = list(range(1, 31))
engagement = [95, 93, 97, 90, 88, 85, 83, 80, 78, 75, 73, 70, 68, 65, 63, 60, 58, 55, 53, 50, 48, 45, 43, 40, 38, 35, 33, 30, 28, 25]

plt.figure(figsize=(18, 9))

plt.plot(days, engagement, color='#1E90FF', linewidth=2.5)

plt.annotate('Lowest Engagement', xy=(30, 25), xytext=(25, 30),
             arrowprops=dict(facecolor='#FFD700', shrink=0.05))

plt.title('Daily User Engagement in February', pad=20, fontsize=16)
plt.xlabel('Day')
plt.ylabel('Engagement')
plt.gca().invert_yaxis()

plt.show()