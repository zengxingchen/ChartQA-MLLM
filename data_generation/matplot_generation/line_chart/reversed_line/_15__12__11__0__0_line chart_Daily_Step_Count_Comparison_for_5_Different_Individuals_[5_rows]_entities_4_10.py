
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
population_growth = [1.2, 1.5, 1.8, 1.6, 2.0, 2.4, 2.3, 2.6, 2.9, 2.8, 3.2, 3.5]

# Adjust some data points to enrich the visualization
population_growth[2] += 0.3  # March
population_growth[9] -= 0.2  # October

# Modify color scheme and figure size
plt.figure(figsize=(14, 8))
plt.plot(months, population_growth, color='#3498db', marker='o', linestyle='--')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, growth) in enumerate(zip(months, population_growth)):
    plt.annotate(f'{growth}', (month, growth), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Population Growth in 2023 (in thousands)')
plt.xlabel('Month')
plt.ylabel('Population Growth (in thousands)')
plt.gca().invert_yaxis()  # Invert y-axis for the specified visualization

# Display chart
plt.show()