
import matplotlib.pyplot as plt

# Data
ages = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
investment_hours = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5]
investment_participants = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
startup_hours = [2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5]
startup_participants = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
stock_trading_hours = [2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
stock_trading_participants = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

# Create a bubble chart
plt.figure(figsize=(16, 10))  # Adjust the width and height

plt.scatter(ages, investment_hours, s=[i * 2 for i in investment_participants], c='#FF6F61', alpha=0.6, label='Investment')
plt.scatter(ages, startup_hours, s=[i * 2 for i in startup_participants], c='#6B5B95', alpha=0.6, label='Startups')
plt.scatter(ages, stock_trading_hours, s=[i * 2 for i in stock_trading_participants], c='#88B04B', alpha=0.6, label='Stock Trading')

# Customize the plot
plt.title('Average Time Spent on Financial Activities by Age Group', fontsize=20, pad=30)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Average Hours per Week', fontsize=14)
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()