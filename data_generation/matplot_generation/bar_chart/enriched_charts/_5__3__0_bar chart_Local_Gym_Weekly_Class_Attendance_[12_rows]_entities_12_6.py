
import matplotlib.pyplot as plt

# Data
countries = ['Japan', 'Switzerland', 'Singapore', 'Italy', 'Spain', 
             'Australia', 'Iceland', 'Israel', 'Sweden', 'France', 
             'South Korea', 'Norway', 'Luxembourg', 'Finland', 
             'Canada', 'Netherlands', 'New Zealand', 'Ireland', 
             'Belgium', 'Austria']
study_hours = [30.5, 28.4, 33.1, 27.3, 25.9, 
               26.7, 22.8, 29.6, 24.5, 23.7, 
               34.0, 21.9, 20.5, 22.3, 
               26.1, 24.2, 25.0, 23.3, 
               22.0, 21.5]

# Create horizontal bar chart
plt.figure(figsize=(14, 10))  # Change width and height of the chart
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#33FFA1', 
          '#FF8C33', '#337BFF', '#FF5733', '#33FF57', '#3357FF', 
          '#FF33A1', '#33FFA1', '#FF8C33', '#337BFF', 
          '#FF5733', '#33FF57', '#3357FF', '#FF33A1', 
          '#33FFA1', '#FF8C33']

plt.barh(countries, study_hours, color=colors, height=0.6)  # Change direction of chart and bar width

# Customizing the plot
plt.xlabel('Average Study Hours per Week')
plt.title('Average Study Hours per Week by Country (2020)', pad=20)
plt.xlim(20, 35)  # Set y-axis limits to truncate the chart
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()