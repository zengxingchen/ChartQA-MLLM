
import matplotlib.pyplot as plt

# Data
categories = ['Investment Banking', 'Corporate Finance', 'Entrepreneurship', 'Marketing', 'Management', 
              'Human Resources', 'Consulting', 'Accounting', 'Risk Management', 'Other']
percentages = [18.00, 14.00, 12.00, 10.00, 9.00, 8.00, 7.00, 6.00, 5.00, 11.00]
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999', '#dede00']

# Create a pie chart
plt.figure(figsize=(12, 8))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', startangle=140, colors=colors)

# Title
plt.title('Popular Business Sectors in 2023', fontsize=16, y=1.05)

# Display the chart
plt.show()