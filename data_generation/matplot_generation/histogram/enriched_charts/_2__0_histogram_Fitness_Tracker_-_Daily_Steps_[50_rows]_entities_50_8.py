import matplotlib.pyplot as plt

# Data: salaries of employees in a company
salaries = [
    35, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670, 690, 710, 730, 750, 770, 790, 810, 830, 850, 870, 890, 910, 930, 950, 970, 990, 1010, 1030, 1050, 1070, 1090, 1110, 1130, 1150, 1170, 1190, 1210, 1230, 1250, 1270, 1290, 1310, 1330, 1350, 1370, 1390, 1410, 1430, 1450, 1470, 1490, 1510, 1530, 1550, 1570, 1590, 1610, 1630, 1650, 1670, 1690, 1710, 1730, 1750, 1770, 1790, 1810, 1830, 1850, 1870, 1890, 1910, 1930, 1950, 1970, 1990
]

# Set the size of the histogram
plt.figure(figsize=(12, 8))

# Create a histogram with vertical orientation, modify colors and change bandwidth
plt.hist(salaries, bins=20, orientation='vertical', color='#4b0082', rwidth=0.8)

# Add title and labels to xaxis and yaxis
plt.title('Salary Distribution in a Company')
plt.xlabel('Salary (in thousands)')
plt.ylabel('Number of Employees')

# Show the plot
plt.show()