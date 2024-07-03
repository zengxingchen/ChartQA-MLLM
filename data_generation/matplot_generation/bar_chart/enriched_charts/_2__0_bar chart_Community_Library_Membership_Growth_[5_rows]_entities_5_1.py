
import matplotlib.pyplot as plt

# Data from the table above
countries = [
    'United States', 'Germany', 'United Kingdom', 'France', 'Italy', 
    'Spain', 'Greece', 'Brazil', 'India', 'China', 'Japan', 
    'South Korea', 'Australia', 'Canada', 'Russia', 'Turkey'
]

average_daily_calories = [
    3770, 3490, 3410, 3480, 3360, 3300, 3520, 3010, 2450, 3050, 
    2680, 2900, 3510, 3670, 3200, 3250
]

# Modify the color scheme, width of bars, and size of the chart
colors = [
    '#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6', 
    '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', 
    '#DAF7A6', '#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845'
]

# Set the figure size for better clarity or visual appeal
plt.figure(figsize=(16, 10))

# Change the direction of the chart from horizontal to vertical
plt.bar(countries, average_daily_calories, color=colors, width=0.4)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add labels and title to the chart
plt.ylabel('Average Daily Calorie Intake')
plt.title('Average Daily Calorie Intake by Country')

# Display the chart
plt.tight_layout()  # Adjust layout to fit all labels and title
plt.show()