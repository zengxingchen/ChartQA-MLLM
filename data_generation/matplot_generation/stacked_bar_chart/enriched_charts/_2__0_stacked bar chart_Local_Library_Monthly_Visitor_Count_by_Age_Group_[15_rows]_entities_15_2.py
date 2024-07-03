
import matplotlib.pyplot as plt

# Data
countries = ['Australia', 'Brazil', 'Canada', 'France', 'Japan', 'South Africa']
adventure_sports = [180, 160, 140, 170, 190, 150]
beach_holidays = [220, 230, 210, 200, 180, 190]
cultural_trips = [140, 120, 150, 130, 160, 170]

# Color codes for each type of trip
colors = ['#4daf4a', '#377eb8', '#ff7f00']

# Plot stacked vertical bar chart
plt.figure(figsize=(12, 6)) # Width and height of the chart in inches
bar_width = 0.5 # Width of the bars

plt.bar(countries, adventure_sports, color=colors[0], edgecolor='white', width=bar_width, label='Adventure Sports')
plt.bar(countries, beach_holidays, bottom=adventure_sports, color=colors[1], edgecolor='white', width=bar_width, label='Beach Holidays')
plt.bar(countries, cultural_trips, bottom=[i+j for i,j in zip(adventure_sports, beach_holidays)], color=colors[2], edgecolor='white', width=bar_width, label='Cultural Trips')

# Add numerical labels
for i in range(len(countries)):
    plt.text(i, adventure_sports[i] / 2, str(adventure_sports[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, adventure_sports[i] + beach_holidays[i] / 2, str(beach_holidays[i]), ha='center', va='center', color='white', fontweight='bold')
    plt.text(i, adventure_sports[i] + beach_holidays[i] + cultural_trips[i] / 2, str(cultural_trips[i]), ha='center', va='center', color='white', fontweight='bold')

# Add labels and title
plt.ylabel('Number of Trips')
plt.xlabel('Country')
plt.title('Popularity of Different Types of Trips by Country')
plt.legend()

# Display the final result
plt.show()