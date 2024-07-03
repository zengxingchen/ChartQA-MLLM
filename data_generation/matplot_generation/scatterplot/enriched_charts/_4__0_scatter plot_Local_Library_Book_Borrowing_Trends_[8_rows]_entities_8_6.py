
import matplotlib.pyplot as plt

# Data for scatterplot
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
visitors_thousands = [30, 35, 40, 50, 70, 90, 100, 95, 80, 65, 50, 35]
average_spending_usd = [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310]

# Size of each point will be proportional to the number of visitors
sizes = [visitors * 10 for visitors in visitors_thousands]

# Different colors for different spending amounts (low to high)
colors = ['#1E90FF', '#00BFFF', '#87CEEB', '#32CD32', '#9ACD32', '#FFD700',
          '#FFA500', '#FF8C00', '#FF4500', '#FF6347', '#DC143C', '#8B0000']

# Create scatterplot
plt.figure(figsize=(14, 10))
plt.scatter(months, average_spending_usd, s=sizes, c=colors, alpha=0.7)

# Chart details
plt.title('Monthly Visitors and Average Spending Per Visitor', pad=20)
plt.xlabel('Month')
plt.ylabel('Average Spending (USD)')
plt.grid(True)

# Show the chart
plt.show()