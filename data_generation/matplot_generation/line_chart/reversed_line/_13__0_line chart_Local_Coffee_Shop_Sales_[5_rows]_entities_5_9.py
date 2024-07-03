
import matplotlib.pyplot as plt

# Data points
years = [
    2000, 2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010, 2011,
    2012, 2013, 2014, 2015, 2016, 2017,
    2018, 2019, 2020
]
health_spending = [
    5.1, 5.3, 5.6, 5.9, 6.2, 6.5,
    6.7, 6.9, 7.2, 7.5, 7.8, 8.0,
    8.3, 8.5, 8.7, 8.9, 9.2, 9.4,
    9.6, 9.9, 10.1
]

# Plot
plt.figure(figsize=(12, 8))  # Change width and height of the chart
plt.plot(years, health_spending, marker='o', color="#4682B4")  # Modify color scheme and add markers

# Annotations
for year, spend in zip(years, health_spending):
    plt.text(year, spend + 0.1, f'{spend:.1f}', ha='center', color='#800080')  # Assign annotations for each data point

# Change the topic and labels to fit the topic of "Health Spending"
plt.title("Health Spending Over the Years", fontsize=14)  # Modify headline
plt.xlabel("Year", fontsize=12)  # Specify the x-axis label
plt.ylabel("Spending (% of GDP)", fontsize=12)  # Specify the y-axis label

# Show the chart
plt.tight_layout()  # Adjusts plot to ensure everything fits without overlap
plt.gca().invert_yaxis()  # Invert the y-axis
plt.show()