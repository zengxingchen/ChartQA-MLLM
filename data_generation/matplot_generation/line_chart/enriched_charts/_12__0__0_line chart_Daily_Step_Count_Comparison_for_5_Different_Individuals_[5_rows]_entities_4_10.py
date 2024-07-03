
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calorie_intake = [2000, 1950, 2100, 2200, 2150, 2300, 2350, 2400, 2250, 2100, 2050, 1980]

# Changes to data to enrich visualization
calorie_intake[5] += 100  # June
calorie_intake[11] -= 50  # December

# Modify color scheme with color codes, change figure size, change trend by adjusting the scores
plt.figure(figsize=(14, 8))
plt.plot(months, [cal + 150 if i % 2 == 0 else cal - 150 for i, cal in enumerate(calorie_intake)], 
         color='#3498db', marker='o')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, cal) in enumerate(zip(months, calorie_intake)):
    adjusted_cal = cal + 150 if i % 2 == 0 else cal - 150
    plt.annotate(f'{cal}', (month, adjusted_cal), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Average Calorie Intake')
plt.xlabel('Month')
plt.ylabel('Calorie Intake')

# Display chart
plt.show()