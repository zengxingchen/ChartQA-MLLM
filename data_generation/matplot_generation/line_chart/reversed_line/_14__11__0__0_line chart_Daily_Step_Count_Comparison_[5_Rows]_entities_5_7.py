
import matplotlib.pyplot as plt

# Data
months = ['2022-Jan', '2022-Feb', '2022-Mar', '2022-Apr', '2022-May', '2022-Jun', '2022-Jul', '2022-Aug', '2022-Sep', '2022-Oct', '2022-Nov', '2022-Dec']
study_hours = [20, 18, 22, 25, 23, 26, 24, 27, 28, 30, 29, 32]

# Plotting the line chart
plt.figure(figsize=(12, 8))  # Adjusted width and height
plt.plot(months, study_hours, color='#3498DB', marker='s', linestyle='-', linewidth=2)  # Different color and marker style

# Annotate a specific point with the label
plt.annotate('Exam Month', xy=('2022-Dec', 32), xytext=('2022-Sep', 28),
             arrowprops=dict(facecolor='#E74C3C', arrowstyle='->'))

# Adding a title and labels
plt.title('Monthly Average Study Hours of Students in 2022', pad=20)  # Changed topic and added padding
plt.xlabel('Month')
plt.ylabel('Study Hours')
plt.gca().invert_yaxis()

# Show the plot
plt.show()