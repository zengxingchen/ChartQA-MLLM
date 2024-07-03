
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
visitors = [1234, 1432, 1560, 1670, 1723, 1901, 1820, 1745, 1634, 1502, 1403, 1300, 1250, 1354, 1456, 1578, 1689, 1790, 1895, 1900, 1850, 1789, 1698, 1604, 1550, 1500, 1589, 1645, 1701, 1789, 1823]

# Creating the figure and specifying figure size
plt.figure(figsize=(14, 8))

# Creating the bar chart as a vertical chart
plt.bar(days, visitors, width=0.6, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c2f0c2', '#ffccf2', '#ffd699', '#ffb3b3', '#d9b3ff', '#ffeb99', '#66e0ff', '#99ffcc', '#cc99ff', '#ffccff', '#c2e0c2', '#ff99e6', '#ccff99', '#ffb366', '#b3ffb3', '#f2ccff', '#d9b3ff', '#99e6ff', '#ff99cc', '#ffcc99', '#c2f0f0', '#e6b3ff', '#66ffcc', '#ff99ff', '#ff99ff'])

# Adding labels and title
plt.xlabel('Day of the Month')
plt.ylabel('Number of Visitors')
plt.title('Daily Visitors to Museum X - May 2023')

# Show the plot
plt.show()