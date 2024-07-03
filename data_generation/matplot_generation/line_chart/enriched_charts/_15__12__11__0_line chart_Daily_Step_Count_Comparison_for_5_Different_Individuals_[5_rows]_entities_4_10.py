
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue_millions = [120, 150, 170, 200, 180, 160, 140, 130, 150, 170, 190, 210]

plt.figure(figsize=(16, 12))
plt.plot(months, revenue_millions, color='#ff5733', marker='o')  # Trend with color code

# Adding labels with annotations
for i, (month, revenue) in enumerate(zip(months, revenue_millions)):
    plt.annotate(f'{revenue}M', (month, revenue), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Revenue for ABC Corp (2023)', pad=20, fontsize=18)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Revenue (in millions)', fontsize=14)

# Invert y-axis
plt.gca().invert_yaxis()

# Display chart
plt.show()