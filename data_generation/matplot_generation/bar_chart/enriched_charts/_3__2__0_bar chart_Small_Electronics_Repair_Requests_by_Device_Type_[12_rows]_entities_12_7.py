
import matplotlib.pyplot as plt

# Data
days = [str(day) for day in range(1, 31)]
participants = [
    100, 120, 110, 130, 150, 160, 170, 180, 190, 200,
    210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
    310, 320, 330, 340, 350, 360, 370, 380, 390, 400
]

# Creating the figure and specifying figure size
plt.figure(figsize=(10, 14))

# Creating the bar chart as a horizontal chart
plt.barh(days, participants, height=0.6, color=[
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
    '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', 
    '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
    '#bcbd22', '#17becf', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
])

# Adding labels and title
plt.ylabel('Day of the Month')
plt.xlabel('Number of Participants')
plt.title('Daily Participants in Fitness Challenge - June 2023')

# Show the plot
plt.show()