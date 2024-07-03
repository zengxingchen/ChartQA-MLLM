
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calories_burned_kcal = [300, 350, 450, 500, 600, 700, 800, 750, 650, 550, 400, 350]

plt.figure(figsize=(14, 10))
plt.plot(months, calories_burned_kcal, color='#1f77b4', marker='o')

# Adding labels with annotations
for i, (month, cal) in enumerate(zip(months, calories_burned_kcal)):
    plt.annotate(f'{cal} kcal', (month, cal), textcoords="offset points", xytext=(0,10), ha='center')

# Invert y-axis
plt.gca().invert_yaxis()

# Adding title and labels
plt.title('Monthly Calories Burned During Workouts in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Calories Burned (kcal)')

# Display chart
plt.show()