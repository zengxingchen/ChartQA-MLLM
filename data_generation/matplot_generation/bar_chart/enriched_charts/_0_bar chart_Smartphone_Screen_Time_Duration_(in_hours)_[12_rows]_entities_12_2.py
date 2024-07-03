
import matplotlib.pyplot as plt

# Data to plot
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
sales = [200, 240, 260, 300, 320, 360, 410, 440, 390, 420, 450, 470]

# Plot a horizontal bar chart
plt.figure(figsize=(8, 10))  # Width and height of the chart
plt.barh(y=months, width=sales, color=[
    '#FF5733', '#C70039', '#900C3F', '#581845', 
    '#DAF7A6', '#FFC300', '#FF5733', '#C70039', 
    '#900C3F', '#581845', '#DAF7A6', '#FFC300'], 
    height=0.6)  # Band height of the bars

# Set the title and labels
plt.title('Monthly Sales Data for the Year', fontsize=16)
plt.xlabel('Sales (in units)', fontsize=12)
plt.ylabel('Month', fontsize=12)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()