
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
rainfall = [120, 100, 150, 170, 180, 190, 210, 230, 220, 160, 140, 130]

# Color scheme using specific color codes
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#33FFA7', 
          '#FF8C33', '#33FFF0', '#FF3333', '#33A8FF', '#FF33D4', '#33FF83']

# Create horizontal bar chart
plt.figure(figsize=(14, 8))
bars = plt.barh(months, rainfall, color=colors, height=0.5)

# Adjusting the height of bars
for bar in bars:
    bar.set_height(0.4)

# Changing the layout and labels
plt.xlabel('Rainfall (mm)', fontsize=12)
plt.title('Monthly Rainfall Data in mm for a Tropical Region', fontsize=16, pad=20)
plt.xlim(min(rainfall) - 20, max(rainfall) + 30)  # Set x-axis limit higher to accommodate labels

# Adding value labels next to each bar
for i, v in enumerate(rainfall):
    plt.text(v + 5, i, str(v), color='black', va='center', fontsize=11)

# Show the final result
plt.tight_layout()
plt.show()