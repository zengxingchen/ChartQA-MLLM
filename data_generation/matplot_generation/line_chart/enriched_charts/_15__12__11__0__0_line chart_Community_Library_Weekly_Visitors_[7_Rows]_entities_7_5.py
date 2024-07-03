
import matplotlib.pyplot as plt

# Define the data points
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
happiness_index = [7.2, 7.4, 7.3, 7.5, 7.6, 7.7, 7.6, 7.8, 7.7, 7.9, 7.1, 7.2, 7.4]

# Create the line chart
plt.figure(figsize=(14, 8))
plt.plot(years, happiness_index, color='#1E90FF', marker='o')

# Customize the trend of the data by simulating a drop in 2020
happiness_index[10] = 7.1
plt.plot(years, happiness_index, linestyle='--', color='#FF6347')

# Assign annotation to the chart
for i, hi in enumerate(happiness_index):
    plt.annotate(f"{hi}", (years[i], happiness_index[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Happiness Index Over Years (2010-2022)', pad=30)
plt.xlabel('Year')
plt.ylabel('Happiness Index')
plt.gca().invert_yaxis()
plt.grid(True)

# Display the plot
plt.show()