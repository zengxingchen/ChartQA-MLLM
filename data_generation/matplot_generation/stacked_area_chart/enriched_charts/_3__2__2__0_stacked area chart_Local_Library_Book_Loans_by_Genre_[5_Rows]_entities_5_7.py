
import matplotlib.pyplot as plt

years = list(range(2011, 2023))
ai_research = [30, 35, 40, 45, 55, 60, 70, 85, 100, 120, 140, 160]
robotics = [40, 45, 50, 55, 60, 70, 80, 95, 110, 130, 155, 180]
quantum_computing = [10, 15, 20, 25, 35, 40, 50, 60, 75, 90, 110, 135]

fig, ax = plt.subplots(figsize=(16, 10))

ax.stackplot(years, ai_research, robotics, quantum_computing, colors=['#003f5c', '#bc5090', '#ffa600'])

ax.annotate('Surge in AI Research', xy=(2020, 120), xytext=(2015, 90), arrowprops=dict(facecolor='#003f5c', shrink=0.05))
ax.annotate('Rise in Robotics', xy=(2020, 130), xytext=(2016, 160), arrowprops=dict(facecolor='#bc5090', shrink=0.05))

plt.xlabel('Year')
plt.ylabel('Funding (in millions)')
plt.title('Investment in Future Technologies (2011-2022)', pad=20)

plt.legend(['AI Research', 'Robotics', 'Quantum Computing'], loc='upper left')

plt.show()