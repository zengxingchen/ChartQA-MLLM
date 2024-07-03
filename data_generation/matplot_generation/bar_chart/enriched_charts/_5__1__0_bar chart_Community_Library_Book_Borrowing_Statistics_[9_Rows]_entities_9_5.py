
import matplotlib.pyplot as plt

# Data
activities = ['Marketing', 'Product Development', 'Customer Support', 'Sales', 'HR Management', 
              'Financial Planning', 'IT Support', 'Logistics', 'Administration', 'Research', 
              'Compliance', 'Public Relations']
hours = [35, 50, 25, 45, 20, 40, 30, 15, 25, 55, 30, 20]

# Create horizontal bar chart
plt.figure(figsize=(12, 8))  # Width, Height of the chart
plt.barh(activities, hours, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8C33', 
                                   '#33FFD4', '#7D33FF', '#FF3333', '#3380FF', '#33FF73', 
                                   '#FF33FB', '#33FFAE'], 
         height=0.7)  # Height of the bars

# Set the title and labels
plt.title('Monthly Business Activities Hours', fontsize=16)
plt.xlabel('Hours per Month', fontsize=12)
plt.ylabel('Activity', fontsize=12)

# Set y-axis limits to truncate the view
plt.xlim(10, 60)

# Show the plot
plt.show()