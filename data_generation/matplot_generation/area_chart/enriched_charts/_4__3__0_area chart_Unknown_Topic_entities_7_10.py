
import matplotlib.pyplot as plt

# Data for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

sign_ups = [850, 920, 1020, 1100, 950, 1130, 1180, 1250, 1300, 1400, 1350, 1450]

# Plotting the area chart
plt.figure(figsize=(16, 9))
plt.fill_between(months, sign_ups, color='#ff5733')

# Adding labels and title
plt.title('Monthly Gym Membership Sign-Ups Over a Year', pad=30)
plt.xlabel('Month')
plt.ylabel('Number of Sign-Ups')

# Customizing the grid
plt.grid(True, color='#b3b3b3', linestyle='-', linewidth=0.6, which='both')

# Adjusting the x-axis labels to fit properly
plt.xticks(rotation=45)

# Annotating the chart with text labels
for i, val in enumerate(sign_ups):
    plt.text(i, val + 20, str(val), ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()