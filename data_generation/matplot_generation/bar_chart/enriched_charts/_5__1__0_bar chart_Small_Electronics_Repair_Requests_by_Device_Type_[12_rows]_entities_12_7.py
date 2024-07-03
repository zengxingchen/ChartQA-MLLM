
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
study_hours = [4.0, 4.5, 5.0, 3.8, 4.7, 5.3, 5.1, 4.9, 5.2, 4.4, 5.5, 5.0, 4.3, 5.8, 6.0, 6.2, 6.1, 5.6, 5.4, 5.7, 5.3, 5.1, 5.9, 6.1, 6.4, 6.3, 6.0, 5.9, 5.2, 4.8, 4.5]

# Creating the figure and specifying figure size
plt.figure(figsize=(10, 12))

# Creating the bar chart as a horizontal chart
plt.barh(days, study_hours, height=0.6, color=['#FF5733', '#33FF57', '#3357FF', '#F333FF', 
                                              '#33FFF3', '#FF33A8', '#F3FF33', '#333FFF',
                                              '#57FF33', '#5733FF', '#F333FF', '#33FF57',
                                              '#33FFF3', '#FF33A8', '#57FF33', '#5733FF',
                                              '#F333FF', '#33FF57', '#33FFF3', '#FF33A8',
                                              '#57FF33', '#5733FF', '#F333FF', '#33FF57',
                                              '#33FFF3', '#FF33A8', '#57FF33', '#5733FF',
                                              '#F333FF', '#33FF57', '#33FFF3'])

# Adding labels and title
plt.xlabel('Average Daily Study Hours')
plt.ylabel('Day of the Month')
plt.title('Average Daily Study Hours for Students - October 2023', pad=20)

# Setting y-axis limits
plt.ylim(2.5, 7)

# Show the plot
plt.show()