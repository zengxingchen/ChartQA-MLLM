
import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
urban_traffic = [150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]
suburban_traffic = [200, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320]
rural_traffic = [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]

# Stacked Area Chart
fig, ax = plt.subplots(figsize=(14, 10))
ax.stackplot(months, urban_traffic, suburban_traffic, rural_traffic, colors=['#FF5733', '#33FF57', '#3357FF'])

# Customizing the plot
ax.set_title('Monthly Traffic Volume by Area in 2023', pad=20)
ax.set_ylabel('Traffic Volume (Thousands of Vehicles)')
ax.set_xlabel('Month')
ax.margins(0, 0)

# Adding annotation
ax.annotate('Urban Peak', xy=('December', 830), xytext=('November', 880),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Displaying the plot
plt.show()