
import matplotlib.pyplot as plt

# Data
countries = ['United States', 'China', 'Japan', 'Germany', 'India', 
             'United Kingdom', 'France', 'Brazil', 'Italy', 'Canada', 
             'Russia', 'South Korea', 'Spain', 'Australia', 'Mexico']
daily_steps = [4.7, 6.5, 7.1, 5.8, 6.0, 5.9, 6.3, 5.1, 6.2, 5.5, 
               5.6, 7.2, 6.1, 5.7, 4.8]  # in thousands
hours_sleep = [6.8, 7.2, 7.6, 7.0, 6.5, 6.9, 7.4, 6.8, 7.3, 7.1, 
               6.7, 7.5, 7.4, 6.9, 6.5]  # in hours
bmi = [29.1, 23.7, 22.5, 26.3, 23.0, 27.5, 24.1, 27.9, 25.3, 26.5, 
       27.8, 23.5, 24.9, 26.7, 28.6]  # Body Mass Index

# Color for each country
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FF8333', 
          '#33FFF5', '#FF5733', '#5733FF', '#33FF57', '#5733FF', 
          '#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFF5']

# Using BMI as the size of the bubble
sizes = [b / max(bmi) * 2000 for b in bmi]

# Set up the figure size
plt.figure(figsize=(16, 12))

# Scatter plot
plt.scatter(daily_steps, hours_sleep, s=sizes, c=colors, alpha=0.6)

# Labels and Title
plt.title('Health Metrics: Daily Steps, Sleep, and BMI by Country', fontsize=18)
plt.xlabel('Daily Steps (thousands)', fontsize=14)
plt.ylabel('Hours of Sleep', fontsize=14)

# Add country names to the bubbles
for i, country in enumerate(countries):
    plt.annotate(country, (daily_steps[i], hours_sleep[i]), fontsize=10)

# Show grid
plt.grid(True)

# Show the plot
plt.show()