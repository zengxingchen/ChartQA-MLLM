
import matplotlib.pyplot as plt

# Data for the stacked area chart
months = ['Jan-2021', 'Feb-2021', 'Mar-2021', 'Apr-2021', 'May-2021', 'Jun-2021', 
          'Jul-2021', 'Aug-2021', 'Sep-2021', 'Oct-2021', 'Nov-2021', 'Dec-2021',
          'Jan-2022', 'Feb-2022', 'Mar-2022', 'Apr-2022', 'May-2022', 'Jun-2022',
          'Jul-2022', 'Aug-2022', 'Sep-2022', 'Oct-2022', 'Nov-2022', 'Dec-2022']
physical_activity = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105,
                     110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165]
healthy_eating = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 
                  100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155]
mental_wellbeing = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 
                    90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

# Modify the dimensions of the plot
plt.figure(figsize=(12, 8))

# Creating the stacked area chart
plt.stackplot(months, physical_activity, healthy_eating, mental_wellbeing,
              colors=['#3498db', '#e74c3c', '#2ecc71'],
              labels=['Physical Activity', 'Healthy Eating', 'Mental Wellbeing'])

# Adding the legend
plt.legend(loc='upper left')

# Adding titles and labels
plt.title('Monthly Health and Wellness Activities', pad=20)
plt.xlabel('Month')
plt.ylabel('Activity Count')

# Add annotation
for i, pa in enumerate(physical_activity):
    total_activity = pa + healthy_eating[i] + mental_wellbeing[i]
    plt.text(months[i], total_activity, f'{total_activity}', ha='center', va='bottom')

# Show the plot
plt.tight_layout()
plt.show()