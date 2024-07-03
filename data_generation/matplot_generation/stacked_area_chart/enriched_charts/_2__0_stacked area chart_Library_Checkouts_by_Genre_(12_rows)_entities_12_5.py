
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
research_funding = [50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000, 105000]
publications = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
patents = [2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(12, 7))
ax.stackplot(months, research_funding, publications, patents, colors=['#4c72b0', '#dd8452', '#55a868'])

# Customizing the plot
ax.set_title('Monthly Research Performance in 2023', pad=20)
ax.set_ylabel('Count/Funding')
ax.set_xlabel('Month')
ax.margins(0, 0)

# Adding annotation
ax.annotate('Peak Funding', xy=('December', 105000), xytext=('October', 110000),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Publications surge', xy=('November', 30), xytext=('September', 35),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Displaying the plot
plt.show()