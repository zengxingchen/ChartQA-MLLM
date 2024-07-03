
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calorie_intake_kcal = [2200, 2250, 2300, 2350, 2400, 2450, 2550, 2500, 2450, 2400, 2300, 2150]

# Changes to data to enrich visualization (slightly higher July and lower December for example)
calorie_intake_kcal[6] += 50  # July
calorie_intake_kcal[-1] -= 50  # December

# Modify color scheme with color codes, change figure size, change trend by increasing the calories
plt.figure(figsize=(12, 7))
plt.plot(months, [cal + 100 for cal in calorie_intake_kcal], color='#ff5733', marker='o')  # Increase trend with color code

# Adding labels with annotations
for i, (month, cal) in enumerate(zip(months, calorie_intake_kcal)):
    increased_cal = cal + 100
    plt.annotate(f'{cal} kcal', (month, increased_cal), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Average Calorie Intake with Increased Trend')
plt.xlabel('Month')
plt.ylabel('Calorie Intake (kcal)')

# Display chart
plt.show()