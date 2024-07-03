
import matplotlib.pyplot as plt

# Data
age_groups = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80+']
avg_water_intake = [1.2, 1.5, 2.1, 2.4, 2.0, 1.8, 1.7, 1.6, 1.5]
number_of_participants = [190000, 230000, 210000, 190000, 170000, 150000, 130000, 110000, 90000]

# Custom colors
colors = ['#ff4500', '#32cd32', '#1e90ff', '#ff69b4', '#8a2be2', '#ffd700', '#00ced1', '#ff6347', '#4682b4']

# Set figure size
plt.figure(figsize=(18, 12))

# Scatter plot with bubble sizes
bubble_sizes = [n / 1000 for n in number_of_participants]  # Scaling the number of participants for bubble size
plt.scatter(age_groups, avg_water_intake, s=bubble_sizes, c=colors, alpha=0.6)

# Labels and title
plt.xlabel('Age Group')
plt.ylabel('Average Daily Water Intake (liters)')
plt.title('Average Daily Water Intake by Age Group', pad=20)

# Show plot
plt.show()