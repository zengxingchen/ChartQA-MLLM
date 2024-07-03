
import matplotlib.pyplot as plt

# Data
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
average_sleep = [10.5, 9.2, 7.5, 7.0, 6.8, 6.5, 6.7, 6.8, 7.0]
number_of_participants = [180000, 220000, 200000, 180000, 160000, 140000, 120000, 100000, 80000]

# Custom colors
colors = ['#ff6347', '#4682b4', '#8a2be2', '#deb887', '#5f9ea0', '#7fff00', '#d2691e', '#ff7f50', '#6495ed']

# Set figure size
plt.figure(figsize=(16, 10))

# Scatter plot with bubble sizes
bubble_sizes = [n / 1000 for n in number_of_participants]  # Scaling the number of participants for bubble size
plt.scatter(age_groups, average_sleep, s=bubble_sizes, c=colors, alpha=0.6)

# Labels and title
plt.xlabel('Age Group')
plt.ylabel('Average Daily Sleep (hours)')
plt.title('Average Daily Sleep Hours by Age Group', pad=20)

# Show plot
plt.show()