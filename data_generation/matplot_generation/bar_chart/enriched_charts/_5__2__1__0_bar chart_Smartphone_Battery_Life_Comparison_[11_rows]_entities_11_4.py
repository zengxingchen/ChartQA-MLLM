
import matplotlib.pyplot as plt

# Sports league attendance data
leagues = [
    "NFL", "Bundesliga", "Premier League", "La Liga", "Serie A",
    "Ligue 1", "MLB", "NBA", "NHL", "MLS", 
    "A-League", "J-League", "Super Rugby", "Eredivisie", 
    "Russian Premier League", "Chinese Super League", 
    "Indian Super League", "Brazilian Serie A", "Turkish Super Lig", 
    "Scottish Premiership"
]
attendance = [
    67631, 43058, 38284, 27584, 24564, 
    22356, 28577, 17864, 17484, 21033, 
    10467, 19452, 16723, 19014, 
    13251, 24233, 18211, 17053, 15032, 
    15673
]

# New color scheme using specific color codes for each league
colors = [
    '#FF6347', '#4682B4', '#FFD700', '#32CD32', '#FF69B4',
    '#8A2BE2', '#DC143C', '#00CED1', '#FF4500', '#2E8B57',
    '#8B4513', '#BDB76B', '#1E90FF', '#FF8C00', 
    '#9932CC', '#D2691E', '#6495ED', '#FF1493', '#00BFFF', 
    '#FFDAB9'
]

# Create truncated vertical bar chart
plt.figure(figsize=(16, 12))  # Width and height of the chart
plt.bar(leagues, attendance, color=colors, width=0.6)  # Bar color and bar width

# Set the title and labels
plt.title('Average Attendance of Sports Leagues Worldwide', fontsize=18, pad=25)
plt.ylabel('Average Attendance', fontsize=14)
plt.xlabel('League', fontsize=14)

# Set y-axis limit to start from 10000
plt.ylim(10000, 70000)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the bar chart
plt.tight_layout()
plt.show()