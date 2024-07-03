
import matplotlib.pyplot as plt

# Data points
age_groups = ['Infants (4-12 months)', 'Toddlers (1-2 years)', 'Preschoolers (3-5 years)',
              'School-age Children (6-13 years)', 'Teenagers (14-17 years)', 'Young Adults (18-25 years)',
              'Adults (26-64 years)', 'Older Adults (65+ years)']
average_sleep = [14, 13, 12, 10, 9, 8, 7, 7]

# Colors for each point
colors = ['#FF4500', '#FF8C00', '#FFD700', '#ADFF2F', '#7CFC00', 
          '#00FA9A', '#00CED1', '#1E90FF']

# Change width and height of the chart
plt.figure(figsize=(12, 8))

# Scatter plot
plt.scatter(age_groups, average_sleep, c=colors)

# Title and labels
plt.title('Average Hours of Sleep by Age Group', pad=20)
plt.xlabel('Age Group')
plt.ylabel('Average Hours of Sleep')

# Adjust x-axis to show each age group
plt.xticks(age_groups, rotation=45, ha='right')

# Show plot
plt.tight_layout()
plt.show()