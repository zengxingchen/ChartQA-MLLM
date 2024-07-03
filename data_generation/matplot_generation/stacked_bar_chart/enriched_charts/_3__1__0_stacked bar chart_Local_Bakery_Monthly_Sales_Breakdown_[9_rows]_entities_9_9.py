
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
country_a_co2 = [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700]
country_b_co2 = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]

# Colors
colors_a = ['#FF6347', '#FFD700', '#FF6347', '#FFD700', '#FF6347', '#FFD700', '#FF6347', '#FFD700', '#FF6347', '#FFD700', '#FF6347']
colors_b = ['#4682B4', '#708090', '#4682B4', '#708090', '#4682B4', '#708090', '#4682B4', '#708090', '#4682B4', '#708090', '#4682B4']

# Plot
fig, ax = plt.subplots(figsize=(10, 12))  # Change width and height of the chart

bar_height = 0.6  # Change band height for bars

# Creating a horizontal stacked bar chart
bars_a = plt.barh(years, country_a_co2, color=colors_a, edgecolor='white', height=bar_height)
bars_b = plt.barh(years, country_b_co2, left=country_a_co2, color=colors_b, edgecolor='white', height=bar_height)

# Adding labels and title
plt.xlabel('CO2 Emissions (Million Metric Tons)')
plt.title('Annual CO2 Emissions Comparison between Country A and Country B', pad=20)

# Adding numerical labels
for bar in bars_a:
    width = bar.get_width()
    plt.text(width - 40, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='center', va='center', color='white')
for bar in bars_b:
    width = bar.get_width() + bar.get_x()
    plt.text(width - 40, bar.get_y() + bar.get_height() / 2, f'{int(width)}', ha='center', va='center', color='white')

# Customizing the axes
plt.xlim(0, 1400)  # Adjust the x-axis limit to accommodate the stack

# Display the plot
plt.show()