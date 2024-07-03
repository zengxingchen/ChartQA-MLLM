
import matplotlib.pyplot as plt

# Data points
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
box_office_revenue = [500, 450, 480, 470, 520, 530, 560, 550, 540, 530, 570, 580]

# Create the plot
plt.figure(figsize=(14, 7))
plt.plot(months, box_office_revenue, marker='o', linestyle='-', color='#1E90FF')

# Annotate the highest and lowest box office revenue points
plt.annotate('Highest\n580$', xy=('December', 580), xytext=('November', 575),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')
plt.annotate('Lowest\n450$', xy=('February', 450), xytext=('March', 455),
             arrowprops=dict(facecolor='#FF4500', shrink=0.05), color='#FF4500')

# Title and labels
plt.title('Monthly Box Office Revenue in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Revenue ($)')

# Customize the grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the plot
plt.gca().invert_yaxis()  # Invert y-axis

# Show the plot
plt.show()