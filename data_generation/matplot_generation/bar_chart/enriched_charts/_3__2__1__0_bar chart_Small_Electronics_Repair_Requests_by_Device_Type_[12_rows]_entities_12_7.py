
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
book_sales = [200, 180, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 
              340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490]

# Creating the figure and specifying figure size
plt.figure(figsize=(14, 8))

# Creating the bar chart as a vertical chart
plt.bar(days, book_sales, width=0.6, color=['#1E88E5', '#D32F2F', '#7B1FA2', '#FBC02D',
                                            '#388E3C', '#F57C00', '#0288D1', '#C2185B',
                                            '#8E24AA', '#FDD835', '#43A047', '#FB8C00',
                                            '#1976D2', '#D81B60', '#AB47BC', '#FFEB3B',
                                            '#4CAF50', '#FFA726', '#039BE5', '#E91E63',
                                            '#BA68C8', '#FFEE58', '#66BB6A', '#FF7043',
                                            '#0288D1', '#AD1457', '#8E24AA', '#FFEB3B',
                                            '#4CAF50', '#FB8C00', '#039BE5'])

# Adding labels and title
plt.xlabel('Day of the Month')
plt.ylabel('Book Sales')
plt.title('Daily Book Sales - October 2023', pad=20)

# Show the plot
plt.show()