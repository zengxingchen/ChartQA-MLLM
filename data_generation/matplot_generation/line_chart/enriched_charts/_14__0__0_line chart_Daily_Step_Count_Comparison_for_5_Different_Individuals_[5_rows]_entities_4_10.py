
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
attendance = [78, 82, 75, 88, 92, 85, 80, 77, 90, 83, 79, 74]

# Changes to data to enrich visualization
attendance[4] += 3  # May
attendance[-1] -= 4  # December

# Modify color scheme with color codes, change figure size, change trend by adjusting the scores
plt.figure(figsize=(10, 6))
plt.plot(months, [score + 5 if i % 2 == 0 else score - 5 for i, score in enumerate(attendance)], 
         color='#1f77b4', marker='o')  # Adjusted trend with color code

# Adding labels with annotations
for i, (month, score) in enumerate(zip(months, attendance)):
    adjusted_score = score + 5 if i % 2 == 0 else score - 5
    plt.annotate(f'{score}', (month, adjusted_score), textcoords="offset points", xytext=(0,10), ha='center')

# Adding title and labels
plt.title('Monthly Attendance at Sports Events')
plt.xlabel('Month')
plt.ylabel('Attendance')
plt.gca().invert_yaxis()  # Invert y-axis

# Display chart
plt.show()