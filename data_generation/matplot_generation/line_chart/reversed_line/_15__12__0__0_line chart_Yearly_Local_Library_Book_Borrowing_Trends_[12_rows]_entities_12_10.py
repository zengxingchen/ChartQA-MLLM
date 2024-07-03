
import matplotlib.pyplot as plt

# Data points
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
participants = [30, 45, 50, 40, 60, 55, 70, 65, 85, 75, 95, 90]

# Creating the line chart
plt.figure(figsize=(12, 8))

plt.plot(months, participants, color="#4682B4", marker='o')

# Annotating the highest and lowest participants
plt.annotate('Highest\n95 participants', xy=("November", 95), xytext=("November", 105),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05), ha='center')
plt.annotate('Lowest\n30 participants', xy=("January", 30), xytext=("January", 20),
             arrowprops=dict(facecolor='#7B68EE', shrink=0.05), ha='center')

# Title and labels
plt.title("Monthly Participation in Fitness Classes", fontsize=18, pad=20)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Number of Participants", fontsize=14)

# Customizing the grid
plt.grid(True, which='major', linestyle='--', linewidth=0.7, color='#D3D3D3')

# Invert y-axis
plt.gca().invert_yaxis()

# Show the plot
plt.show()