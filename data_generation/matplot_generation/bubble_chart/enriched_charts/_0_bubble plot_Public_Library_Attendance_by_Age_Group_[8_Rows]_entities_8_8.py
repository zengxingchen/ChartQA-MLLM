
import matplotlib.pyplot as plt

# Hypothetical data representing average daily hours of internet usage by age group
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
internet_usage = [1, 3, 4, 3.5, 3, 2.5, 2, 1.5, 1]
number_of_users = [100000, 300000, 500000, 400000, 350000, 300000, 200000, 100000, 50000]

# Custom color for each age group
colors = ['#FF6347', '#FFD700', '#90EE90', '#ADD8E6', '#C71585', '#FFB6C1', '#20B2AA', '#778899', '#B0C4DE']

# Set the figure size
plt.figure(figsize=(12, 8))

# Scatter plot with bubble sizes
bubble_sizes = [n / 1000 for n in number_of_users]  # Scaling the number of users for bubble size
plt.scatter(age_groups, internet_usage, s=bubble_sizes, c=colors, alpha=0.5)

# Labels and title
plt.xlabel('Age Group')
plt.ylabel('Average Daily Internet Usage (hours)')
plt.title('Average Daily Internet Usage by Age Group in a Hypothetical Country')

# Show plot
plt.show()