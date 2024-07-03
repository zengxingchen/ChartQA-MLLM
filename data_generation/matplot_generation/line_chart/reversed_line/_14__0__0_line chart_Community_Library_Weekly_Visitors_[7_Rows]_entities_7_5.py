
import matplotlib.pyplot as plt

# Define the data points
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
revenue = [20.5, 21.7, 23.1, 25.0, 24.0, 23.8, 22.7, 22.9, 24.2, 25.5, 27.1, 29.3, 30.7]

# Create the line chart
plt.figure(figsize=(14, 8))  # Changed width and height of the chart
plt.plot(years, revenue, color='#4682B4', marker='o')  # Changed color scheme and added markers

# Customize the trend of the data by simulating a dip in 2016
revenue[6] = 22.7
plt.plot(years, revenue, linestyle='--', color='#FF4500')  # Overlaying the modified trend line

# Assign annotation to the chart
for i, rev in enumerate(revenue):
    plt.annotate(f"${rev}M", (years[i], revenue[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Annual Revenue in Music Industry (2010-2022)', pad=20)
plt.xlabel('Year')
plt.ylabel('Revenue (in millions)')
plt.grid(True)

# Invert y-axis
plt.gca().invert_yaxis()

# Display the plot
plt.show()