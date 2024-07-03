
import matplotlib.pyplot as plt

# Table data represented as lists
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
astronomy = [3000, 3500, 4000, 4500, 4800, 5000, 5300, 5600, 5800, 6000, 6200, 6400]
physics = [3500, 4000, 4200, 4500, 4700, 4900, 5200, 5400, 5700, 5900, 6100, 6300]
chemistry = [2500, 2800, 3000, 3300, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000]
biology = [2000, 2300, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400]

# Create a stacked area chart
plt.figure(figsize=(14, 7))  # Change width and height of the chart
plt.stackplot(months, astronomy, physics, chemistry, biology, 
              colors=['#FF4500', '#32CD32', '#1E90FF', '#FFD700'])  # Modify the color scheme

# Add title and labels
plt.title('Monthly Research Paper Publications by Field', fontdict={'fontsize': 15}, loc='left')
plt.xlabel('Month')
plt.ylabel('Number of Papers')

# Assign annotation/text label on the chart for the peak of Astronomy
peak_papers_month = months[astronomy.index(max(astronomy))]
peak_papers_value = max(astronomy)
plt.text(peak_papers_month, peak_papers_value, 'Peak for Astronomy', ha='center', va='top')

# Display the chart
plt.show()