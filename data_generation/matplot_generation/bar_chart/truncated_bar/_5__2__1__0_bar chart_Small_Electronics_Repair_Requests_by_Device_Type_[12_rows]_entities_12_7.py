
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 32)]
page_views = [350, 380, 420, 450, 480, 500, 520, 530, 540, 560, 580, 600, 610, 620, 630, 
              640, 650, 670, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920]

# Creating the figure and specifying figure size
plt.figure(figsize=(14, 8))

# Creating the bar chart
plt.bar(days, page_views, width=0.7, color=['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFA8', 
                                             '#A833FF', '#FF8D33', '#33A8FF', '#A8FF33', '#FF3333', 
                                             '#33FFBD', '#FF3333', '#33FFBD', '#A833FF', '#FF8D33', 
                                             '#33A8FF', '#A8FF33', '#FF3333', '#33FFBD', '#FF5733', 
                                             '#33FF57', '#3357FF', '#FF33A8', '#33FFA8', '#A833FF', 
                                             '#FF8D33', '#33A8FF', '#A8FF33', '#FF3333', '#33FFBD', 
                                             '#FF3333'])

# Adding labels and title
plt.ylabel('Page Views')
plt.xlabel('Day of the Month')
plt.title('Daily Page Views for Blog - January 2024', pad=20)

# Setting y-axis limits to truncate
plt.ylim(300, 950)

# Show the plot
plt.show()