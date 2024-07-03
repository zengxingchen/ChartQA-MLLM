
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
sunshine_hours = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]

# Changes to data to enrich visualization
sunshine_hours[5] += 10  # June
sunshine_hours[-2] -= 15  # November

# Modify color scheme with color codes, change figure size, change trend by adjusting the scores
plt.figure(figsize=(12, 7))
plt.plot(months, [score + 10 if i % 2 == 0 else score - 10 for i, score in enumerate(sunshine_hours)], 
         color='#e74c3c', marker='s', linestyle='-')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, score) in enumerate(zip(months, sunshine_hours)):
    adjusted_score = score + 10 if i % 2 == 0 else score - 10
    plt.annotate(f'{score}', (month, adjusted_score), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Sunshine Hours in 2023', pad=20)
plt.xlabel('Month')
plt.ylabel('Sunshine Hours')

# Display chart
plt.gca().invert_yaxis()
plt.show()