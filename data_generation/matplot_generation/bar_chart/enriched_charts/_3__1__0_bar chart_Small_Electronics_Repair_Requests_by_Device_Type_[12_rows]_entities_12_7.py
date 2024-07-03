
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 31)]
calories = [150, 200, 180, 220, 160, 210, 230, 190, 170, 200, 250, 240, 260, 270, 180, 220, 190, 200, 210, 230, 180, 220, 200, 210, 230, 240, 250, 260, 220, 210]

# Creating the figure and specifying figure size
plt.figure(figsize=(12, 6))

# Creating the bar chart as a horizontal chart
plt.barh(days, calories, height=0.4, color=['#4B0082', '#A52A2A', '#7FFF00', '#D2691E', '#FF7F50',
                                            '#6495ED', '#DC143C', '#00FFFF', '#00008B', '#008B8B',
                                            '#B8860B', '#A9A9A9', '#006400', '#BDB76B', '#8B008B',
                                            '#556B2F', '#FF8C00', '#9932CC', '#8B0000', '#E9967A',
                                            '#8FBC8F', '#483D8B', '#2F4F4F', '#00CED1', '#9400D3',
                                            '#FF1493', '#00BFFF', '#696969', '#1E90FF', '#B22222'])

# Adding labels and title
plt.xlabel('Calories Burned')
plt.ylabel('Day of the Month')
plt.title('Calories Burned Daily - June 2024')

# Show the plot
plt.show()