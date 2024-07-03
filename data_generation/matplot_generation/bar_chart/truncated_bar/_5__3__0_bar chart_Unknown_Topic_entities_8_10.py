
import matplotlib.pyplot as plt

# Data
dates = [
    '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', 
    '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08', 
    '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', 
    '2024-01-13', '2024-01-14', '2024-01-15', '2024-01-16', 
    '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20', 
    '2024-01-21', '2024-01-22', '2024-01-23', '2024-01-24', 
    '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', 
    '2024-01-29', '2024-01-30', '2024-01-31'
]
calories = [
    150, 200, 180, 220, 210, 190, 230, 170, 160, 240, 180, 250, 200, 220, 
    190, 210, 230, 200, 180, 220, 190, 210, 250, 200, 220, 230, 190, 240, 
    200, 210, 230
]

# Plotting the bar chart
plt.figure(figsize=(14, 8))  # changing width and height of the chart
plt.barh(dates, calories, height=0.7, color=[
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E', '#33FFF6', 
    '#8B33FF', '#33FFB2', '#DAFF33', '#FF8333',
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E', '#33FFF6', 
    '#8B33FF', '#33FFB2', '#DAFF33', '#FF8333',
    '#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
    '#57FF33', '#FFDA33', '#FF335E'
])  # change direction and color scheme of bars

# Customizing the plot
plt.xlabel('Calories')
plt.title('Daily Caloric Intake for January 2024')  # changing topic
plt.xlim(140, 260)  # setting truncated y-axis limits

# Show the plot
plt.show()