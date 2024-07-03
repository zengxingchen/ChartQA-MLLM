
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
attendance = [120, 135, 150, 145, 160, 155, 165, 170, 175, 180, 185, 190, 195, 200, 205, 
              210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285]

# Creating the figure and specifying figure size
plt.figure(figsize=(16, 10))

# Creating the bar chart as a horizontal chart
plt.barh(days, attendance, height=0.5, color=['#4CAF50', '#FFC107', '#2196F3', '#F44336',
                                              '#9C27B0', '#FF9800', '#009688', '#8BC34A',
                                              '#00BCD4', '#E91E63', '#3F51B5', '#CDDC39',
                                              '#FF5722', '#795548', '#607D8B', '#673AB7',
                                              '#FFEB3B', '#FF4081', '#9E9E9E', '#03A9F4',
                                              '#FFCDD2', '#FF1744', '#D32F2F', '#C2185B',
                                              '#7B1FA2', '#303F9F', '#0288D1', '#00796B',
                                              '#689F38', '#F57C00', '#FF5252'])

# Adding labels and title
plt.xlabel('Attendance')
plt.ylabel('Day of the Month')
plt.title('Daily Attendance for Event Y - October 2023', pad=20)

# Show the plot
plt.show()