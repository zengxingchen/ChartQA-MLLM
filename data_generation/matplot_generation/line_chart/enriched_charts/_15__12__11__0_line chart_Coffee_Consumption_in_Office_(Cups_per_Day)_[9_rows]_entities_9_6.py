
import matplotlib.pyplot as plt

years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
happiness_index = [7.5, 7.2, 7.8, 7.3, 7.0, 6.8, 7.4, 7.1, 6.9, 7.2, 7.5, 7.3]

plt.figure(figsize=(12, 8))  # Adjust width and height of the chart
plt.plot(years, happiness_index, marker='s', linestyle='-', color='#FF6347')  # Specific hex color

# Annotation for the lowest happiness index
plt.annotate('Lowest Happiness', xy=('2024', 6.8), xytext=('2025', 6.5),
             arrowprops=dict(facecolor='#32CD32', shrink=0.05))

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Happiness Index')
plt.title('Happiness Index Over a Decade in Society', pad=30)  # Added padding to avoid overlap

plt.gca().invert_yaxis()  # Inverting the y-axis

# Showing the plot
plt.show()