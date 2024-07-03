
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
star_discoveries = [80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170]
planetary_missions = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
space_research_papers = [100, 110, 120, 130, 140, 160, 170, 180, 200, 210, 220, 240]

fig, ax = plt.subplots(figsize=(16, 8))
ax.stackplot(months, star_discoveries, planetary_missions, space_research_papers, colors=['#FFD700', '#FF4500', '#1E90FF'])

ax.set_title('Astronomy & Space Exploration Activities in 2023', pad=20)
ax.set_ylabel('Count')
ax.set_xlabel('Month')
ax.margins(0, 0)

ax.annotate('Peak in Space Research Papers', xy=('December', 240), xytext=('October', 250),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.legend(['Star Discoveries', 'Planetary Missions', 'Space Research Papers'], loc='upper left')

plt.show()