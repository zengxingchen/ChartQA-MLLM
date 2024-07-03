
import matplotlib.pyplot as plt

# Data
landmarks = ['Landmark 1', 'Landmark 2', 'Landmark 3', 'Landmark 4', 'Landmark 5', 'Landmark 6', 
             'Landmark 7', 'Landmark 8', 'Landmark 9', 'Landmark 10', 'Landmark 11', 'Landmark 12', 
             'Landmark 13', 'Landmark 14', 'Landmark 15', 'Landmark 16', 'Landmark 17', 'Landmark 18', 
             'Landmark 19', 'Landmark 20', 'Landmark 21', 'Landmark 22', 'Landmark 23', 'Landmark 24', 
             'Landmark 25', 'Landmark 26', 'Landmark 27', 'Landmark 28', 'Landmark 29', 'Landmark 30', 
             'Landmark 31']
visitors = [1600, 1650, 1700, 1620, 1750, 1800, 1830, 1780, 1690, 1760, 1810, 1770, 1640, 1880, 1900, 
            1950, 2000, 1980, 1850, 1790, 1820, 1860, 1920, 1970, 2010, 2030, 2050, 2080, 1910, 1870, 1790]

# Creating the figure and specifying figure size
plt.figure(figsize=(12, 8))

# Creating the bar chart as a vertical chart
plt.bar(landmarks, visitors, width=0.5, color=['#4B0082', '#8B0000', '#FF8C00', '#ADFF2F', 
                                                '#00CED1', '#9400D3', '#DAA520', '#8B008B', 
                                                '#00008B', '#DC143C', '#00BFFF', '#32CD32', 
                                                '#FF4500', '#2E8B57', '#8B4513', '#FF1493', 
                                                '#1E90FF', '#FFD700', '#ADFF2F', '#FF6347', 
                                                '#4682B4', '#D2691E', '#7FFF00', '#B22222', 
                                                '#87CEEB', '#FF69B4', '#FF00FF', '#8A2BE2', 
                                                '#7B68EE', '#6A5ACD', '#48D1CC'])

# Adding labels and title
plt.xlabel('Landmark')
plt.ylabel('Number of Visitors')
plt.title('Number of Tourists Visiting Different Landmarks - October 2023', pad=20)

# Setting y-axis limits
plt.ylim(1500, 2100)

# Rotate the x labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()