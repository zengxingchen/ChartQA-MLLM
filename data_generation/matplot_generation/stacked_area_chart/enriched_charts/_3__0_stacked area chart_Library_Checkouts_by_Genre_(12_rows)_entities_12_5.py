
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
running = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100]
cycling = [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]
swimming = [600, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(months, running, cycling, swimming, colors=['#e41a1c', '#377eb8', '#4daf4a'])

# Customizing the plot
ax.set_title('Monthly Calories Burned by Activity Type in 2023', fontsize=16)
ax.set_ylabel('Calories Burned')
ax.set_xlabel('Month')
ax.margins(0, 0)  # Use the entire plotting area

# Adding annotation
ax.annotate('Peak in Running', xy=('December', 2100), xytext=('October', 3000),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Adding legend
ax.legend(['Running', 'Cycling', 'Swimming'], loc='upper left')

# Displaying the plot
plt.show()