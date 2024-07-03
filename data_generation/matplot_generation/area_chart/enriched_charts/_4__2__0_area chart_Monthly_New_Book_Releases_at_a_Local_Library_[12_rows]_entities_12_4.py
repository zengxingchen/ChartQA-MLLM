
import matplotlib.pyplot as plt

# Data for the area chart
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
revenue = [110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 310, 330]

# Create the area chart
plt.figure(figsize=(14, 8))
plt.fill_between(months, revenue, color='#228B22')

# Adding a title and labels
plt.title('Monthly Revenue for ABC Enterprise', fontsize=18, pad=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Revenue (in thousands)', fontsize=15)

# Annotate the highest revenue
highest_revenue_idx = revenue.index(max(revenue))
plt.annotate('Highest Revenue', xy=(months[highest_revenue_idx], revenue[highest_revenue_idx]), 
             xytext=(months[highest_revenue_idx], revenue[highest_revenue_idx]+30),
             arrowprops=dict(facecolor='#FF6347', shrink=0.05))

# Customize ticks and grid
plt.xticks(rotation=45)
plt.yticks(range(0, max(revenue)+50, 50))
plt.grid(True, linestyle='--', alpha=0.7)

# Display the chart
plt.tight_layout()
plt.show()