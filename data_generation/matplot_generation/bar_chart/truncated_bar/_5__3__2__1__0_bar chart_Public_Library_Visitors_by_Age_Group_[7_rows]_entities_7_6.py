
import matplotlib.pyplot as plt

# Data
events = [
    "Music Concert", "Theater Play", "Dance Performance", "Opera", 
    "Comedy Show", "Magic Show", "Circus", "Ballet", 
    "Stand-up Comedy", "Musical", "Rock Concert", 
    "Jazz Night", "Symphony Orchestra", "Puppet Show"
]
attendance = [15000, 8000, 5000, 3000, 12000, 4000, 6000, 3500, 11000, 7500, 14000, 4500, 5500, 2000]

# Creating horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(events, attendance, color=[
    '#2E8B57', '#4682B4', '#D2691E', '#9ACD32',
    '#8A2BE2', '#5F9EA0', '#7FFF00', '#DC143C',
    '#FF8C00', '#8B0000', '#006400', '#B22222',
    '#FFD700', '#FF69B4'
], height=0.5)  # Change bar color and height

# Adding labels and title
ax.set_xlabel('Attendance')
ax.set_title('Attendance of Various Performing Arts Events in 2023', pad=20)

# Setting y-axis limit to truncate the chart
ax.set_xlim(1500, 16000)

# Show the plot
plt.show()