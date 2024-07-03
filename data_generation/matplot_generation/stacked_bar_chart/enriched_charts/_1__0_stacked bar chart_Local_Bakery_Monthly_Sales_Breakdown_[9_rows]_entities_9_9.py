
import matplotlib.pyplot as plt

# Data
years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
country_a_co2 = [400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600]
country_b_co2 = [350, 365, 380, 395, 410, 425, 440, 455, 470, 485, 500]

# Colors
colors_a = ['#FF5733', '#FFC300', '#FF5733', '#FFC300', '#FF5733', '#FFC300', '#FF5733', '#FFC300', '#FF5733', '#FFC300', '#FF5733']
colors_b = ['#1F618D', '#34495E', '#1F618D', '#34495E', '#1F618D', '#34495E', '#1F618D', '#34495E', '#1F618D', '#34495E', '#1F618D']

# Plot
fig, ax = plt.subplots(figsize=(12, 10))  # Change width and height of the chart

bar_width = 0.6  # Change band width for bars

# Creating a vertical stacked bar chart
bars_a = plt.bar(years, country_a_co2, color=colors_a, edgecolor='white', width=bar_width)
bars_b = plt.bar(years, country_b_co2, bottom=country_a_co2, color=colors_b, edgecolor='white', width=bar_width)

# Adding labels and title
plt.ylabel('CO2 Emissions (Million Metric Tons)')
plt.title('Annual CO2 Emissions Comparison between Country A and Country B', pad=20)

# Customizing the axes
plt.ylim(0, 1200)  # Adjust the y-axis limit to accommodate the stack

# Display the plot
plt.show()