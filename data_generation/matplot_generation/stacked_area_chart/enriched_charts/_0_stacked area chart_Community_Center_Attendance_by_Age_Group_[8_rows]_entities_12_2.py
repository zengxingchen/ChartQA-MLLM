
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']
rent = [800, 820, 830, 850, 860, 880, 900, 910, 930, 950, 970, 1000]
utilities = [150, 160, 155, 158, 165, 170, 175, 180, 185, 190, 195, 200]
groceries = [300, 320, 310, 305, 315, 325, 330, 335, 345, 350, 360, 370]
entertainment = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 220, 230]
transportation = [75, 80, 85, 90, 95, 100, 105, 110, 120, 125, 130, 135]

fig, ax = plt.subplots(figsize=(12, 6))

# Stacking the data
y = np.vstack([rent, utilities, groceries, entertainment, transportation])

# Colors
colors = ['#FFD700', '#FF8C00', '#1E90FF', '#32CD32', '#FF1493']

# Plotting the stacked area chart
ax.stackplot(months, y, labels=['Rent', 'Utilities', 'Groceries', 'Entertainment', 'Transportation'], colors=colors)

# Annotating specific points
ax.annotate('Highest rent', xy=('December', 1000), xytext=('November', 1100),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Peak entertainment', xy=('December', 230 + sum(y[:-1, -1])), xytext=('November', 230 + sum(y[:-1, -2])),
            arrowprops=dict(facecolor='orange', shrink=0.05))

# Adding title and labels
ax.set_title('Monthly Expenses Breakdown')
ax.set_xlabel('Month')
ax.set_ylabel('Expenses (USD)')

# Adding legend
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()