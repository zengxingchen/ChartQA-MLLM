
import matplotlib.pyplot as plt

# Data points - Number of gyms, average membership cost, average monthly attendance
countries = ["United States", "Germany", "Brazil", "Canada", "Australia", "Japan", 
             "United Kingdom", "China", "South Korea", "India", "Italy", "France", 
             "Spain", "Russia", "Mexico", "Indonesia", "South Africa", "Saudi Arabia", 
             "Turkey", "Argentina"]
num_gyms = [40000, 9500, 30000, 8000, 5000, 12000, 10000, 60000, 7000, 25000, 7000, 
            9000, 8000, 15000, 12000, 20000, 6000, 3000, 11000, 5000]
avg_membership_cost = [45, 35, 25, 40, 50, 30, 42, 20, 28, 18, 37, 39, 38, 22, 25, 
                       15, 30, 50, 20, 22]
avg_monthly_attendance = [35000, 8000, 20000, 5000, 7000, 15000, 9000, 60000, 
                          10000, 40000, 6000, 8000, 7000, 12000, 10000, 25000, 
                          5000, 4000, 9000, 6000]

# Create the bubble chart with a custom size
fig, ax = plt.subplots(figsize=(16, 10))

# Assign a color to each region
colors = {
    "United States": "#FF5733", "Germany": "#33FF57", "Brazil": "#3357FF", 
    "Canada": "#FFFF33", "Australia": "#FF33FF", "Japan": "#57FFF3", 
    "United Kingdom": "#F357FF", "China": "#F3573C", "South Korea": "#3CF357", 
    "India": "#5733FF", "Italy": "#33FF95", "France": "#FF3357", "Spain": "#33F3FF", 
    "Russia": "#FF9533", "Mexico": "#3C57F3", "Indonesia": "#95FF33", 
    "South Africa": "#33F3F3", "Saudi Arabia": "#F333FF", "Turkey": "#FF3C57", 
    "Argentina": "#F39533"
}

# Plot each data point and assign it a label, size, and color
for i, country in enumerate(countries):
    ax.scatter(num_gyms[i], avg_membership_cost[i], s=avg_monthly_attendance[i]*0.1,  # Adjust size scaling factor as desired
               c=colors[country], alpha=0.6, edgecolors="w", label=country)

# Customize the chart
ax.set_title('Gym Distribution, Membership Cost, and Monthly Attendance by Country', fontsize=18, pad=20)
ax.set_xlabel('Number of Gyms', fontsize=14)
ax.set_ylabel('Average Membership Cost in USD', fontsize=14)

# Customize the grid
ax.grid(True)

# Add legend
ax.legend(title="Countries", loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

# Show plot with a tight layout
plt.tight_layout()
plt.show()