import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
domestic = [1000, 1200, 1500, 1800, 1600, 1400, 2000, 2300, 2500, 2700, 3000, 3200]
international = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420]
exchange = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

fig, ax = plt.subplots(figsize=(16, 12))
ax.stackplot(months, domestic, international, exchange, colors=['#FF5733', '#33FF57', '#3357FF'])

ax.set_title('Monthly Student Enrollment in 2023 by Category', fontsize=18, loc='right')
ax.set_ylabel('Number of Students', fontsize=15)
ax.set_xlabel('Month', fontsize=15)
ax.margins(0, 0)

ax.annotate('Highest Domestic Enrollment', xy=('December', 3200), xytext=('November', 3500),
            arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()