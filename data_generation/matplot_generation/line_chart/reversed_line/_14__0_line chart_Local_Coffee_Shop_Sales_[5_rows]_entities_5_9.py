
import matplotlib.pyplot as plt

# Data points
years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020
]
enrollment = [
    1000, 1050, 1100, 1200, 1300, 1150,
    1250, 1400, 1350, 1450, 1500, 1550,
    1600, 1700, 1750, 1800, 1850, 1900,
    1950, 2000, 2050
]

# Plot
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.plot(years, enrollment, marker='o', color="#1E90FF")  # Modify color scheme and add markers

# Annotations
for year, enroll in zip(years, enrollment):
    plt.text(year, enroll + 50, f'{enroll}', ha='center', color='#32CD32')  # Assign annotations for each data point

# Change the topic and labels to fit the topic of "Annual Enrollment in Higher Education"
plt.title("Annual Enrollment in Higher Education Over the Years")  # Modify headline
plt.xlabel("Year")                             # Specify the x-axis label
plt.ylabel("Enrollment")                       # Specify the y-axis label

plt.gca().invert_yaxis()  # Invert y-axis

# Show the chart
plt.tight_layout()  # Adjusts plot to ensure everything fits without overlap
plt.show()