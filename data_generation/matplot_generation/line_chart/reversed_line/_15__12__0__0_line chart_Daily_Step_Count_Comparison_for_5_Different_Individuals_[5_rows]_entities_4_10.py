
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calorie_intake = [1800, 1650, 1850, 1900, 1800, 2000, 2100, 1950, 1850, 1700, 1650, 1600]

# Adjust data for visualization
calorie_intake[2] += 50   # March
calorie_intake[8] -= 100  # September

# Modify color scheme, figure size, and data trend
plt.figure(figsize=(12, 7))
plt.plot(months, [cal + 200 if i % 2 == 0 else cal - 100 for i, cal in enumerate(calorie_intake)], color='#e74c3c', marker='o')

# Adding labels with annotations
for i, (month, cal) in enumerate(zip(months, calorie_intake)):
    adjusted_cal = cal + 200 if i % 2 == 0 else cal - 100
    plt.annotate(f'{cal}', (month, adjusted_cal), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Average Calorie Intake - Sports & Fitness')
plt.xlabel('Month')
plt.ylabel('Calorie Intake')
plt.gca().invert_yaxis()

# Display chart
plt.show()