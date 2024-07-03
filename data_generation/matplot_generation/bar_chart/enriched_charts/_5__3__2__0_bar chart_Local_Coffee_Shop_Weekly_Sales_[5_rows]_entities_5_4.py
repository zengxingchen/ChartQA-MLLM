
import matplotlib.pyplot as plt

# Data
countries = [
    'China', 'United States', 'India', 'Russia', 'Japan', 'Germany', 'Iran',
    'South Korea', 'Saudi Arabia', 'Indonesia', 'Canada', 'Mexico', 'Brazil',
    'South Africa', 'Australia', 'Turkey', 'Italy', 'France', 'Thailand', 'Poland'
]
co2_emissions = [
    10165, 5290, 2580, 1605, 1230, 725, 645, 610, 590, 550, 530, 510, 480,
    460, 420, 400, 380, 360, 350, 340
]

# Color scheme using specific color codes
colors = [
    '#FF5733', '#33FF57', '#3357FF', '#F7DC6F', '#BB8FCE', '#76D7C4', '#F1948A', 
    '#F5B7B1', '#A9DFBF', '#AED6F1', '#F9E79F', '#D7BDE2', '#85C1E9', '#FAD7A0', 
    '#EDBB99', '#9B59B6', '#1ABC9C', '#2980B9', '#C0392B', '#7F8C8D'
]

# Create vertical bar chart
plt.figure(figsize=(16, 10))
bars = plt.bar(countries, co2_emissions, color=colors, width=0.5)

# Adjusting the width of bars
for bar in bars:
    bar.set_width(0.4)

# Changing the layout and labels
plt.ylabel('Annual CO2 Emissions (in Million Metric Tons)', fontsize=12)
plt.title('Annual CO2 Emissions by Country (2024)', fontsize=16, pad=20)
plt.ylim(300, max(co2_emissions) * 1.1)  # Set y-axis limit to start from 300

# Adding value labels to the top of each bar
for i, v in enumerate(co2_emissions):
    plt.text(i, v + 100, str(v), color='black', ha='center', fontsize=11)

# Show the final result
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()