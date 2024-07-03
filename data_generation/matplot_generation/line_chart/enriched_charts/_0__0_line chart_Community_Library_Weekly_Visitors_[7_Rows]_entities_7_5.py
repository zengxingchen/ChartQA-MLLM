
import matplotlib.pyplot as plt

# Define the data points
years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
funding = [0.8, 1.2, 1.8, 2.4, 3.2, 4.1, 5.0, 4.5, 6.3, 7.2, 8.1, 9.5, 11.0]

# Create the line chart
plt.figure(figsize=(12, 6)) # Changed width and height of the chart
plt.plot(years, funding, color='#2E8B57', marker='s') # Changed color scheme and added markers

# Customize the trend of the data by simulating a dip in 2017
funding[7] = 4.5
plt.plot(years, funding, linestyle='--', color='#DC143C') # Overlaying the modified trend line

# Assign annotation to the chart
for i, fund in enumerate(funding):
    plt.annotate(f"${fund}B", (years[i], funding[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Axes and title
plt.title('Venture Capital Funding in Tech Startups (2010-2022)', pad=20)
plt.xlabel('Year')
plt.ylabel('Funding (in billions)')
plt.grid(True)

# Display the plot
plt.show()