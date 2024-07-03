
import matplotlib.pyplot as plt
import squarify

# Data points
apps = ['MyFitnessPal', 'Fitbit', 'Nike+ Run Club', 'Strava', 'Google Fit', 
        'Samsung Health', 'Garmin Connect', 'Runtastic', 'MapMyRun', 'Apple Health', 
        'Runkeeper', 'Endomondo', 'Pacer', 'Zombies, Run!', 'Couch to 5K', 
        'FitOn', 'JEFIT', 'StrongLifts', 'Freeletics', 'Aaptiv']
users_in_millions = [150, 120, 100, 95, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10]
colors = ['#ffcc00', '#ff9933', '#ff6666', '#99cc33', '#66cc99', '#339999', 
          '#3366cc', '#9966cc', '#cc3333', '#ff66b2', '#993333', '#b3b35e', 
          '#99cc00', '#556b2f', '#1e90ff', '#66ccff', '#99ccff', '#cc99ff', 
          '#ff99cc', '#ff9966']

# Plot Dimensions
plt.figure(figsize=(14, 10))

# Create a treemap
squarify.plot(sizes=users_in_millions, label=apps, color=colors, alpha=0.8)

# Title
plt.title('Number of Active Users of Fitness Apps (in Millions)', fontsize=18)

# Remove axes
plt.axis('off')

# Show plot
plt.show()