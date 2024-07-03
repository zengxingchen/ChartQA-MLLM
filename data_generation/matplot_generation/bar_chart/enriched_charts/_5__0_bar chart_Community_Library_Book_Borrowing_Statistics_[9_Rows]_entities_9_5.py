
import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [500, 450, 470, 480, 510, 530, 520, 505, 490, 515, 495, 500]

# Create vertical bar chart
plt.figure(figsize=(10, 6))  # Width, Height of the chart
plt.bar(months, sales, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFC300', '#DAF7A6', 
                              '#C70039', '#900C3F', '#581845', '#FF5733', '#33FF57', '#3357FF'], 
        width=0.6)  # Width of the bars

# Set the title and labels
plt.title('Monthly Gym Membership Sales')
plt.xlabel('Month')
plt.ylabel('Membership Sales in USD')

# Set y-axis limits to truncate the lower part
plt.ylim(400, 550)

# Show the plot
plt.show()