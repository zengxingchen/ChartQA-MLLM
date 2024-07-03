
import matplotlib.pyplot as plt

# Data to plot
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
steps = [7500, 7800, 8200, 8500, 9000, 9200, 9400, 9600, 8900, 8700, 8300, 8000]

# Plot a vertical bar chart
plt.figure(figsize=(12, 6))  # Width and height of the chart
plt.bar(x=months, height=steps, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e'], 
    width=0.5)  # Band width of the bars

# Set the title and labels
plt.title('Average Daily Steps Taken Each Month', fontsize=16)
plt.ylabel('Steps', fontsize=12)
plt.xlabel('Month', fontsize=12)

# Display the chart
plt.tight_layout()  # Adjust the padding between and around subplots.
plt.show()