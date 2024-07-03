
import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
historical_figures = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210]
inventions = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
artworks = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

fig, ax = plt.subplots(figsize=(14, 10))
ax.stackplot(months, historical_figures, inventions, artworks, colors=['#4682B4', '#FFA07A', '#8A2BE2'])

ax.set_title('Cultural Milestones in 2023', pad=20)
ax.set_ylabel('Count')
ax.set_xlabel('Month')
ax.margins(0, 0)

ax.annotate('Peak in Historical Figures', xy=('December', 210), xytext=('November', 230),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()